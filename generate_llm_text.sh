#!/bin/bash

PORT=$1
PROMPT=$2
EXPORT_FILE_LOCATION=$3

## Send a request to the server requesting prompt then save this request as a JSON file
echo "Sending prompt to llm [PORT:$PORT]..."
curl --location "http://$SLURM_JOB_NODELIST:$PORT/api/generate" --data "{\"model\":\"phi4-mini\",\"prompt\":\"$PROMPT\",\"stream\":false}" -s -o $EXPORT_FILE_LOCATION
echo "Response exported to $EXPORT_FILE_LOCATION."
