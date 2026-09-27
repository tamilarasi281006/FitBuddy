import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()
MODEL_NAME = "gemini-3.8-flash"

async def generate_nutrition_tip(goal):
    prompt = f"Give one short, practical nutrition or recovery tip for someone whose fitness goal is '{goal}'. Keep it friendly and easy to understand."
    try:
        interaction = await client.aio.interactions.create(
            model=MODEL_NAME,
            input=prompt
        )
        return interaction.output_text.strip()
    except Exception as e:
        return f"API Error: {str(e)}"