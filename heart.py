import av
import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import AudioProcessorBase,RTCConfiguration,VideoProcessorBase,WebRtcMode,webrtc_streamer
from aiortc.contrib.media import MediaPlayer
import os 
import subprocess


if st.button('Run'):
    list_dir = subprocess.Popen(["heartwave"])
else: print('Thanks')

