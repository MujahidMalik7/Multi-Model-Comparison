# Multi-Model Comparison Tool

A Python command-line tool that sends the same prompt to **Claude Haiku** and **Llama 3.3 70B** simultaneously and displays responses side by side.

## Features
- Runs both models in parallel using `async/await`
- Displays response time and token usage for each model
- Supports custom temperature settings using `--temperature` e.g `"prompt" --temperature=0.3`
- Forces structured JSON output with `--json` flag
- Saves all interactions to a local log file with timestamps

## Models Used
- `claude-haiku-4-5-20251001` by Anthropic
- `llama-3.3-70b-versatile` by Meta (via Groq)

## Setup
```bash
# 1. Clone the repository
git clone https://github.com/MujahidMalik7/Multi-Model-Comparison.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create your .env file
cp .env.example .env

# 4. Add your API keys to .env
ANTHROPIC_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
```

## Usage
```bash
# Basic usage
python compare.py "Your prompt here"

# With custom temperature
python compare.py "Your prompt" --temperature 1.2

# Force JSON output
python compare.py "Your prompt" --json
```

## Example Output
```
==================================================
            MODEL COMPARISON
==================================================

[ claude-haiku-4-5-20251001 ]
Time   : 2.20s
Tokens : 59
Answer : The capital of Pakistan is Islamabad. It is located
in the Islamabad Capital Territory in the northern part of
the country and has been the capital since 1967.

--------------------------------------------------

[ llama-3.3-70b-versatile ]
Time   : 0.54s
Tokens : 50
Answer : The capital of Pakistan is Islamabad.

==================================================
```

## Real Comparison Examples

### Factual Question
**Prompt:** `"Who is the founder of Pakistan?"`

| | Claude Haiku | Llama 3.3 70B |
|---|---|---|
| Time | 1.32s | 1.33s |
| Tokens | 74 | 384 |
| Style | Concise with key dates | Detailed essay-style |

### Creative Question
**Prompt:** `"If you could fix one thing about the internet?"`

| | Claude Haiku | Llama 3.3 70B |
|---|---|---|
| Time | 3.55s | 1.49s |
| Tokens | 210 | 391 |
| Style | Thoughtful, original angle | Structured, comprehensive |

### JSON Mode
**Prompt:** `"Give me 3 programming languages with creator and year" --json`

**Claude output:**
```json
{
  "programming_languages": [
    {"name": "Python", "creator": "Guido van Rossum", "year_created": 1991},
    {"name": "JavaScript", "creator": "Brendan Eich", "year_created": 1995},
    {"name": "Java", "creator": "James Gosling", "year_created": 1995}
  ]
}
```

**Llama output:**
```json
{
  "languages": [
    {"name": "Java", "creator": "James Gosling", "year": 1995},
    {"name": "Python", "creator": "Guido van Rossum", "year": 1991},
    {"name": "C++", "creator": "Bjarne Stroustrup", "year": 1983}
  ]
}
```

## API Keys Required
- Anthropic API key: https://console.anthropic.com
- Groq API key: https://console.groq.com
