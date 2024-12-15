import streamlit as st
import pandas as pd
import numpy as np

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.sidebar.success("Select a demo above.")

st.bar_chart(st.session_state.data)
button1, button2 = st.columns(2)
with st.container():
    file = button1.file_uploader(label="Upload log file")
    if file is not None:
        st.session_state.data = LogFileParser(StringIO(file.getvalue().decode("utf-8")))
        st.write(parser.parse('{Data} --- {Message}'))
    text = button2.text_input("Log Format")




