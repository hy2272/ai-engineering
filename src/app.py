import streamlit as st
from openai import OpenAI
from google import genai
from groq import Groq
from core.config import config

def run_llm(provider: str, model_name: str, messages: list[dict],max_tokens: int = 500):
    
    if provider == "OpenAI":
        client = OpenAI(api_key=config.OPENAI_API_KEY)
    elif provider == "Groq":
        client = Groq(api_key=config.GROQ_API_KEY)
    else:
        client = genai.Client(api_key=config.GOOGLE_API_KEY)

    if provider == "Google":
        return client.models.generate_content(
            model=model_name, 
            contents=[message["content"] for message in messages],
            ).text
    elif provider == "Groq":
        return client.chat.completions.create(
            model=model_name,
            messages=messages,
            max_completion_tokens=max_tokens,
        ).choices[0].message.content
    else:
        return client.chat.completions.create(
            model=model_name,
            messages=messages,
            max_completion_tokens=max_tokens,
            reasoning_effort="minimal"
        ).choices[0].message.content

#lets create a sidebar with a dropdown for the model list and provider
with st.sidebar:
    st.title("Settings")

    #dropdown for model
    provider = st.selectbox("Provider", ["OpenAI", "Groq", "Google"])
    if provider == "OpenAI":
        model_name = st.selectbox("Model", ["gpt-5-nano", "gpt-5-mini"])
    elif provider == "Groq":
        model_name = st.selectbox("Model", ["llama-3.3-70b-versatile"])
    else: #Google
        model_name = st.selectbox("Model", ["gemini-2.5-flash"])

    #save provider and model name to session state
    st.session_state.provider = provider
    st.session_state.model_name = model_name

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! how can I assist you today?"}]

#display the messages in the chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Hello! How can I assist you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        output = run_llm(st.session_state.provider, st.session_state.model_name, st.session_state.messages)
        reponse_data = output
        answer = reponse_data
        st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
