import openai
import sys
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def main(prompt_text):
    response = openai.Completion.create(
    engine="text-davinci-002",
    max_tokens=100,
    prompt=f"{prompt_text}"
    )
    return response

if __name__ == "__main__":
    args = sys.argv
    args.pop(0)
    prompt_text = " ".join(args)
    response = main(prompt_text)
    print(response["choices"][0]["text"].replace("\n"," "))

