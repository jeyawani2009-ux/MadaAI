import streamlit as st
import google.generativeai as genai

# ... (Previous CSS and Layout code remains the same) ...

# 1. TRACK THE ACTIVE TAB
# Streamlit tabs don't natively return their index easily, so we use a radio or a state tracker.
# For the 'Niche' look, we'll stick to tabs but use a hidden state.

tab_titles = ["🏛️ Profile & Legal", "💡 LearnTeach", "📖 Learning", "📊 Feedback", "🤝 Community", "📥 Requests"]
tabs = st.tabs(tab_titles)

# 2. DEFINE THE BRAIN SWITCHER (Mada's Logic)
def mada_brain(user_query, active_tab):
    if "GEMINI_API_KEY" not in st.secrets:
        return "Please set your API Key in Secrets."
    
    genai.configure(api_key=st.secrets["AIzaSyCt9LuZfPbYrqxOpLvycHpu4F5v0GMDBsE"])
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Context Injection
    contexts = {
        "🏛️ Profile & Legal": "You are a UAE Legal Expert. Advise on MoHRE permits and TLS certifications.",
        "💡 LearnTeach": "You are a Pedagogical Architect. Help design Socratic lessons and high-leverage teaching methods.",
        "📊 Feedback": "You are a Data Analyst. Help the teacher solve specific student friction points and learning gaps.",
        "📖 Learning": "You are a Mirror Guide. Explain how students are interacting with the current module.",
        "🤝 Community": "You are a Networking Liaison. Help connect this teacher with Scholars and peer educators.",
        "📥 Requests": "You are a Conflict-of-Interest Shield. Ensure all private sessions are legally compliant."
    }
    
    system_prompt = contexts.get(active_tab, "You are Mada, a professional teaching co-pilot.")
    full_prompt = f"System: {system_prompt}\nUser: {user_query}"
    
    response = model.generate_content(full_prompt)
    return response.text

# --- 3. THE 6-COLUMN CONTENT (Simplified for this example) ---
# Each tab block here...
with tabs[0]:
    st.session_state.current_tab = "🏛️ Profile & Legal"
    # (Your Profile UI Code)
with tabs[1]:
    st.session_state.current_tab = "💡 LearnTeach"
    # (Your LearnTeach UI Code)
# ... repeat for all tabs ...

# --- 4. THE CONTEXT-AWARE CHATBAR ---
with st.sidebar:
    st.title("🛡️ Mada AI")
    st.caption(f"Currently assisting with: {st.session_state.get('current_tab', 'General')}")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("How can I help you in this section?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # Mada's brain switches here!
        answer = mada_brain(prompt, st.session_state.current_tab)
        
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)
