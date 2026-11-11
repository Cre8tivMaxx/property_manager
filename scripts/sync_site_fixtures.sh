#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
bench_root="${BENCH_ROOT:-/home/frappe/frappe-bench}"

cd "$bench_root"
output="$(
  printf 'from scripts.export_site_fixtures import run; run(); print("SYNC_" + "COMPLETE")\n' | \
    PYTHONPATH="$repo_root${PYTHONPATH:+:$PYTHONPATH}" \
    PROPERTY_MANAGER_REPO="$repo_root" \
    nice -n 10 bench --site property-mgmt console
)"
if [[ "$output" != *SYNC_COMPLETE* ]]; then
  printf '%s\n' "$output" >&2
  exit 1
fi
printf '%s\n' "$output" | sed -n '/Client Script:/,/Dashboard Chart Source:/p' | sed 's/^In \[1\]: //'
