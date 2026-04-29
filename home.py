import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Aletheia | Ecosystem", layout="wide")

# 2. Advanced CSS for Scrolling & Interactions
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #008080 0%, #1e3a8a 50%, #0f172a 100%);
        color: #f0fdfa;
    }
    
    /* Hero Section */
    .hero {
        height: 80vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    /* Floating Feature Cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 30px;
        margin: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease, border 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-10px);
        border: 1px solid #14b8a6;
        background: rgba(255, 255, 255, 0.1);
    }

    /* Section Headers */
    .section-header {
        color: #5eead4;
        font-size: 2.5rem;
        font-weight: bold;
        margin-top: 100px;
        text-align: center;
    }

    /* Price/Package Tags */
    .package-tag {
        background: #ff7f50;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SECTION 1: HERO & LOGIN ---
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.title("🛡️ Project Aletheia")
st.write("Scroll to explore the high-agency ecosystem.")
st.markdown('</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 20px;">', unsafe_allow_html=True)
    st.subheader("Secure Entry")
    st.text_input("Email")
    st.text_input("Password", type="password")
    if st.button("Enter Portal"):
        st.success("Welcome back, Pragathi.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 2: THE FEATURES (The Scrollable Part) ---
st.markdown('<div class="section-header">The Aletheia Suite</div>', unsafe_allow_html=True)

f_col1, f_col2, f_col3 = st.columns(3)

with f_col1:
    st.markdown("""
    <div class="feature-card">
        <div class="package-tag">CORE ENGINE</div>
        <h3>Mada AI</h3>
        <p>[INSERT DESCRIPTION: e.g., Your Socratic physics navigator that bridges the gap between CBSE and reality.]</p>
    </div>
    """, unsafe_allow_html=True)

with f_col2:
    st.markdown("""
    <div class="feature-card">
        <div class="package-tag">RESEARCH</div>
        <h3>Perplexity Lens</h3>
        <p>[INSERT DESCRIPTION: e.g., Real-time verified data with 2026 citations for high-fidelity scholarship.]</p>
    </div>
    """, unsafe_allow_html=True)

with f_col3:
    st.markdown("""
    <div class="feature-card">
        <div class="package-tag">VISION</div>
        <h3>Smart Scanner</h3>
        <p>[INSERT DESCRIPTION: e.g., Instant OCR and image identification for complex mathematical diagrams.]</p>
    </div>
    """, unsafe_allow_html=True)

# --- SECTION 3: INTERACTIVE QUOTES ---
st.markdown('<div class="section-header">Words of Vision</div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align: center; padding: 50px; font-style: italic; color: #ccfbf1; font-size: 1.5rem;">
    " [INSERT A POWERFUL UAE VISION 2071 QUOTE HERE] "
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br><br><p style='text-align: center; opacity: 0.5;'>End of Page | Sharjah, UAE</p>", unsafe_allow_html=True)
