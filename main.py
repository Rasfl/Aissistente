import os
import argparse

from dotenv import load_dotenv
from openai import OpenAI
from config import system_prompt
from call_function import available_functions, call_function
import json

# dotenv part + Apikey
def main() -> None:

    # Parser with the user msg
    parser = argparse.ArgumentParser(description="Aissistente")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Ativar modo detalhado")
    args = parser.parse_args()
    #---

    load_dotenv()

    # o uso do env_path é para que idependente onde o usuario esteja, ao rodar main.py, ele procura na pasta raiz de main.py
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError('OPENROUTER_API_KEY not set. Configure it in the environment or the expected dotenv file path.')
    # ---
    # OpenAi Class and configs
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key,)
    messages: list[dict[str, str]] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": args.user_prompt},
        ]
    
    # ---
    generate_content(client, messages, args)

def generate_content(client:OpenAI, messages:list, args) -> None:
    # Core function
    completion = client.chat.completions.create(
        model="deepseek/deepseek-v4-flash-0731",
        messages= messages,
        tools=available_functions,
    )
    # ---
    # tokenUsage to track the consumption from the AI Tokens, also raise RuntimeError if usage == None
    if not completion.usage:
        raise RuntimeError("Failed API request")
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {completion.usage.prompt_tokens}")
        print(f"Response tokens: {completion.usage.completion_tokens}")
    # ---

    print("Response:")

    message = completion.choices[0].message

    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose=args.verbose)

            if not result_message.get("content"):
                return f"Empty response from tool: {tool_call.function.name}"

            if args.verbose:
                print(f"-> {result_message['content']}")
    
    else:
        print(message.content)

if __name__ == "__main__":
    main()

