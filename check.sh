#!/bin/bash

vats=(CZ28987373 DE296459264 DE292188391 SE556900620701 NL802465602B01 NL151412984B01 GB163980581 PL9492191021 CZ64610748 IT06700351213)

for v in ${vats[@]}; do
  echo checking $v
  python vatcheck.py $v
  echo
done