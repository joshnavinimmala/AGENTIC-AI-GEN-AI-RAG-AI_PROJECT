import streamlit as st
from nltk.chat.util import Chat, reflections

# Page configuration
st.set_page_config(
    page_title="Joshnavi's Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Chatbot patterns and responses
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, how are you today?"]
    ],
    [
        r"(.*)help(.*)",
        ["I can help you. What do you need?"]
    ],
    [
        r"(.*)your name(.*)",
        ["My name is Joshnavi's Chatbot. You can call me Robot!"]
    ],
    [
        r"how are you(.*)",
        ["I'm doing very well!", "I am great!"]
    ],
    [
        r"sorry(.*)",
        ["It's alright.", "It's okay, never mind."]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello!", "Hey there!"]
    ],
    [
        r"(.*)created(.*)",
        ["I was created using Python's NLTK library."]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a big fan of cricket!"]
    ],
    [
        r"(.*)(cricketer|batsman|cricket)(.*)",
        ["Virat Kohli is a famous Indian cricketer."]
    ],
    [
        r"quit",
        ["Goodbye! See you soon."]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you explain more?"]
    ]
]

# Create chatbot
chat = Chat(pairs, reflections)

# Frontend design
st.title("🤖 Joshnavi's Chatbot")
st.caption("A simple Python chatbot powered by NLTK")
st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! 👋 Welcome to my chatbot. How can I help you?"
        }
    ]

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Display user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate chatbot response
    if user_input.strip().lower() == "quit":
        response = "Goodbye! See you soon."
    else:
        response = chat.respond(user_input.lower())

        if response is None:
            response = "Sorry, I couldn't understand that."

    # Display bot response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)

# Sidebar
with st.sidebar:
    st.header("About")
    st.write(
        "This chatbot is built using Python, NLTK and Streamlit."
    )

    st.write("**Features:**")
    st.write("- Pattern matching")
    st.write("- Interactive chat interface")
    st.write("- Chat history during the session")

    if st.button("Clear Chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! 👋 Welcome back. How can I help you?"
            }
        ]
        st.rerun()