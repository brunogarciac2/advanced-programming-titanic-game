#!bin/bash

PORT=$1

## Run OLLAMA as a Daemon (background process)
echo "Running OLLAMA... [Port: $PORT, Node: $SLURM_JOB_NODELIST]"
singularity run --nv --env OLLAMA_HOST=0.0.0.0:$PORT ollama.sif serve &

## Wait until server is set up
until curl -s http://$SLURM_JOB_NODELIST:$PORT/health > /dev/null; do
        sleep 1
done

echo "OLLAMA ready to receive commands."
