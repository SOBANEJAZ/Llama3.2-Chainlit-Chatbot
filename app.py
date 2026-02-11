import chainlit as cl
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client (auto-detects GROQ_API_KEY from environment)
client = Groq()

# Model configuration
MODEL = "llama-3.3-70b-versatile"


@cl.on_chat_start
async def start():
    # Initialize conversation history in user session
    cl.user_session.set(
        "conversation_history",
        [{"role": "system", "content": "You are a famous podcaster, Andrew Huberman."}],
    )

    await cl.Message(
        content="Welcome! I'm Dr. Andrew Huberman, a Professor of Neurobiology at Stanford University and host of the Huberman Lab podcast. I'm here to discuss neuroscience, health optimization, and peak performance. What would you like to know?",
        author="Dr. Andrew Huberman",
    ).send()


@cl.on_message
async def main(message: cl.Message):
    try:
        # Get conversation history from user session
        conversation_history = cl.user_session.get("conversation_history")
        conversation_history.append({"role": "user", "content": message.content})

        # Create message placeholder for streaming
        msg = cl.Message(content="", author="Dr. Andrew Huberman")
        await msg.send()

        # Stream response from Groq
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
                await msg.stream_token(content)

        # Update conversation history
        conversation_history.append({"role": "assistant", "content": full_response})
        cl.user_session.set("conversation_history", conversation_history)

        await msg.update()

    except Exception as e:
        await cl.Message(content=f"An error occurred: {str(e)}", author="Error").send()
