import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Support Assistant Agent", layout="centered")

# --- UI Header ---
st.title("💁‍♂️ AI Support Assistant Agent")
st.write("Ask me any common **technical, general, or customer support-related** question!")

# --- User Input ---
user_query = st.text_input("💡 Type your question here:")

# --- AI Response Function ---
def get_ai_response(user_query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI support assistant."},
                {"role": "user", "content": user_query},
            ]
        )
        return response.choices[0].message.content

    except Exception:
        # Custom fallback answers (local logic)
        fallback_responses = {
            "refund": "Refunds are available within 7 days of purchase with a valid receipt.",
            "password": "To reset your password, click on 'Forgot Password' at the login screen.",
            "contact": "You can reach support at support@example.com.",
            "time": "Our support hours are 9 AM to 6 PM, Monday to Saturday.",
            "mongodb": "MongoDB is a NoSQL database that stores data in JSON-like documents.",
            "passport": "A passport is an official document issued by the government allowing citizens to travel internationally.",
        }

        for keyword, answer in fallback_responses.items():
            if keyword in user_query.lower():
                return answer

        return (
            "⚠️ Live AI unavailable (No valid API access). Here is a sample answer:\n\n"
            f"**Q:** {user_query}\n"
            "I am a basic AI Support Assistant prototype. I can help with:\n"
            "✔ Refund policy ✔ Password help ✔ Contact info ✔ Support timings\n\n"
            "For advanced answers, AI will be enabled with full API integration."
        )

# --- Display Answer ---
if st.button("Get Answer"):
    if user_query.strip():
        answer = get_ai_response(user_query)
        st.markdown("### 🧠 Agent Response:")
        st.write(answer)
    else:
        st.warning("❗ Please type a question first.")

st.write("---")
st.caption("🚀 Prototype version | Built using Python, Streamlit, and OpenAI API")
