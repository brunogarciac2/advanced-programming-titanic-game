#!/bin/bash

PORT=11796
PROMPT=$1
EXPORT_FILE_LOCATION=$2

## Run OLLAMA as a Daemon (background process)
echo "Running OLLAMA... [Port: $PORT, Node: $SLURM_JOB_NODELIST]"
singularity run --nv --env OLLAMA_HOST=0.0.0.0:$PORT ollama.sif serve &

## Wait until server is set up
until curl -s http://$SLURM_JOB_NODELIST:$PORT/health > /dev/null; do
        sleep 1
done

echo "OLLAMA ready to receive commands."

## Send a request to the server for a story about peguins then save this request as a JSON file
echo "Sending commands..."
curl --location "http://$SLURM_JOB_NODELIST:$PORT/api/generate" --data "{\"model\":\"phi4-mini\",\"prompt\":\"$PROMPT\",\"stream\":false}" -o $EXPORT_FILE_LOCATION
echo "Response exported to $EXPORT_FILE_LOCATION."
