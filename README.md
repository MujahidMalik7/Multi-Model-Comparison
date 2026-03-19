# Multi-Model Comparison Tool

A Python command-line tool that sends the same prompt to **Claude Haiku** and **Llama 3.3 70B** simultaneously and displays responses side by side.

## Features
- Runs both models in parallel using async/await
- Displays response time and token usage for each model
- Supports custom temperature settings
- Forces structured JSON output with --json flag
- Saves all interactions to a local log file with timestamps

## Models Used
- Claude Haiku (claude-haiku-4-5-20251001) by Anthropic
- Llama 3.3 70B Versatile by Meta (via Groq)

## Setup

1. Clone the repository
   git clone https://github.com/yourusername/Multi-Model-Comparison.git

2. Install dependencies
   pip install -r requirements.txt

3. Create your .env file
   cp .env.example .env

4. Add your API keys to .env
   ANTHROPIC_API_KEY=your_key_here
   GROQ_API_KEY=your_key_here

## Usage

Basic usage:
   python compare.py "Your prompt here"

With custom temperature:
   python compare.py "Your prompt" --temperature 1.2

Force JSON output:
   python compare.py "Your prompt" --json

## Example Output

==================================================
            MODEL COMPARISON
==================================================

[ claude-haiku-4-5-20251001 ]
Time   : 1.56s
Tokens : 173
Answer : The capital of Pakistan is Islamabad.

--------------------------------------------------

[ llama-3.3-70b-versatile ]
Time   : 0.54s
Tokens : 50
Answer : The capital of Pakistan is Islamabad.

==================================================

## API Keys Required
- Anthropic API key: https://console.anthropic.com
- Groq API key: https://console.groq.com