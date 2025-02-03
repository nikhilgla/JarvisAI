from openai import OpenAI

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
      {"role": "system", "content": "You are a helpful virtual assistant named Jarvis."},
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
