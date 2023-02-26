import streamlit as st
import os 
import subprocess


if st.button('Run'):
#     list_dir = subprocess.Popen(["heartwave"])
    subprocess.run([f"{sys.executable}", "heartwave"])
else: print('Thanks')

