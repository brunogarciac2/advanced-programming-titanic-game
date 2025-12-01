# Local Setup Guide - Titanic Escape Room with LLM Integration

## Overview

This project uses **Ollama** with **phi4-mini** model to generate LLM text for Challenge 4. Here's how to set it up locally.

---

## Prerequisites

### 1. Install Ollama (Local LLM Runtime)

**Windows:**
```powershell
# Download installer from https://ollama.com/download
# Or use winget
winget install Ollama.Ollama
```

**Mac/Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Install Python Dependencies

```powershell
pip install -r requirements.txt
```

---

## Setup Steps

### Step 1: Start Ollama Server

**Check if Ollama is already running:**

```powershell
# Test if Ollama is responding
curl http://localhost:11434
```

If you see a response like "Ollama is running", **skip this step** - Ollama is already running!

**If Ollama is not running**, open a **new terminal** and run:

```powershell
# This starts Ollama on default port 11434
ollama serve
```

**Note:** If you see error `bind: Only one usage of each socket address...`, Ollama is already running as a background service. This is normal on Windows - you can proceed to the next step.

Keep this terminal open while running the game.

### Step 2: Pull the Model

In another terminal:

```powershell
# Download the phi4-mini model (recommended for this project)
ollama pull phi4-mini

# Alternative models (if phi4-mini is not available):
# ollama pull llama3.2
# ollama pull gemma2:2b
```

### Step 3: Test Ollama

```powershell
# Test that Ollama is working
ollama run phi4-mini "Write a short letter from someone on the Titanic"
```

If you see a response, Ollama is working correctly!

---

## Running the Game Locally

### Option 1: Use the Local Script (Recommended)

```powershell
# Run the complete game generation
python run_local.py
```

This will:
1. Check if Ollama is running
2. Generate LLM responses for Challenge 4
3. Generate all challenges
4. Convert to HTML
5. Open the game guide in your browser

### Option 2: Manual Step-by-Step

```powershell
# 1. Generate LLM text for Challenge 4
python generate_challenge_4_llm_local.py

# 2. Generate all challenges and convert to HTML
python convert_to_html.py

# 3. Open gm_guide.html in your browser
start gm_guide.html  # Windows
# or
open gm_guide.html   # Mac
```

---

## File Structure

```
project/
├── run_local.py                          # ⭐ Main entry point (LOCAL)
├── generate_challenge_4_llm_local.py     # ⭐ LLM generator (LOCAL)
├── run_escape_room.slurm                 # HPC cluster script
├── generate_challenge_4_llm_text.sh      # HPC cluster script
├── convert_to_html.py                    # HTML generator
├── generate_challenge.py                 # Challenge data generator
├── challenge4.py                         # Challenge 4 logic
├── requirements.txt                      # Python dependencies
├── plaintext_letter_llm_prompt.txt       # LLM prompt 1
├── encrypted_letter_llm_prompt.txt       # LLM prompt 2
├── plaintext_letter_llm_response.json    # Generated response 1
├── encrypted_letter_llm_response.json    # Generated response 2
└── gm_guide.html                         # Final output
```

---

## Configuration

### Ollama Settings

You can customize Ollama behavior in `generate_challenge_4_llm_local.py`:

```python
# Change model
MODEL = "phi4-mini"  # or "llama3.2", "gemma2:2b"

# Change Ollama URL (if running on different host/port)
OLLAMA_URL = "http://localhost:11434"

# Adjust temperature (0.0-1.0)
# Higher = more creative, Lower = more deterministic
TEMPERATURE = 0.7
```

---

## Troubleshooting

### Problem: "Connection refused" error

**Solution:**
- Make sure Ollama server is running: `ollama serve`
- Or check if it's already running: `curl http://localhost:11434`
- Check if port 11434 is not blocked

### Problem: "bind: Only one usage of each socket address" when running `ollama serve`

**Solution:**
- ✅ This is GOOD NEWS! Ollama is already running as a service
- On Windows, Ollama often runs automatically in the background
- You can proceed directly to running the game: `python run_local.py`
- No need to run `ollama serve` manually

### Problem: "Model not found"

**Solution:**
```powershell
ollama pull phi4-mini
```

### Problem: LLM responses are too short/weird

**Solution:**
- Try a different model: `ollama pull llama3.2`
- Adjust temperature in `generate_challenge_4_llm_local.py`
- Modify prompts in `plaintext_letter_llm_prompt.txt` and `encrypted_letter_llm_prompt.txt`

### Problem: "Out of memory"

**Solution:**
- Use a smaller model: `ollama pull gemma2:2b`
- Close other applications
- Restart Ollama: `killall ollama; ollama serve`

---

## Quick Start Commands

```powershell
# Full setup from scratch
ollama serve                              # Terminal 1
ollama pull phi4-mini                     # Terminal 2
python run_local.py                       # Terminal 2
```

---

## Differences: Local vs HPC Cluster

| Feature | Local (Windows/Mac) | HPC Cluster (Slurm) |
|---------|---------------------|---------------------|
| **Entry Script** | `run_local.py` | `run_escape_room.slurm` |
| **LLM Runtime** | Ollama (native) | Ollama (Singularity container) |
| **Model** | Downloaded via `ollama pull` | Pulled inside container |
| **Port** | 11434 (default) | 11796 (custom) |
| **Execution** | `python run_local.py` | `sbatch run_escape_room.slurm` |

---

## Advanced: Using Different Models

### Recommended Models for This Project

1. **phi4-mini** (Default) - Fast, good quality
   ```powershell
   ollama pull phi4-mini
   ```

2. **llama3.2** - Larger, better quality
   ```powershell
   ollama pull llama3.2
   ```

3. **gemma2:2b** - Smaller, faster
   ```powershell
   ollama pull gemma2:2b
   ```

### Using OpenAI API Instead

If you prefer to use OpenAI API instead of Ollama, modify `generate_challenge_4_llm_local.py`:

```python
import openai

openai.api_key = "your-api-key"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)
```

---

## Next Steps

1. ✅ Install Ollama
2. ✅ Pull the model
3. ✅ Run `python run_local.py`
4. ✅ Open `gm_guide.html` in your browser
5. 🎮 Play the escape room game!

---

**Need Help?** Check the troubleshooting section or open an issue on GitHub.
