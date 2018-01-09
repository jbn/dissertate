#!/bin/bash 

set -e
set -v

jupyter nbconvert \
    cli_tests/image_template/image_captions.ipynb \
    --template dissertate/dissertate.tpl \
    --to markdown 

grep "A captioned SVG" cli_tests/image_template/image_captions.md
grep "A captioned PNG" cli_tests/image_template/image_captions.md
grep "A captioned JPG" cli_tests/image_template/image_captions.md
