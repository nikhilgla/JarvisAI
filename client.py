from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
      {"role": "system", "content": "You are a helpful virtual assistant named Jarvis."},
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
