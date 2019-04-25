#!/bin/bash 

set -e
set -v

jupyter nbconvert \
    cli_tests/image_template/image_captions.ipynb \
    --config cli_tests/nb_config.py \
    --to markdown 

grep "A captioned SVG" cli_tests/image_template/image_captions.md
grep "A captioned PNG" cli_tests/image_template/image_captions.md
grep "A captioned JPG" cli_tests/image_template/image_captions.md

# tags: ["todo"]
grep "TODO" cli_tests/image_template/image_captions.md | wc -l | grep "0"

# tags: ["setup"]
grep "import matplotlib" cli_tests/image_template/image_captions.md | wc -l | grep "0"

# tags: ["private"]
grep "A private cell" cli_tests/image_template/image_captions.md | wc -l | grep "0"
