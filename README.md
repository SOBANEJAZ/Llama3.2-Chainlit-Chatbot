# Chatbot with Llama 3.3 and Chainlit

A chatbot using the Llama 3.3 model through the Groq API with a Chainlit web interface.

![Demo](Animation.gif)

## Setup

### 1. API Key

1. Get an API key from [Groq Console](https://console.groq.com/keys)
2. Copy `.env.example` to `.env`
3. Add your key: `GROQ_API_KEY=your_key_here`

### 2. Install Dependencies

```bash
uv sync
```

### 3. Run

**Chainlit UI:**
```bash
uv run chainlit run app.py -w
```

**CLI Version:**
```bash
uv run python cli_version.py
```

## Features

- **Model**: `llama-3.3-70b-versatile` (128K context window)
- **Streaming**: Responses stream in real time
- **Memory**: Maintains conversation history per session
- **Persona**: Responds as Dr. Andrew Huberman

## Contributing

Fork the repository and submit pull requests. Open an issue first for significant changes.
