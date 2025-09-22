from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="meta/llama3-8b-instruct",
  messages=[{"role":"user","content":"what is machine learning "}],
  temperature=0.5,
  top_p=1,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")