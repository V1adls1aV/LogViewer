import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
from app.dataflow.parsing import LogFileParser

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

if "log_format" not in st.session_state:
    st.session_state.log_format = None

if "file" not in st.session_state:
    st.session_state.file = None

st.bar_chart(st.session_state.data)

button1, button2 = st.columns(2)
with st.container():
    file = button1.file_uploader(label="Upload log file")
    if file is not None:
        st.session_state.file = file

    log_format = button2.text_input("Log Format")

    if st.session_state.file is not None and st.session_state.logformat is not None:
        try:
            parser = LogFileParser(StringIO(file.getvalue().decode("utf-8")))
            st.session_state.data = parser.parse(st.session_state.log_format)
            st.write(st.session_state.data)
        except:
            st.write('Invalid log format.')
