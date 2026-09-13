import streamlit as st


# ============================================================
# HOME PAGE BACKGROUND
# ============================================================

def style_background_home():

    st.markdown("""
    <style>

    /* Main home background */
    .stApp {
        background: #5865F2 !important;
    }

    /* Student / Teacher cards */
    div[data-testid="stColumn"] {
        background-color: #E0E3FF !important;
        padding: 2.5rem !important;
        border-radius: 5rem !important;
    }

    /* Card text BLACK */
    div[data-testid="stColumn"] h1,
    div[data-testid="stColumn"] h2,
    div[data-testid="stColumn"] h3,
    div[data-testid="stColumn"] h4,
    div[data-testid="stColumn"] p,
    div[data-testid="stColumn"] span {
        color: #000000 !important;
    }

    </style>
    """, unsafe_allow_html=True)


# ============================================================
# DASHBOARD BACKGROUND
# ============================================================

def style_background_dashboard():

    st.markdown("""
    <style>

    .stApp {
        background: #E0E3FF !important;
    }

    </style>
    """, unsafe_allow_html=True)


# ============================================================
# COMMON / BASE STYLE
# ============================================================

def style_base_layout():

    st.markdown("""
    <style>

    /* ========================================================
       FONTS
    ======================================================== */

    @import url(
        'https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap'
    );

    @import url(
        'https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap'
    );


    /* ========================================================
       HIDE STREAMLIT DEFAULT UI
    ======================================================== */

    #MainMenu,
    footer,
    header {
        visibility: hidden;
    }


    /* ========================================================
       MAIN CONTAINER
    ======================================================== */

    .block-container {
        padding-top: 1.5rem !important;
    }


    /* ========================================================
       HEADINGS
    ======================================================== */

    h1 {
        font-family: 'Climate Crisis', sans-serif !important;
        font-size: 3.5rem !important;
        line-height: 1.1 !important;
        margin-bottom: 0rem !important;
        color: #000000 !important;
    }

    h2 {
        font-family: 'Climate Crisis', sans-serif !important;
        font-size: 2rem !important;
        line-height: 0.9 !important;
        margin-bottom: 0rem !important;
        color: #000000 !important;
    }

    h3,
    h4 {
        font-family: 'Outfit', sans-serif !important;
        color: #000000 !important;
    }


    /* ========================================================
       NORMAL TEXT
    ======================================================== */

    p {
        font-family: 'Outfit', sans-serif !important;
        color: #000000 !important;
    }

    label {
        font-family: 'Outfit', sans-serif !important;
        color: #000000 !important;
    }


    /* ========================================================
       GENERAL BUTTON
    ======================================================== */

    button {
        font-family: 'Outfit', sans-serif !important;
        border-radius: 1.5rem !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
    }


    /* ========================================================
       BLUE BUTTON
    ======================================================== */

    button[kind="primary"] {
        background-color: #5865F2 !important;
        color: #000000 !important;
    }

    button[kind="primary"] span,
    button[kind="primary"] p,
    button[kind="primary"] div {
        color: #000000 !important;
    }


    /* ========================================================
       PINK BUTTON
    ======================================================== */

    button[kind="secondary"] {
        background-color: #EB459E !important;
        color: #000000 !important;
    }

    button[kind="secondary"] span,
    button[kind="secondary"] p,
    button[kind="secondary"] div {
        color: #000000 !important;
    }


    /* ========================================================
       BLACK BUTTON
    ======================================================== */

    button[kind="tertiary"] {
        background-color: #000000 !important;
        color: #FFFFFF !important;
    }

    button[kind="tertiary"] span,
    button[kind="tertiary"] p,
    button[kind="tertiary"] div {
        color: #FFFFFF !important;
    }


    /* ========================================================
       BUTTON HOVER
    ======================================================== */

    button:hover {
        transform: scale(1.05) !important;
    }


    /* ========================================================
       SUBJECT CARD BUTTONS
       Example:
       👥 1 Students
       🧑‍🏫 1 Classes
    ======================================================== */

    div[data-testid="stButton"] button {
        color: #000000 !important;
    }

    div[data-testid="stButton"] button span,
    div[data-testid="stButton"] button p,
    div[data-testid="stButton"] button div {
        color: #000000 !important;
    }


    /* ========================================================
       INPUT / SELECTBOX
    ======================================================== */

    input,
    textarea {
        font-family: 'Outfit', sans-serif !important;
        color: #000000 !important;
    }


    /* Selectbox text */
    div[data-baseweb="select"] {
        font-family: 'Outfit', sans-serif !important;
    }

    div[data-baseweb="select"] * {
        color: #000000 !important;
    }


    /* ========================================================
       IMAGES
    ======================================================== */

    img {
        border-radius: 1rem;
    }


    /* ========================================================
       DIVIDERS
    ======================================================== */

    hr {
        border-color: rgba(0, 0, 0, 0.15) !important;
    }


    /* ========================================================
       LINKS
    ======================================================== */

    a {
        color: #5865F2 !important;
        font-family: 'Outfit', sans-serif !important;
    }


    /* ========================================================
       EXPANDER
    ======================================================== */

    div[data-testid="stExpander"] {
        border-radius: 1.5rem !important;
        border: 1px solid #000000 !important;
    }


    /* ========================================================
       CHECKBOX
    ======================================================== */

    div[data-testid="stCheckbox"] label {
        color: #000000 !important;
        font-family: 'Outfit', sans-serif !important;
    }


    /* ========================================================
       RADIO BUTTON
    ======================================================== */

    div[data-testid="stRadio"] label {
        color: #000000 !important;
        font-family: 'Outfit', sans-serif !important;
    }


    </style>
    """, unsafe_allow_html=True)