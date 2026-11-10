"""Chat completion through FastAIToken with the official OpenAI SDK.

    pip install openai
    export FASTAITOKEN_API_KEY=sk-...
    export FASTAITOKEN_BASE_URL=...   # copy from the FastAIToken console
    python examples/python/chat.py "你好"
"""
import os
import sys

from openai import OpenAI


def main() -> None:
    key = os.environ.get("FASTAITOKEN_API_KEY")
    base_url = os.environ.get("FASTAITOKEN_BASE_URL")
    if not key or not base_url:
        sys.exit("Set FASTAITOKEN_API_KEY and FASTAITOKEN_BASE_URL (see the FastAIToken console).")

    client = OpenAI(api_key=key, base_url=base_url)
    model = os.environ.get("FASTAITOKEN_MODEL", "gpt-5.5")
    prompt = " ".join(sys.argv[1:]) or "Hello!"

    stream = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()


if __name__ == "__main__":
    main()
