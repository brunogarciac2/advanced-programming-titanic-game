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
chmod +x generate_challenge_4_llm_text.sh
chmod +r plaintext_letter_llm_prompt.txt

## Start ollama container
singularity pull ollama.sif docker://ollama/ollama

echo "Generating llm text for challenge 4..."

$PLAINTEXT_LETTER_LLM_PROMPT_PATH="./assets/llm_prompts/plaintext_letter_llm_prompt.txt"
$ENCRYPTED_LETTER_LLM_PROMPT_PATH="./assets/llm_prompts/encrypted_letter_llm_prompt.txt"

$PLAINTEXT_LETTER_LLM_RESPONSE_PATH="./assets/llm_prompts/plaintext_letter_llm_response.json"
$ENCRYPTED_LETTER_LLM_RESPONSE_PATH="./assets/llm_prompts/encrypted_letter_llm_response.json"

bash generate_challenge_4_llm_text.sh "$(cat $PLAINTEXT_LETTER_LLM_PATH)" "plaintext_letter_llm_response.json"
bash generate_challenge_4_llm_text.sh "$(cat $ENCRYPTED_LETTER_LLM_PATH)" "encrypted_letter_llm_response.json"

echo "[SUCCESS] Text generated."

echo "Installing Requirements..."

pip install -r requirements.txt

echo "Generating challenges..."

python3.12 convert_to_html.py

echo "Challenge generation complete."

echo "Open 'gm_guide.html' with your preferred web browser to play!"
