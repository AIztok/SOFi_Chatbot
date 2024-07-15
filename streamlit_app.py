import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext, Document, Settings
from llama_index.llms.openai import OpenAI
import openai
from llama_index.core.memory import ChatMemoryBuffer # for the context chat engine

st.set_page_config(
    page_title="Chat with a SOFiSTiK database of Teddy/Cadinp files, powered by LlamaIndex",
    page_icon="🦙",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

openai.api_key = st.secrets.openai_key
st.title("Chat with a SOFiSTiK database of Teddy/Cadinp files, powered by LlamaIndex 💬🦙")
st.info(
    "The database consists of authors' examples and examples prepared by SOFiSTiK. For more information on the Software visit [Sofistik.de](https://www.sofistik.de/)", 
    icon="📃"
)

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about SOFiSTiK Teddy/Cadinp Input!"}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the database – hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        Settings.llm = OpenAI(
            model="gpt-4", 
            temperature=0.1, 
            system_prompt="""You are an expert on the sofistik structural design, finite element method software and its teddy, cadinp language and your job is to answer technical questions. Assume that all questions are related to the finite element analysis using the sofistik teddy programming language. Keep your answers technical and based on facts – do not hallucinate features."""
        )
        index = VectorStoreIndex.from_documents(docs)
        return index

index = load_data()

#memory = ChatMemoryBuffer.from_defaults(token_limit=500)

#chat_engine = index.as_chat_engine(chat_mode="context", verbose=True, memory=memory)

if "chat_engine" not in st.session_state.keys():  # Initialize the chat engine
    st.session_state.chat_engine = index.as_chat_engine(
        chat_mode="condense_question", verbose=True, streaming=True
    )

if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # write message history in user interface
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
#            response = chat_engine.chat(st.session_state.messages[-1]["content"])
#            st.write(response)
#            st.session_state.messages.append({"role": "assistant", "content": response})
        response_stream = st.session_state.chat_engine.stream_chat(prompt)
        st.write_stream(response_stream.response_gen)
        message = {"role": "assistant", "content": response_stream.response}
        # Add response to message history
        st.session_state.messages.append(message)
