import os
import argparse

from dotenv import load_dotenv
from openai import OpenAI

# dotenv part + Apikey
def main() -> None:
    load_dotenv()

    messages: list[dict[str, str, str, object]] = [
        {
            "role": "user",
            "content": args.user_prompt
        }]
    # o uso do env_path é para que idependente onde o usuario esteja, ao rodar main.py, ele procura na pasta raiz de main.py
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError('OPENROUTER_API_KEY not set. Configure it in the environment or the expected dotenv file path.')
    # ---

    # Parser with the user msg
    parser = argparse.ArgumentParser(description="Aissistente")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    #---
    # OpenAi Class and configs
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key,)

    completion = client.chat.completions.create(
        model="deepseek/deepseek-v4-flash-0731",
        messages= messages
    )
    # ---

    # tokenUsage to track the consumption from the AI Tokens, also raise RuntimeError if usage == None
    def tokenUsage(completion) -> None:
        if not completion.usage:
            raise RuntimeError("Failed API request")
        promptTokens: int = completion.usage.prompt_tokens
        completionTokens: int = completion.usage.completion_tokens

        print(f"Prompt tokens: {promptTokens}")
        print(f"Response tokens: {completionTokens}")
    tokenUsage(completion)
    # ---

    print("Reponse:")
    print(completion.choices[0].message.content)

if __name__ == "__main__":
    main()