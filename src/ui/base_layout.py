import streamlit as st

def style_background_home():

    st.markdown("""
        <style>

        .stApp {
            background: #000000 !important;
        }

        .stApp div[data-testid="stColumn"] {
            background-color: #FFFFFF !important;
            padding: 2.5rem !important;
            border-radius: 5rem !important;
        }

        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>

        .stApp {
            background: #000000 !important;
        }

        </style>
    """, unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');


        /* Hide Streamlit top bar */
        #MainMenu, footer, header {
            visibility: hidden;
        }


        /* Main content */
        .block-container {
            padding-top: 1.5rem !important;
        }


        /* Headings */
        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            color: #FFFFFF !important;
        }


        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;
            color: #FFAB0F !important;
        }


        h3, h4, p {
            font-family: 'Outfit', sans-serif !important;
            color: #FFFFFF !important;
        }


        /* ALL BUTTONS */
        button {
            border-radius: 1.5rem !important;
            background-color: #FFB000 !important;
            color: #000000 !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }


        /* Secondary button */
        button[kind="secondary"] {
            border-radius: 1.5rem !important;
            background-color: #FFB000 !important;
            color: #000000 !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }


        /* Tertiary button */
        button[kind="tertiary"] {
            border-radius: 1.5rem !important;
            background-color: #000000 !important;
            color: #FFFFFF !important;
            padding: 10px 20px !important;
            border: 2px solid #FFB000 !important;
            transition: transform 0.25s ease-in-out !important;
        }


        /* Button hover */
        button:hover {
            transform: scale(1.05);
        }


        /* TEXT INPUT */
        .stTextInput input {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 2px solid #FFB000 !important;
            border-radius: 1rem !important;
        }


        /* Username / password placeholder */
        .stTextInput input::placeholder {
            color: #555555 !important;
            opacity: 1 !important;
        }


        /* Input labels */
        .stTextInput label {
            color: #FFFFFF !important;
            font-family: 'Outfit', sans-serif !important;
        }


        /* Input focus */
        .stTextInput input:focus {
            border: 2px solid #FFB000 !important;
            box-shadow: 0 0 8px #FFB000 !important;
        }
        
        /* Toast text */
        div[data-testid="stToast"] * {
        background-color:#000000 !important;
        color: #FFFFFF !important;
        }

        </style>
    """, unsafe_allow_html=True)