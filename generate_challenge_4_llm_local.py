"""
Local LLM Text Generator for Challenge 4
Uses Ollama to generate letter content for the Titanic Escape Room game
"""

import requests
import json
import os
import sys
import time

# Configuration
OLLAMA_URL = "http://localhost:11434"
MODEL = "phi4-mini"  # You can change this to "llama3.2", "gemma2:2b", etc.
TEMPERATURE = 0.7

# File paths
PLAINTEXT_PROMPT_FILE = "plaintext_letter_llm_prompt.txt"
ENCRYPTED_PROMPT_FILE = "encrypted_letter_llm_prompt.txt"
PLAINTEXT_RESPONSE_FILE = "plaintext_letter_llm_response.json"
ENCRYPTED_RESPONSE_FILE = "encrypted_letter_llm_response.json"


def check_ollama_running():
    """Check if Ollama server is running"""
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=2)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False


def check_model_exists(model_name):
    """Check if the model is downloaded"""
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags")
        models = response.json().get("models", [])
        return any(model["name"].startswith(model_name) for model in models)
    except:
        return False


def generate_llm_response(prompt, model=MODEL, temperature=TEMPERATURE):
    """
    Generate text using Ollama API
    
    Args:
        prompt: The prompt text
        model: Model name (default: phi4-mini)
        temperature: Sampling temperature (0.0-1.0)
    
    Returns:
        dict: Ollama response JSON
    """
    url = f"{OLLAMA_URL}/api/generate"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature
        }
    }
    
    print(f"[GENERATING] Sending prompt to Ollama ({model})...")
    print(f"[PROMPT] {prompt[:100]}...")
    
    try:
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        
        result = response.json()
        print(f"[OK] Generated {len(result.get('response', ''))} characters")
        return result
        
    except requests.exceptions.Timeout:
        print("[ERROR] Request timed out. Try using a smaller model.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        sys.exit(1)


def main():
    print("=" * 60)
    print("Challenge 4 LLM Text Generator (Local)")
    print("=" * 60)
    
    # Step 1: Check if Ollama is running
    print("\n[STEP 1] Checking Ollama server...")
    if not check_ollama_running():
        print("[ERROR] Ollama server is not running!")
        print("\nTo start Ollama, open a new terminal and run:")
        print("  ollama serve")
        print("\nOr install Ollama from: https://ollama.com/download")
        sys.exit(1)
    print("[OK] Ollama server is running")
    
    # Step 2: Check if model exists
    print(f"\n[STEP 2] Checking if model '{MODEL}' is downloaded...")
    if not check_model_exists(MODEL):
        print(f"[ERROR] Model '{MODEL}' not found!")
        print(f"\nTo download the model, run:")
        print(f"  ollama pull {MODEL}")
        print("\nAlternative models:")
        print("  ollama pull llama3.2")
        print("  ollama pull gemma2:2b")
        sys.exit(1)
    print(f"[OK] Model '{MODEL}' is available")
    
    # Step 3: Read prompts
    print("\n[STEP 3] Reading prompt files...")
    
    if not os.path.exists(PLAINTEXT_PROMPT_FILE):
        print(f"[ERROR] Prompt file '{PLAINTEXT_PROMPT_FILE}' not found!")
        sys.exit(1)
    
    if not os.path.exists(ENCRYPTED_PROMPT_FILE):
        print(f"[ERROR] Prompt file '{ENCRYPTED_PROMPT_FILE}' not found!")
        sys.exit(1)
    
    with open(PLAINTEXT_PROMPT_FILE, 'r', encoding='utf-8') as f:
        plaintext_prompt = f.read().strip()
    
    with open(ENCRYPTED_PROMPT_FILE, 'r', encoding='utf-8') as f:
        encrypted_prompt = f.read().strip()
    
    print(f"[OK] Read 2 prompts")
    
    # Step 4: Generate responses
    print("\n[STEP 4] Generating LLM responses...")
    print("This may take 30-60 seconds per prompt...\n")
    
    # Generate plaintext letter
    print("[1/2] Generating plaintext letter...")
    start_time = time.time()
    plaintext_response = generate_llm_response(plaintext_prompt)
    print(f"      Completed in {time.time() - start_time:.1f} seconds")
    
    # Save plaintext response
    with open(PLAINTEXT_RESPONSE_FILE, 'w', encoding='utf-8') as f:
        json.dump(plaintext_response, f, indent=2, ensure_ascii=False)
    print(f"      Saved to: {PLAINTEXT_RESPONSE_FILE}")
    
    # Generate encrypted letter
    print("\n[2/2] Generating encrypted letter...")
    start_time = time.time()
    encrypted_response = generate_llm_response(encrypted_prompt)
    print(f"      Completed in {time.time() - start_time:.1f} seconds")
    
    # Save encrypted response
    with open(ENCRYPTED_RESPONSE_FILE, 'w', encoding='utf-8') as f:
        json.dump(encrypted_response, f, indent=2, ensure_ascii=False)
    print(f"      Saved to: {ENCRYPTED_RESPONSE_FILE}")
    
    # Step 5: Done
    print("\n" + "=" * 60)
    print("[SUCCESS] LLM text generation complete!")
    print("=" * 60)
    print("\nGenerated files:")
    print(f"  ✓ {PLAINTEXT_RESPONSE_FILE}")
    print(f"  ✓ {ENCRYPTED_RESPONSE_FILE}")
    print("\nNext step:")
    print("  python convert_to_html.py")


if __name__ == "__main__":
    main()
