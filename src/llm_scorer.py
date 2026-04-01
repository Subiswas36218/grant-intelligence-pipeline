from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def llm_score(grant):
    """
    Uses LLM to score grant relevance (0 to 1).
    Falls back safely if any error occurs.
    """

    # Fallback if API key missing
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️ No API key found. Using fallback score.")
        return 0.5

    prompt = f"""
    Evaluate this grant for relevance to a Data Engineering / AI student.

    Title: {grant.get('title')}
    Description: {grant.get('description')}
    Funding: {grant.get('funding')}

    Return ONLY a number between 0 and 1.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # safer + available model
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        output = response.choices[0].message.content.strip()

        # Debug print (VERY useful)
        print("LLM OUTPUT:", output)

        return float(output)

    except Exception as e:
        print("❌ LLM ERROR:", e)
        return 0.5