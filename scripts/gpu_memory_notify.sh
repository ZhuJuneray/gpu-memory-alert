#!/bin/bash

# Load configurations
source /path/to/gpu-memory-alert/config/thresholds.conf

# Log file path
LOG_FILE="/path/to/gpu-memory-alert/logs/gpu_monitor.log"

# Check GPU memory usage using gpustat
gpustat --json | jq '.gpus[] | select(.memory.used < env.MEMORY_THRESHOLD) | {id: .index, memory: .memory.used}' | while read -r line; do
    GPU_ID=$(echo $line | jq -r '.id')
    MEM_USED=$(echo $line | jq -r '.memory')

    # Email notification
    MESSAGE="GPU ${GPU_ID} memory usage is ${MEM_USED}MiB, below threshold ${MEMORY_THRESHOLD}MiB."
    echo "$MESSAGE" | mail -s "GPU Memory Below Threshold Alert" $EMAIL_RECIPIENT

    # Log the event
    echo "$(date): $MESSAGE" >> $LOG_FILE
done
