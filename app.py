import streamlit as st

st.set_page_config(page_title="AI Support Assistant Agent")

st.title("AI Support Assistant Agent")
st.write("I am a simple prototype support agent. Ask me a question related to customer support!")

# Simple rule-based responses (no real AI, but works as a demo)
def get_response(user_query: str) -> str:
    query = user_query.lower()

    if "refund" in query:
        return "Our refund policy allows refunds within 7 days of purchase with a valid receipt."
    elif "password" in query:
        return "You can reset your password by clicking on 'Forgot Password' on the login page."
    elif "contact" in query or "support" in query:
        return "You can contact our support team at support@example.com."
    elif "timing" in query or "time" in query:
        return "Our support center is available from 9 AM to 6 PM, Monday to Saturday."
    elif "hello" in query or "hi" in query:
        return "Hello! How can I help you today?"
    else:
        return (
            "I am a basic prototype AI Support Assistant. "
            "I can help with common questions like refund, password reset, contact details, and timings."
        )

user_input = st.text_input("Type your question here:")

if st.button("Get Answer"):
    if user_input.strip() == "":
        st.warning("Please type a question first.")
    else:
        answer = get_response(user_input)
        st.markdown("### 🧠 Agent Response:")
        st.write(answer)
