import os
import openai
import prompts

from dotenv import load_dotenv, find_dotenv
from functools import partial

# load the .env file
load_dotenv()
client = openai.OpenAI()

# Set parameters for the model.
model = "gpt-4o-mini"
temperature = 0.3
max_tokens = 500

def send_question(question: str):
  
  completion = client.chat.completions.create(
    model=model,
    messages=[
      {"role": "system", "content": prompts.system_message},
      {"role": "user", "content": question}
    ],
    temperature=temperature,
    max_tokens = max_tokens
  )

  return completion.choices[0].message.content 


def retrieve_characters(script: str):
  question = prompts.generate_character_prompt(script)
  return send_question(question)

def retrieve_lines(script: str):
  question = prompts.generate_lines_prompt(script)
  return send_question(question)