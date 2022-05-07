import openai


# load OpenAI API Key
with open("./api_key.txt") as f:
    api_key = f.read()
openai.api_key = api_key

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Tell me something nice.",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

print(response["choices"][0]["text"])
