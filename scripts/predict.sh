#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 2 ]]; then
  echo "Usage: bash scripts/predict.sh INPUT_DIR OUTPUT_DIR" >&2
  exit 2
fi
nnUNetv2_predict -i "$1" -o "$2" -d Dataset413_microctbycsm -c 3d_fullres -f 0 -tr nnUNetTrainer
