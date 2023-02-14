import streamlit as st

custom_css_properties = """
                    <style>
                    # MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """

st.set_page_config(
    page_title="Screen Sailor",
    page_icon=":boat:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(custom_css_properties, unsafe_allow_html=True)
