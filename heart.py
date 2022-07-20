import streamlit as st
import os 
import subprocess


if st.button('Run'):
    list_dir = subprocess.Popen(["heartwave"])
else: print('Thanks')

