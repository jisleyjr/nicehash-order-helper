#!/bin/bash
echo 'Launching nicehash_python'

SRCDIR="`pwd`/src"

docker run --name nicehash_python -v $SRCDIR:/app --rm nicehash_python:latest