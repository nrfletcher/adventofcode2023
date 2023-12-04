#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <day_number> <input_choice>"
    exit 1
fi

day_number="$1"
input_choice="$2"

script_filename="day${day_number}.py"

python main.py "${script_filename}" "${input_choice}"
