#!/usr/bin/bash

MODEL_PKG="./model_store/helmet_detection.mar"
if [ ! -f $MODEL_PKG ]; then
    echo "  ERROR: Model package file not found!"
    exit 1
fi

torchserve \
  --start \
  --ncs \
  --model-store "./model_store" \
  --models "./model_store/helmet_detection.mar" \
  --ts-config config.properties