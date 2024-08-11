import google.generativeai as genai
import streamlit as st
google_api_key= "AIzaSyClsqKASJFmO2u9dsL7Ni_w4ZEzno7vQ94"

genai.configure(api_key=google_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
def getresponsefrommodel(user_input):
    response=model.generate_content(user_input)
    return response.text
#.git/MERGE_MSG [unix] (04:42 11/08/2024)        6,12 Bot
st.title("😀simple chatbot😀")
st.write("gemini api")
if "histroy" not in st.session_state:
    st.session_state["histroy"]=[] 

#user_input=input("enter your message=")
#output=getresponsefrommodel(user_input)
#print(output)
with st.form(key="chat_form", clear_on_submit=True):
    user_input=st.text_input("",max_chars=2000)
    submit_button=st.form_submit_button("Send")
    if submit_button:
        if user_input:
            response=getresponsefrommodel(user_input) 
            st.write(response)
            st.session_state.histroy.append((user_input,response))
        else: 
            st.warning("please enter a Prompt")
    