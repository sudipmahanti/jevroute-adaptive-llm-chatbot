# jevroute-adaptive-llm-chatbot
A simple terminal chatbot that asks Jev to check each prompt before Gemini answers.

## How it works

1. You enter a prompt.
2. Jev returns the probability that it needs coding, reasoning, or careful analysis.
3. If that probability is **greater than 80%**, the chatbot uses `gemini-3.1-pro-preview`.
4. At **80% or below**, it uses the Flash model in `GEMINI_MODEL`.
5. Gemini generates the answer. The terminal shows the probability and selected model.

If Jev times out, returns an error, or sends an invalid result, the chatbot prints
a message and uses Flash. Every new prompt gets a new routing decision.

## Setup

Install the dependencies in your Python environment:

```sh
pip install -r requirements.txt
```

Create a `.env` file in this folder:

```dotenv
GEMINI_API_KEY=your_gemini_key
JEV_API_KEY=your_typesafe_jev_key
GEMINI_MODEL=gemini-3.5-flash-lite
SYSTEM_PROMPT=You are a helpful AI assistant.
```

`JEV_API_KEY` must be a TypeSafe key for the official Jev endpoint.
Keep your actual API keys out of Git.

Run the chatbot:

```sh
python chatbot.py
```

With this project's existing environment, you can also run:

```sh
myenv/bin/python chatbot.py
```

Type `exit` or `stop` to quit. Change `COMPLEXITY_THRESHOLD` in `config.py`
if you want a different cutoff. No additional packages are needed for routing.

Jev's `noul` field represents a probability from 0 to 1;
see the [official API quickstart](https://docs.typesafe.ai/introduction/quickstart).
