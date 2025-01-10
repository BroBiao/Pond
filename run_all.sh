#!/bin/bash

for dir in */; do
    cd "$dir" || continue
    python3 random_pred.py
    cd ..
done

