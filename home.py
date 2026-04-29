import streamlit as st
from PIL import Image

# 1. Page Configuration & Global Design
st.set_page_config(
    page_title="Aletheia | UAE MoE SAFE AI",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS for that "High-End Tech" look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2e7d32; color: white; }
    .stTextInput>div>div>input { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Hero Section (Design)
col1, col2 = st.columns([2, 1])
with col1:
    st.title("🛡️ Project Aletheia")
    st.subheader("The Truth in Education: UAE NRI-CBSE Hybrid Engine")
    st.write("Bridging academic rigor with the UAE's Vision 2071 through High-Agency AI.")
with col2:
    # This acts as a placeholder for your logo
    st.info("Aletheia v1.0.4 | Sharjah, UAE")

st.divider()

# 3. Access Control (Login & Verification)
if 'auth_status' not in st.session_state:
    st.session_state.auth_status = "logged_out"

if st.session_state.auth_status == "logged_out":
    st.header("🔐 Secure Access Portal")
    
    # Create Tabs for a clean look
    tab1, tab2 = st.tabs(["Institutional Login", "Emirates ID Verification"])
    
    with tab1:
        st.text_input("School Email (e.g., student@school.ae)")
        st.text_input("Password", type="password")
        if st.button("Enter Aletheia"):
            st.session_state.auth_status = "logged_in"
            st.rerun()

    with tab2:
        st.warning("MoE REQUIREMENT: Identity verification required for High-Agency modules.")
        id_upload = st.file_uploader("Scan Emirates ID", type=['png', 'jpg', 'jpeg'])
        
        if id_upload:
            st.image(id_upload, caption="Identity Document Detected", width=300)
            if st.button("Verify Identity via AI Scanner"):
                with st.spinner("Mada is verifying credentials..."):
                    # This simulates the "Proof of Life" / ID check
                    st.session_state.auth_status = "verified"
                    st.success("Identity Verified. Full Access Granted.")
                    st.rerun()

# 4. Post-Login Landing View
else:
    st.balloons()
    st.success(f"Welcome back, Pragathi. Current Status: **{st.session_state.auth_status.upper()}**")
    st.markdown("""
    ### 🚀 Getting Started
    Use the **Sidebar on the left** to navigate:
    * **🎓 Student Navigator:** Access the Physics/Math Engine and Image Scanner.
    * **🍎 Teacher Dashboard:** Generate MoE-aligned lesson plans and analytics.
    * **👥 Community:** Connect with other NRI students in the Emirates.
    """)
    
    if st.button("Log Out"):
      st.session_state.auth_status = "logged_out"
        st.rerun()
        st.session_state.auth_status = "logged_out"
        st.rerun()
