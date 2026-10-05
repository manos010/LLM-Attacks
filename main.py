import streamlit as st
import os 
from groq import Groq

from modules import university_ctf, prompt_leak_1, prompt_leak_2, prompt_leak_3, direct_prompt_injection_1

from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="OWASP LLM Top 10 | CTF", layout="wide")


API_KEY = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

if "current_module" not in st.session_state:
    st.session_state.current_module = "menu"
if "current_level" not in st.session_state:
    st.session_state.current_level = 1
if "messages" not in st.session_state:
    st.session_state.messages = []

FLAGS = {
    1: "FLAG{DEAN_ACCESS_GRANTED}",
    2: "FLAG{GRADE_MODIFIER_LEAKED}",
    3: "FLAG{MEDICAL_EXCEPTION_ACCEPTED}",
    4: "FLAG{FACULTY_EMAIL_SPOOFED}",
    5: "FLAG{INDIRECT_INJECTION_SUCCESS}"
}

if st.session_state.current_module == "menu":
    st.markdown("""
  <style>
    .lab-overview-title {
        color: #e5e5e5;
        font-size: 1.8rem;
        font-weight: 600;
        text-align: center;
        margin-bottom: 40px;
        font-family: sans-serif;
    }

    .category-title {
        color: #8b5cf6;
        font-size: 1.15rem;
        margin-bottom: 8px;
        margin-top: 25px;
        font-weight: 500;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-left: 3px solid #6d28d9 !important;
        border-top: none !important;
        border-right: none !important;
        border-bottom: none !important;
        background-color: #1c1c1e !important;
        padding: 10px 10px 10px 25px !important;
        border-radius: 2px !important;
    }

    button[kind="primary"] {
        background-color: transparent !important;
        border: none !important;
        color: #8b5cf6 !important;
        padding: 6px 0 !important;
        text-align: left !important;
        justify-content: flex-start !important;
        box-shadow: none !important;
    }
    
    button[kind="primary"] p {
        font-size: 1.05rem !important;
        margin: 0 !important;
        font-weight: 400 !important;
    }
    
    /* Βγάζουμε την υπογράμμιση από το κεντρικό button και την αφήνουμε ΜΟΝΟ στο p */
    button[kind="primary"]:hover {
        color: #a855f7 !important;
        background-color: transparent !important;
        text-decoration: none !important; 
    }

    button[kind="primary"]:hover p {
        text-decoration: underline !important;
        text-underline-offset: 4px; /* Κάνει την υπογράμμιση λίγο πιο όμορφη */
        color: #a855f7 !important;
    }
    
    /* Με το inline-block απομονώνουμε την τελεία ώστε να μην κληρονομεί το underline του p */
    button[kind="primary"] p::before {
        content: "• ";
        color: #a3a3a3;
        margin-right: 12px;
        font-weight: bold;
        display: inline-block;
        text-decoration: none !important; 
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='lab-overview-title'>Prompt Injection</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='category-title'>Direct Prompt Injection</div>", unsafe_allow_html=True)
    with st.container(border=True):
        if st.button("Prompt Leak 1", type="primary", use_container_width=True, key="menu_leak_1"):
            st.session_state.current_module = "prompt_leak_1"
            st.session_state.messages = []
            st.rerun()
        if st.button("Prompt Leak 2", type="primary", use_container_width=True, key="menu_leak_2"):
            st.session_state.current_module = "prompt_leak_2"
            st.session_state.messages = []
            st.rerun()
        if st.button("Prompt Leak 3", type="primary", use_container_width=True, key="menu_leak_3"):
            st.session_state.current_module = "prompt_leak_3"
            st.session_state.messages = []
            st.rerun()
        if st.button("Direct Prompt Injection 1", type="primary", use_container_width=True, key="menu_dir_1"):
            st.session_state.current_module = "direct_prompt_injection_1"
            st.session_state.messages = []
            st.rerun()

    st.markdown("<div class='category-title'>Indirect Prompt Injection</div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Indirect Prompt Injection 1", type="primary", use_container_width=True, key="menu_ind_1")
        st.button("Indirect Prompt Injection 2", type="primary", use_container_width=True, key="menu_ind_2")
        st.button("Indirect Prompt Injection 3", type="primary", use_container_width=True, key="menu_ind_3")
        st.button("Indirect Prompt Injection 4", type="primary", use_container_width=True, key="menu_ind_4")
        st.button("Indirect Prompt Injection 5", type="primary", use_container_width=True, key="menu_ind_5")

    st.markdown("<div class='category-title'>Jailbreaking</div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Jailbreaking 1", type="primary", use_container_width=True, key="menu_jb_1")
        st.button("Jailbreaking 2", type="primary", use_container_width=True, key="menu_jb_2")

    st.markdown("<div class='category-title'>Prompt Injection Defense</div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Prompt Injection Defense 1", type="primary", use_container_width=True, key="menu_def_1")
        st.button("Prompt Injection Defense 2", type="primary", use_container_width=True, key="menu_def_2")
        st.button("Prompt Injection Defense 3", type="primary", use_container_width=True, key="menu_def_3")
        st.button("Prompt Leak 4", type="primary", use_container_width=True, key="menu_leak_4")

    st.write("")
    st.markdown("<div class='category-title'>CTF</div>", unsafe_allow_html=True)
    with st.container(border=True):
        if st.button("University ChatBot CTF", type="primary", use_container_width=True, key="menu_ctf"):
            st.session_state.current_level = 1
            st.session_state.current_module = "LLM01"
            st.session_state.messages = []
            st.rerun()

    st.write("")
    st.write("")
    st.markdown("<div class='lab-overview-title' style='margin-top: 20px;'>LLM Output Attacks</div>", unsafe_allow_html=True)

    st.markdown("<div class='category-title'>Cross-Site Scripting (XSS)</div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Cross-Site Scripting (XSS) 1", type="primary", use_container_width=True, key="menu_xss_1")
        st.button("Cross-Site Scripting (XSS) 2", type="primary", use_container_width=True, key="menu_xss_2")

    st.markdown("<div class='category-title'>SQL Injection</div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.button("SQL Injection 1", type="primary", use_container_width=True, key="menu_sqli_1")
        st.button("SQL Injection 2", type="primary", use_container_width=True, key="menu_sqli_2")
        st.button("SQL Injection 3", type="primary", use_container_width=True, key="menu_sqli_3")

    st.markdown("<div class='category-title'>Code Injection</div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Code Injection 1", type="primary", use_container_width=True, key="menu_ci_1")
        st.button("Code Injection 2", type="primary", use_container_width=True, key="menu_ci_2")

    st.markdown("<div class='category-title'>Function Calling</div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Function Calling 1", type="primary", use_container_width=True, key="menu_fc_1")
        st.button("Function Calling 2", type="primary", use_container_width=True, key="menu_fc_2")
        st.button("Function Calling 3", type="primary", use_container_width=True, key="menu_fc_3")

    st.markdown("<div class='category-title'>Exfiltration Attacks</div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Chat Bot Playground", type="primary", use_container_width=True, key="menu_exf_play")
        st.button("Exfiltration 1", type="primary", use_container_width=True, key="menu_exf_1")
        st.button("Exfiltration 2", type="primary", use_container_width=True, key="menu_exf_2")
        st.button("Exfiltration 3", type="primary", use_container_width=True, key="menu_exf_3")
        st.button("Exfiltration 4", type="primary", use_container_width=True, key="menu_exf_4")

elif st.session_state.current_module == "LLM01":
    university_ctf.run(client)

elif st.session_state.current_module == "prompt_leak_1":
    prompt_leak_1.run(client)

elif st.session_state.current_module == "prompt_leak_2":
    prompt_leak_2.run(client)

elif st.session_state.current_module == "prompt_leak_3":
    prompt_leak_3.run(client)

elif st.session_state.current_module == "direct_prompt_injection_1":
    direct_prompt_injection_1.run(client)