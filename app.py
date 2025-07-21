import streamlit as st
import pandas as pd

from src.config.config import load_config
from src.constants import LANGUAGE_PROMPTS, SUPPORTED_LANGUAGES
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

# Initialize session state
def init_session_state():
    """Initialize session state variables"""
    if 'language' not in st.session_state:
        st.session_state.language = "English"
    
    if 'df' not in st.session_state:
        st.session_state.df = None
    
    if 'filename' not in st.session_state:
        st.session_state.filename = None
    
    if 'agent_executor' not in st.session_state:
        st.session_state.agent_executor = None
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

# Call initialization
init_session_state()

config = load_config()

with st.sidebar:
    st.title("YANCCA: Yet Another Csv Chatbot Assistant 🌞")
    
    # Language selector with persistence
    current_language_index = SUPPORTED_LANGUAGES.index(st.session_state.language) if st.session_state.language in SUPPORTED_LANGUAGES else 0
    
    language = st.selectbox(
        "🌍 Response Language",
        SUPPORTED_LANGUAGES,
        index=current_language_index,
        key="language_selector"
    )
    
    # Update session state when language changes
    if language != st.session_state.language:
        st.session_state.language = language
        # Reset agent when language changes
        st.session_state.agent_executor = None
        st.rerun()
    
    # Show API key status
    if config.openai_api_key:
        st.success("✅ API Key loaded")
    else:
        st.error("❌ No API Key found")
    
    # Show current file status
    if st.session_state.filename:
        st.info(f"📁 Current file: {st.session_state.filename}")
        if st.button("🗑️ Clear File"):
            st.session_state.df = None
            st.session_state.filename = None
            st.session_state.agent_executor = None
            st.session_state.chat_history = []
            st.rerun()
    
    # Show chat history count
    if st.session_state.chat_history:
        st.info(f"💬 Chat history: {len(st.session_state.chat_history)} messages")
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

# File upload section
st.header("📊 CSV Data Analysis")

uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])

# Handle file upload
if uploaded_file is not None:
    # Check if it's a new file
    if st.session_state.filename != uploaded_file.name:
        try:
            # Load new file
            df = pd.read_csv(uploaded_file)
            
            # Update session state
            st.session_state.df = df
            st.session_state.filename = uploaded_file.name
            st.session_state.agent_executor = None  # Reset agent for new file
            st.session_state.chat_history = []  # Clear chat for new file
            
            st.success(f"✅ Loaded new file: {uploaded_file.name}")
            st.success(f"📊 {len(df)} rows and {len(df.columns)} columns")
            st.rerun()
            
        except Exception as e:
            st.error(f"Error loading file: {e}")

# Work with persisted data
if st.session_state.df is not None:
    df = st.session_state.df
    
    # Show file info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Rows", len(df))
    with col2:
        st.metric("Columns", len(df.columns))
    with col3:
        st.metric("Language", st.session_state.language)
    
    # Show data preview
    with st.expander("🔍 Data Preview", expanded=False):
        st.dataframe(df.head(10))
        st.write("**Column Info:**")
        st.write(df.dtypes.to_frame('Type'))
    
    # Create or use existing agent
    if config.openai_api_key:
        if st.session_state.agent_executor is None:
            try:
                # Get system prompt from constants
                system_prompt = LANGUAGE_PROMPTS.get(st.session_state.language, LANGUAGE_PROMPTS["English"])
                
                llm = ChatOpenAI(
                    api_key=config.openai_api_key,
                    model=config.openai_model,
                    temperature=config.temperature
                )
                
                st.session_state.agent_executor = create_pandas_dataframe_agent(
                    llm,
                    df,
                    agent_type="tool-calling",
                    verbose=True,
                    prefix=system_prompt,
                    allow_dangerous_code=True
                )
                
                st.success(f"🤖 Agent ready! Will respond in {st.session_state.language}")
                
            except Exception as e:
                st.error(f"Error creating agent: {e}")
        
        # Query interface
        if st.session_state.agent_executor:
            st.subheader("💬 Ask Questions About Your Data")
            
            # Sample questions
            with st.expander("💡 Sample Questions"):
                sample_questions = [
                    "What are the basic statistics?",
                    "Show me the first 5 rows",
                    "Are there any missing values?",
                    "What's the correlation between columns?",
                    "Create a summary of the data"
                ]
                
                cols = st.columns(2)
                for i, question in enumerate(sample_questions):
                    col = cols[i % 2]
                    if col.button(question, key=f"sample_{i}"):
                        # Add to chat history and process
                        st.session_state.chat_history.append(("user", question))
                        with st.spinner("Thinking..."):
                            try:
                                response = st.session_state.agent_executor.invoke({"input": question})
                                st.session_state.chat_history.append(("assistant", response['output']))
                                st.rerun()
                            except Exception as e:
                                error_msg = f"Error: {e}"
                                st.session_state.chat_history.append(("assistant", error_msg))
                                st.rerun()
            
            # Query input
            query = st.text_input("Ask a question about your data:", key="user_query")
            
            if st.button("Ask", type="primary") and query:
                # Add to chat history
                st.session_state.chat_history.append(("user", query))
                
                with st.spinner("Thinking..."):
                    try:
                        response = st.session_state.agent_executor.invoke({"input": query})
                        st.session_state.chat_history.append(("assistant", response['output']))
                        st.rerun()
                    except Exception as e:
                        error_msg = f"Error: {e}"
                        st.session_state.chat_history.append(("assistant", error_msg))
                        st.rerun()
            
            # Display chat history
            if st.session_state.chat_history:
                st.subheader("📝 Conversation History")
                
                for i, (role, message) in enumerate(st.session_state.chat_history):
                    if role == "user":
                        st.chat_message("user").write(f"**You:** {message}")
                    else:
                        st.chat_message("assistant").write(f"**Assistant:** {message}")
        
    else:
        st.warning("⚠️ Add your OpenAI API key to use the chatbot")

else:
    st.info("👆 Upload a CSV file to get started")
    
    # Option to load sample data
    if st.button("📊 Load Sample Data"):
        sample_data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=50),
            'Product': ['Product A', 'Product B', 'Product C'] * 16 + ['Product A', 'Product B'],
            'Sales': pd.np.random.randint(100, 1000, 50),
            'Region': ['North', 'South', 'East', 'West'] * 12 + ['North', 'South'],
            'Rating': pd.np.random.uniform(1, 5, 50)
        })
        
        st.session_state.df = sample_data
        st.session_state.filename = "sample_data.csv"
        st.session_state.agent_executor = None
        st.session_state.chat_history = []
        st.rerun()