#!/bin/bash
wget -q -O wngsr.txt http://ir.eia.gov/ngs/wngsr.txt
grep Total wngsr.txt | awk '{print $3}' | head -1 | sed 's/,//'
