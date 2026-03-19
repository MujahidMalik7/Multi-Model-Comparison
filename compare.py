from anthropic import AsyncAnthropic
from groq import AsyncGroq
import asyncio, argparse, json, datetime, time, dotenv,os
from dotenv import load_dotenv

load_dotenv()

async def call_claude(prompt, temperature, json_mode):

    client = AsyncAnthropic()
    start_time = time.time()
    model = "claude-haiku-4-5-20251001"

    response = await client.messages.create(
        messages=[{"role": "user", "content": prompt}],
        model = model,
        temperature = temperature,
        max_tokens = 2000,
    )

    answer = response.content[0].text
    
    if json_mode:
        answer = answer.strip()
        answer = answer.removeprefix("```json").removeprefix("```")
        answer = answer.removesuffix("```").strip()

    end_time = time.time()    
    estimated_time = end_time - start_time
    token_usage = response.usage.input_tokens + response.usage.output_tokens

    return {
        "model"  : model,
        "answer" : answer,
        "time"   : estimated_time,
        "tokens" : token_usage
    }

async def call_grok(prompt,temperature,json_mode):

    client = AsyncGroq()
    start_time = time.time()
    model = 'llama-3.3-70b-versatile'

    response = await client.chat.completions.create(
        messages = [{"role": "user", "content": prompt}],
        model = model,
        temperature = temperature
    )

    answer = response.choices[0].message.content

    if json_mode:
        answer = answer.strip()
        answer = answer.removeprefix("```json").removeprefix("```")
        answer = answer.removesuffix("```").strip()
    
    end_time = time.time()    
    estimated_time = end_time - start_time
    token_usage = response.usage.total_tokens

    return {
        "model"  : model,
        "answer" : answer,
        "time"   : estimated_time,
        "tokens" : token_usage
    }

def display_results(claude_result, groq_result):
    print()
    print ("=" * 50)
    print ("            MODEL COMPARISON            ")
    print ("=" * 50)
    print()
    
    print (f"[ {claude_result['model']} ]")
    print (f"Time   : {claude_result['time']:.2f}s")
    print (f"Tokens : {claude_result['tokens']}")
    print (f"Answer : {claude_result['answer']}") 

    print ("-" * 50)

    print (f"[ {groq_result['model']} ]")
    print (f"Time   : {groq_result['time']:.2f}s")
    print (f"Tokens : {groq_result['tokens']}")
    print (f"Answer : {groq_result['answer']}")
    
    print()
    print ("=" * 50)

def save_log(prompt, temperature, claude_result, groq_result):
    
    new_entry = {
        "timestamp"    : datetime.datetime.now().isoformat(),
        "prompt"       : prompt,
        "temperature"  : temperature,
        "claude_result": claude_result,
        "groq_result"  : groq_result
    }

    if os.path.exists('log.json'):
        with open('log.json', 'r') as f:
            try:
                logs = json.load(f)
                
                if not isinstance(logs, list):
                    logs = []
            except json.JSONDecodeError:
                logs = []
    else:
        logs = []
    
    logs.append(new_entry)
    with open('log.json', 'w') as f:
        json.dump(logs, f, indent = 4)

async def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('prompt', type=str, help = "")
    parser.add_argument('--temperature', type=float, default = 0.7, help="")
    parser.add_argument('--json', action = 'store_true', help = "")

    args = parser.parse_args()

    prompt = args.prompt
    
    if args.json is True:
        prompt = prompt + " Return ONLY raw JSON. No markdown, no code blocks, no explanation. Just the JSON object."

    
    claude_result, groq_result = await asyncio.gather (
        call_claude(prompt, args.temperature, args.json),
        call_grok(prompt, args.temperature, args.json)
    )

    display_results(claude_result, groq_result)
    save_log(prompt, args.temperature, claude_result, groq_result)

if __name__ == "__main__":
    asyncio.run(main())