#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:56:52 2023

@author: drasken
"""

import argparse
from pathlib import Path

parser = argparse.ArgumentParser(prog='Simple CLI Program')

parser.add_argument("path", help='the path to the target directory')

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)
