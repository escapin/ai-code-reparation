# AI-enhanced Code Reparation and Performances 
Web App which uses the [Codex model series](https://beta.openai.com/docs/engines/codex-series-private-beta) 
to automatically find bugs on your code.

# Dependencies
- python (tested with python3.10)
- pip (tested with 21.2)
- `pip install dash`
- `pip install dash_ace`
- `pip install openai`

# Build and Test
1. Create the file `api_key.txt` in the root directory of this project and put your OpenAI API key from 
   [https://beta.openai.com/account/api-keys](https://beta.openai.com/account/api-keys).

2. Execute `web_app.py` to run the web app on `localhost:8050`