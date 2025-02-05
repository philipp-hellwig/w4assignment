import streamlit as st
import pandas as pd
import numpy as np

spells = pd.read_csv("https://raw.githubusercontent.com/philipp-hellwig/w4assignment/refs/heads/main/Spells.csv")

st.set_page_config(page_title="Harry's Spell Book")

def generate_spell():
    random_id = np.random.choice(spells.shape[0])
    st.header(f'{spells.loc[random_id, "Incantation"]} ({spells.loc[random_id, "Spell Name"]})')
    st.markdown(f':magic_wand::dizzy: *{spells.loc[random_id, "Effect"]}*')
    st.header(":point_up: You're a wizard, Harry :eye::lips::eye:")

st.button("Generate random spell", on_click=generate_spell)