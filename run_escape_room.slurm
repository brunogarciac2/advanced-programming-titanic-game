#!/bin/bash
#SBATCH -N 1
#SBATCH -c 4
#SBATCH -p "tpg-gpu-small"
#SBATCH --qos="short"
#SBATCH --mem=16G
#SBATCH -t 02:00:00
#SBATCH --gres=gpu:turing:1
#SBATCH --job-name=Titanic-Escape-Room

source /etc/profile

echo "Running..."

## Generate the required LLM responses for challenge 4
chmod +x llm_server_init.sh
chmod +x generate_llm_text.sh

PLAINTEXT_LETTER_LLM_PROMPT_PATH="assets/llm_prompts/plaintext_letter_llm_prompt.txt"
ENCRYPTED_LETTER_LLM_PROMPT_PATH="assets/llm_prompts/encrypted_letter_llm_prompt.txt"

PLAINTEXT_LETTER_LLM_RESPONSE_PATH="assets/llm_responses/plaintext_letter_llm_response.json"
ENCRYPTED_LETTER_LLM_RESPONSE_PATH="assets/llm_responses/encrypted_letter_llm_response.json"

## Give read access to the files
chmod +r "$PLAINTEXT_LETTER_LLM_PROMPT_PATH"
chmod +r "$ENCRYPTED_LETTER_LLM_PROMPT_PATH"

## Start ollama container
singularity pull ollama.sif docker://ollama/ollama

echo "Initialising Server..."
PORT=11796
bash llm_server_init.sh $PORT

echo "Generating llm text for challenge 4..."

bash generate_llm_text.sh $PORT "$(cat $PLAINTEXT_LETTER_LLM_PROMPT_PATH)" "$PLAINTEXT_LETTER_LLM_RESPONSE_PATH"
bash generate_llm_text.sh $PORT "$(cat $ENCRYPTED_LETTER_LLM_PROMPT_PATH)" "$ENCRYPTED_LETTER_LLM_RESPONSE_PATH"

echo "[SUCCESS] Text generated."

echo "Initialising Virtual Environment..."
python3.11 -m venv .venv
source .venv/bin/activate

echo "Installing Requirements..."

pip install -r requirements.txt

echo "Generating challenges..."

python3.11 convert_to_html.py

echo "Challenge generation complete."

echo "Open 'gm_guide.html' with your preferred web browser to play!"
