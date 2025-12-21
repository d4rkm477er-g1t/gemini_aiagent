import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("no api key present")

def main():

    model = "gemini-2.5-flash"

    client = genai.Client(api_key=api_key)

   
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="This is the user prompt. The user is the one you should do your best to aid.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbos output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


    response = client.models.generate_content(model=model, contents=messages)

    if response.usage_metadata != None:
        if args.verbose:
            print("User prompt:" + str(args.user_prompt))
            print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
            print("Response tokens: " + str(response.usage_metadata.candidates_token_count))
        print(response.text)
    else:
        raise RuntimeError("Could not connect with Google API")


if __name__ == "__main__":
    main()
