import streamlit as st
import requests
from chatbot_ui.core.config import config


def api_call(method, url, **kwargs): 
   
    def _show_error_popup(message: str):
        """Show error message as a popup in the top-right corner of the screen"""
        st.session_state["error_popup"] = {
            "visible": True,
            "message": message,
        }
    
    try:
        response = getattr(requests, method)(url, **kwargs)

        try:
            response_data = response.json()
        except requests.exceptions.JSONDecodeError:
            response_data = {"message": "Invalid JSON response format from server"}
        
        if response.ok:
            return True, response_data
        
        return False, response_data

    except requests.exceptions.ConnectionError:
        _show_error_popup(f"Connection error. Please check your internet connection and try again.")
        return False, {"message": "Connection error"}
    except requests.exceptions.Timeout:
        _show_error_popup(f"Request timed out. Please try again later.")
        return False, {"message": "Request timed out"}
    except Exception as e:
        _show_error_popup(f"An unexpected error occurred: {str(e)}")
        return False, {"message": str(e)}


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
        output = api_call("post", f"{config.API_URL}/rag", json={"query": prompt})
        reponse_data = output[1]
        answer = reponse_data["answer"]
        st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})