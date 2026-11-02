# Usage: source scripts/summariseCrabLog.sh [--names "<CATEGORY|CATEGORY>"] <check log> [<check log> ...]
# One line per CRAB task from a checkSubmission.sh log, grouped so the tasks needing attention come first.
# Works on old logs too, so you can re-summarise without calling crab status again.
# --names prints only the names of tasks in the given categories (e.g. FAILED), one per line, for use in other scripts
# --probelogs prints "<task> <probe stage log URL>" for each SPLIT FAILED task, for scripts/diagnoseProbes.sh

_want=""
_probelogs=0
if [[ $1 == "--names" ]]; then _want=$2; shift 2; fi
if [[ $1 == "--probelogs" ]]; then _probelogs=1; shift; fi

for _crablog in "$@"; do
    awk -v want="$_want" -v probelogs="$_probelogs" '
    function flush() {
        if (name == "") return
        n++; names[n] = name
        if (length(name) > w) w = length(name)
        line[n] = describe()
        extra[n] = (cat[n] == "SPLIT FAILED" && probelog != "") ? "probe stage log: " probelog : ""
        plog[n] = probelog
        name = ""; server = ""; sched = ""; msg = ""; codes = ""; tape = 0; nodir = 0; age = ""; purged = 0
        boot = ""; nostatus = 0; probelog = ""
        delete jobs; delete probe; njobtot = 0; nprobetot = 0
    }
    function counts(arr, tot,   s, out) {
        out = ""
        for (s in arr) out = out ", " arr[s] " " s
        return substr(out, 3)
    }
    function describe(   active, s, done, failed) {
        if (nodir)                                    { cat[n] = "NO CRAB DIR"; return "crab_ directory not found" }
        if (purged && server ~ /REFUSED|FAILED|KILLED/) { cat[n] = server;    return "last known status, task submitted " age " days ago" (tape ? " (input on TAPE)" : "") }
        if (purged)                                   { cat[n] = "PURGED";      return "submitted " age " days ago, job details purged from the scheduler after 40 days" }
        if (server == "")                             { cat[n] = "UNKNOWN";     return (msg != "" ? msg : "no status from crab (proxy expired?)") }
        if (server == "KILLED" && njobtot == 0) { cat[n] = "KILLED"; return "task killed" (nprobetot ? ", probe jobs: " counts(probe) : "") " - move, then submit fresh" }
        if (server ~ /REFUSED|FAILED|KILLED/ && njobtot == 0) {
            cat[n] = server
            return (tape ? "input on TAPE only - recall to disk, then submit fresh (resubmit will not work)" : msg)
        }
        # automatic splitting: probes ran but the scheduler failed before any processing jobs were made - will never progress
        if (njobtot == 0 && sched == "FAILED") {
            cat[n] = "SPLIT FAILED"
            return "probe jobs: " (nprobetot ? counts(probe) : "none") ", but no processing jobs were created (scheduler FAILED) - check the probe stage log, then unstick"
        }
        # on the scheduler but it reports nothing: normal for a few minutes after submission, stuck after much longer
        if (nostatus && boot + 0 > 120) { cat[n] = "STUCK"; return "on the scheduler for " boot " min with no status info - unstick (or report it if it keeps happening)" }
        if (nostatus) { cat[n] = "PROBING"; return "just reached the scheduler, no status info yet" }
        if (njobtot == 0) { cat[n] = "PROBING"; return (nprobetot ? "probe jobs: " counts(probe) : (sched != "" ? "waiting to start, scheduler " sched : "waiting to start, no scheduler status yet")) }
        done = jobs["finished"] + 0; failed = jobs["failed"] + jobs["killed"]
        active = njobtot - done - failed
        s = done "/" njobtot " finished"
        if (failed) s = s ", " failed " failed" (codes != "" ? " (exit" codes ")" : "")
        for (st in jobs) if (st != "finished" && st != "failed" && st != "killed") s = s ", " jobs[st] " " st
        if (server == "KILLED") { cat[n] = "KILLED"; return s " - task killed, move, then submit fresh" }
        if (active > 0)  cat[n] = "RUNNING"
        else if (failed) { cat[n] = "FAILED"; s = s " - crab resubmit" }
        else             cat[n] = "DONE"
        return s
    }
    # one "state  pct% (n/N)" entry, on the status line itself or a continuation line
    function addstate(txt, arr,   st, c) {
        sub(/^.*status:[ \t]*/, "", txt); sub(/^[ \t]+/, "", txt)
        split(txt, f, /[ \t]+/); st = f[1]
        if (!match(txt, /\( *[0-9]+\//)) return 0
        c = substr(txt, RSTART + 1, RLENGTH - 2); gsub(/ /, "", c)
        arr[st] += c
        return c + 0
    }
    /^Processing: /                  { flush(); name = $2; next }
    /^Skipping /                     { flush(); name = $2; sub(/:$/, "", name); nodir = 1; flush(); next }
    /^All directories processed/     { flush(); next }
    /^Status on the CRAB server:/    { server = $NF }
    /^Status on the scheduler:/      { sched = $NF }
    /^Jobs status:/                  { block = "jobs";  njobtot   += addstate($0, jobs);  next }
    /^Probe Jobs status:/            { block = "probe"; nprobetot += addstate($0, probe); next }
    block != "" && /^[ \t]+[A-Za-z]+[ \t]+[0-9.]+%/ {
        if (block == "jobs") njobtot += addstate($0, jobs); else nprobetot += addstate($0, probe)
        next
    }
    { block = "" }
    /jobs failed with exit code/     { codes = codes " " $NF "x" $1 }
    /TAPE/                           { tape = 1 }
    /^Task was submitted [0-9]+ days ago/ { age = $4 }
    /^Files are purged from Grid scheduler/ { purged = 1 }
    /^Task bootstrapped on schedd more than [0-9]+ minutes ago/ { boot = $(NF-2) }
    /no status info is available yet/ { nostatus = 1 }
    /^Probe stage log:/              { probelog = $NF }
    /^(Warning|Error|ERROR)/ && msg == "" { msg = $0; sub(/^[A-Za-z]+:[ \t]*/, "", msg); msg = substr(msg, 1, 100) }
    END {
        flush()
        if (probelogs) { for (i = 1; i <= n; i++) if (cat[i] == "SPLIT FAILED" && plog[i] != "") print names[i], plog[i]; exit }
        if (want != "") { for (i = 1; i <= n; i++) if (cat[i] ~ ("^(" want ")$")) print names[i]; exit }
        split("NO CRAB DIR,UNKNOWN,SUBMITREFUSED,SUBMITFAILED,KILLED,FAILED,SPLIT FAILED,STUCK,PROBING,RUNNING,DONE,PURGED", order, ",")
        for (o = 1; o in order; o++) {
            for (i = 1; i <= n; i++) if (cat[i] == order[o]) {
                printf "  %-13s %-" w "s  %s\n", cat[i], names[i], line[i]; tally[cat[i]]++; seen[i] = 1
                if (extra[i] != "") printf "  %-13s %-" w "s  %s\n", "", "", extra[i]
            }
        }
        for (i = 1; i <= n; i++) if (!seen[i]) { printf "  %-13s %-" w "s  %s\n", cat[i], names[i], line[i]; tally[cat[i]]++ }
        t = ""; for (o = 1; o in order; o++) if (order[o] in tally) t = t ", " tally[order[o]] " " order[o]
        printf "  -> %d tasks: %s\n", n, substr(t, 3)
    }' "$_crablog"
done
