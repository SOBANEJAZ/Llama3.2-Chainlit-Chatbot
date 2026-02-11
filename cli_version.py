from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client (auto-detects GROQ_API_KEY from environment)
client = Groq()

# Model configuration
MODEL = "llama-3.3-70b-versatile"

# Initialize conversation history
conversation_history = [
    {"role": "system", "content": "You are a famous podcaster, Andrew Huberman."}
]


def chat(user_input: str) -> str:
    """Send a message and stream the response."""
    conversation_history.append({"role": "user", "content": user_input})

    stream = client.chat.completions.create(
        messages=conversation_history,
        model=MODEL,
        stream=True,
    )

    full_response = ""
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content is not None:
            full_response += content
            print(content, end="", flush=True)
    print()  # New line after response

    conversation_history.append({"role": "assistant", "content": full_response})
    return full_response


def view_history() -> None:
    """Display the conversation history."""
    for message in conversation_history:
        print(f"{message['role'].upper()}: {message['content']}\n")


def main() -> None:
    """Main chat loop."""
    print("Chat started (type 'quit' to exit, 'history' to view conversation history)")
    
    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            break
        elif user_input.lower() == "history":
            view_history()
        elif user_input:
            chat(user_input)


if __name__ == "__main__":
    main()
