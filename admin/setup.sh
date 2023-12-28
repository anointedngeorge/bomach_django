#!/bin/bash
pip install --upgrade pip pip
pip install --upgrade pip setuptools

cat requirements.txt | xargs -n 1 pip install