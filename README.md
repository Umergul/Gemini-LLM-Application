# Gemini LLM Application

A Streamlit web app that answers user questions using Google's Gemini model \u2014 a minimal, readable example of wiring an LLM into a Python web UI.

## What It Does

Type a question, hit **Get Response**, and the app sends it to Gemini and renders the answer.

## Tech Stack

| Component | Purpose |
|---|---|
| Streamlit | Web UI |
| google-genai | Gemini API client |
| python-dotenv | API key management via `.env` |

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Get a free Gemini API key from Google AI Studio (https://aistudio.google.com/)
3. Copy the example env file and add your key:
   ```bash
   cp .env.example .env
   ```
   then set `GOOGLE_API_KEY=your_key_here` inside `.env`
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Files

| File | Description |
|---|---|
| `app.py` | Streamlit app \u2014 question input, Gemini call, answer display |
| `requirements.txt` | Python dependencies |
| `.env.example` | Template for the API key (never commit a real `.env`) |
| `LICENSE` | MIT license |
| `README.md` | This documentation |

## Notes

- The API key stays in `.env`, which is git-ignored \u2014 no secrets in the repo.
- Default model: `gemini-2.0-flash` (fast, free-tier friendly).

## License

MIT \u2014 free to use, adapt, and extend.
