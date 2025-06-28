import sys
p = ""
if __name__ == "__main__":
    if len(sys.argv) == 2:
        argument = sys.argv[1]
    elif len(sys.argv) == 3:
        argument = sys.argv[1]
        p = sys.argv[2]
    else:
        print("Please provide a question as an argument.")
        sys.exit(1)

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=argument)]),
]

# question = argument

response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents= messages,)
print(response.text)

if p == '--verbose':
    print(f"User prompt: {argument}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")