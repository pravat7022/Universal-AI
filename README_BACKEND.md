# Universal AI backend

Render settings:
- Runtime: Docker
- Branch: main
- Root Directory: leave blank
- Dockerfile Path: ./Dockerfile
- Compute: Free, if available

After deployment, open Render > your service > Environment and add:
- OPENAI_API_KEY = your secret API key (enter it only in Render; never share it or commit it to GitHub)
- Optional OPENAI_MODEL = gpt-4.1-mini

Endpoints:
- GET / checks whether the backend is running.
- POST /chat accepts {"message":"Hello"} and returns {"reply":"..."}.

Important: this is a minimal learning backend, not production-ready. It does not yet have user authentication, rate limiting, usage limits, saved chat history, or a restricted CORS allowlist. OpenAI API usage may cost money. Keep the API key only in Render environment variables.
