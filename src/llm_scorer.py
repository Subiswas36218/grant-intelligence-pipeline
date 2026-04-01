from openai import OpenAI
import os
from dotenv import load_dotenv

# Optional: for Streamlit deployment
try:
    import streamlit as st
except ImportError:
    st = None

# Load environment variables
load_dotenv()

# Get API key (local .env OR Streamlit secrets)
api_key = os.getenv("OPENAI_API_KEY")

if not api_key and st is not None:
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
    except:
        pass

# Initialize client safely
client = OpenAI(api_key=api_key) if api_key else None


def llm_score(grant):
    """
    LLM-based semantic scoring (0–1)
    Safe fallback if API fails or not available
    """

    # 🔒 Fallback if no API key
    if not client:
        print("⚠️ No API key found. Using fallback score.")
        return 0.5

    prompt = f"""
    Evaluate this grant for relevance to a Data Engineering / AI student.

    Title: {grant.get('title')}
    Description: {grant.get('description')}
    Funding: {grant.get('funding')}

    Respond ONLY with a number between 0 and 1 (e.g., 0.85).
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        output = response.choices[0].message.content.strip()

        # Debug (useful during development)
        print("LLM OUTPUT:", output)

        return float(output)

    except Exception as e:
        print("❌ LLM ERROR:", e)
        return 0.5