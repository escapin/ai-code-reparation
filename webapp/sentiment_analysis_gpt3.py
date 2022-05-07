import openai


# load OpenAI API Key
with open("./api_key.txt") as f:
    api_key = f.read()
openai.api_key = api_key


def sentiment_anaysis_check(customer_review):
    # read the GPT-3 designed prompt
    with open("./sentiment_analysis_prompt.txt") as f:
        prompt = f.read()

    # predifined colours
    colours = {
        "green": "#00FF00",
        "yellow": "#FFFF00",
        "red": "#FF0000",
        "white": "#FFFFFF",
    }

    if customer_review == None:
        return "No Review to check, silly human. Buzz buzz!", colours["white"]

    prompt = prompt + customer_review + "\nSentiment Analysis Result:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=20,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    sentiment_analysis_result = response["choices"][0]["text"]

    if "VERY POSITIVE" in sentiment_analysis_result:
        return "VERY POSITIVE", colours["green"]
    elif "POSITIVE" in sentiment_analysis_result:
        return "POSITITVE", colours["green"]
    elif "NEUTRAL" in sentiment_analysis_result:
        return "NEUTRAL", colours["yellow"]
    elif "NEGATIVE" in sentiment_analysis_result:
        return "NEGATIVE", colours["red"]
    elif "VERY NEGATIVE" in sentiment_analysis_result:
        return "VERY NEGATIVE", colours["red"]
    else:
        return "UNSURE", colours["white"]
