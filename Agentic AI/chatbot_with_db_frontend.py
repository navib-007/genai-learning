import streamlit as st
from chatbot_with_db_backend import chatbot, retrieve_all_threads
from langchain_core.messages import HumanMessage
import uuid

# **************************************** utility functions *************************

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'], label="New Chat")
    st.session_state['message_history'] = []

def add_thread(thread_id, label="New Chat"):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)
        st.session_state['thread_labels'][thread_id] = label

def load_conversation(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    return state.values.get('messages', [])


# **************************************** Session Setup ******************************
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()

if 'thread_labels' not in st.session_state:
    st.session_state['thread_labels'] = {}

# Populate missing thread labels from DB
for tid in st.session_state['chat_threads']:
    if tid not in st.session_state['thread_labels']:
        messages = load_conversation(tid)
        if messages:
            first_human_msg = next((m for m in messages if isinstance(m, HumanMessage)), None)
            if first_human_msg:
                label = first_human_msg.content[:30] + "..." if len(first_human_msg.content) > 30 else first_human_msg.content
            else:
                pass
            st.session_state['thread_labels'][tid] = label

add_thread(st.session_state['thread_id'])


# **************************************** Sidebar UI *********************************

st.sidebar.title('LangGraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My Conversations')

for thread_id in st.session_state['chat_threads'][::-1]:
    label = st.session_state['thread_labels'].get(thread_id, str(thread_id))
    if st.sidebar.button(label, key=thread_id):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)

        temp_messages = []

        for msg in messages:
            role = 'user' if isinstance(msg, HumanMessage) else 'assistant'
            temp_messages.append({'role': role, 'content': msg.content})

        st.session_state['message_history'] = temp_messages


# **************************************** Main UI ************************************

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type here')

if user_input:
    # Save the message
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})

    # If it's the first user message, use it as the thread label
    if len(st.session_state['message_history']) == 1:
        st.session_state['thread_labels'][st.session_state['thread_id']] = user_input[:30] + "..." if len(user_input) > 30 else user_input
    
    with st.chat_message('user'):
        st.text(user_input)

    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

    # first add the message to message_history
    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= CONFIG,
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})