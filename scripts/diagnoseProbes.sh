# Usage: source scripts/diagnoseProbes.sh <submission, e.g V45_reL1wTT_170pre5> <check log> [output dir]
# For each SPLIT FAILED task in a checkSubmission.sh log: downloads the probe stage log and the probe job
# stdouts from the scheduler (needs a valid grid proxy), prints the exit codes and the first cmsRun fatal
# exception, and the commands to look further. Called by checkMultiple.sh; can be rerun on its own.

_sub=$1
_log=$2
_outdir=${3:-logs/probes_$(date +%y%m%d-%H%M)}
_nprobes=${NPROBES:-5}

if [[ -z $_sub || ! -f $_log ]]; then
    echo "Error: run with e.g source scripts/diagnoseProbes.sh V45_reL1wTT_170pre5 logs/check_170pre5_<date>.log"
    return 1
fi

_proxy=$(voms-proxy-info -path 2> /dev/null)
_cadir=${X509_CERT_DIR:-/etc/grid-security/certificates}
_fetch() {  # url, output file; returns non-zero (and leaves no file) if not available
    curl -sf --cert "$_proxy" --key "$_proxy" --capath "$_cadir" -o "$2" "$1" || { rm -f "$2"; return 1; }
}

_tasks=$(source scripts/summariseCrabLog.sh --probelogs "$_log")
[[ -z $_tasks ]] && return 0
if [[ -z $_proxy ]]; then
    echo "  No grid proxy, cannot fetch the probe logs (voms-proxy-init -voms cms -rfc)"
    return 1
fi

echo "Probe diagnosis (logs in $_outdir):"
while read -r _task _url; do
    _dir=$_outdir/$_task
    mkdir -p "$_dir"
    _base=${_url%/*}
    _fetch "$_url" "$_dir/${_url##*/}"
    for _i in $(seq 1 $_nprobes); do
        _fetch "$_base/job_out.0-$_i.0.txt" "$_dir/job_out.0-$_i.0.txt"
    done

    echo "  $_task:"
    if ! ls "$_dir"/* &> /dev/null; then
        echo "    could not download anything from $_base (proxy not accepted, or logs already purged)"
    else
        # exit codes, e.g "8001 x5": from the probe stdouts, else from the probe stage log
        _src=$(ls "$_dir"/job_out.*.txt 2> /dev/null || ls "$_dir"/*.txt)
        _codes=$(cat $_src \
            | grep -oiE '(exit[ _]?code|exitcode)[^0-9]{0,15}[0-9]+' | grep -oE '[0-9]+$' | grep -v '^0$' \
            | sort | uniq -c | awk '{printf "%s%s x%s", sep, $2, $1; sep=", "}')
        echo "    probe exit codes: ${_codes:-none found}"
        # first fatal exception of any probe, without the "== CMSSW: " prefix of the CRAB wrapper
        _exc=$(cat "$_dir"/job_out.*.txt 2> /dev/null | sed 's/^== CMSSW: //' \
            | awk '/Begin Fatal Exception/ {on = 1} on {print; n++} /End Fatal Exception/ || n >= 15 {if (on) exit}')
        if [[ -n $_exc ]]; then
            echo "$_exc" | sed 's/^/    | /'
        else
            # no cmsRun exception: show what the job stdouts and the splitting log complain about instead
            cat "$_dir"/*.txt 2> /dev/null \
                | grep -iE 'error|exception|fail|killed|exceed|memory|wall ?clock|not found|denied' \
                | sed 's/^== CMSSW: //' | awk '!seen[$0]++' | head -8 | sed 's/^/    | /'
        fi
    fi
    echo "    more: crab getlog -d ntuples/$_sub/$_task/crab_$_task --short --jobids=0-1"
    echo "          or the probe stdouts at $_base/job_out.0-<1..$_nprobes>.0.txt"
done <<< "$_tasks"
