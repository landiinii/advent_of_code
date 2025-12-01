#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TODAY=$(date +%-d)
TOMORROW=$((TODAY + 1))

for day in $TODAY $TOMORROW; do
    day_dir="$SCRIPT_DIR/Day$day"

    [ ! -d "$day_dir" ] && mkdir -p "$day_dir"
    [ ! -f "$day_dir/test.txt" ] && touch "$day_dir/test.txt"
    [ ! -f "$day_dir/input.txt" ] && touch "$day_dir/input.txt"
    [ ! -f "$day_dir/main.go" ] && cp "$SCRIPT_DIR/template/main.go" "$day_dir/main.go"
    [ ! -f "$day_dir/go.mod" ] && cp "$SCRIPT_DIR/template/go.mod" "$day_dir/go.mod"
done
