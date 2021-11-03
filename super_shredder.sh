#!/bin/bash

shred -n 1 "$1"
sync
shred -n 1 -uz "$1"
