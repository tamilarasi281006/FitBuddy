import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()
MODEL_NAME = "gemini-3.8-flash"


async def stream_workout_gemini(goal, intensity):
    """Async generator that streams a 3-day workout plan from Gemini."""
    prompt = f"""You are a professional fitness trainer. Create a personalized 3-day workout plan.
Fitness goal: {goal}
Preferred intensity: {intensity}

For each day include:
- Warm-up (5-10 mins)
- Main workout (exercises with sets and reps)
- Cooldown

Format:
Day 1:
Warm-up: ...
Main Workout: ...
Cooldown: ...
(Repeat for Day 2 and Day 3)

Keep the plan concise and clear."""
    try:
        stream = client.interactions.create(
            model=MODEL_NAME,
            input=prompt,
            stream=True
        )
        for event in stream:
            if event.event_type == "step.delta" and event.delta.type == "text":
                yield event.delta.text
    except Exception as e:
        yield f"API Error: {str(e)}"


async def update_workout_plan(original_plan, feedback):
    """Use Gemini to update the workout plan based on user feedback."""
    prompt = f"""You are a professional fitness trainer.
Here is the original 3-day workout plan:
{original_plan}

The user has given this feedback: "{feedback}"

Revise the plan based on this feedback. Keep the same format (3 days) and change only what's needed."""
    try:
        interaction = client.interactions.create(
            model=MODEL_NAME,
            input=prompt
        )
        return interaction.output_text.strip()
    except Exception as e:
        return f"API Error: {str(e)}"