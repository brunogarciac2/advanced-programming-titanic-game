#!/bin/bash
#SBATCH -N 1
#SBATCH -c 4
#SBATCH -p "tpg-gpu-small"
#SBATCH --qos="short"
#SBATCH --mem=16G
#SBATCH -t 02:00:00
#SBATCH --gres=gpu:turing:1
#SBATCH --job-name=LLM_TESTING_HOST

source /etc/profile

echo "Running..."

## Generate the required LLM responses for challenge 4
chmod +x generate_challenge_4_llm_text.sh
chmod +r plaintext_letter_llm_prompt.txt

echo "$(cat plaintext_letter_llm_prompt.txt)"

./generate_challenge_4_llm_text.sh "$(cat plaintext_letter_llm_prompt.txt)" "plaintext_letter_llm_response.json"
./generate_challenge_4_llm_text.sh "$(cat encrypted_letter_llm_prompt.txt)" "encrypted_letter_llm_response.json"
