import streamlit as st
from io import StringIO
from app.dataflow.parsing import LogFileParser
from app.visualizations.load_hist import HistOfLoad
from app.core import config

st.set_page_config(layout='wide', page_title='LogViewer')

if "data" not in st.session_state:
    st.session_state.data = None

if "log_format" not in st.session_state:
    st.session_state.log_format = ''

if "datetime_format" not in st.session_state:
    st.session_state.datetime_format = ''

if "file" not in st.session_state:
    st.session_state.file = None

graph = st.container()
settings = st.expander('Settings', expanded=True)
data = st.container()

with settings:
    col1, col2 = st.columns(2)

    file = col1.file_uploader(label="Upload log-file")
    if file is not None:
        st.session_state.file = file

    log_format = col2.text_input("Log Format")
    if log_format != '':
        st.session_state.log_format = log_format

    datetime_format = col2.text_input("Datetime Format")
    if datetime_format != '':
        st.session_state.datetime_format = datetime_format

if st.session_state.file is not None and st.session_state.log_format != '':
    try:
        parser = LogFileParser(StringIO(st.session_state.file.getvalue().decode(config.ENCODING)))
        st.session_state.data = parser.parse(st.session_state.log_format)
    except:
        st.write('Invalid log format.')

with graph:
    if st.session_state.data is not None and st.session_state.datetime_format != '':
        try:
            plotter = HistOfLoad(st.session_state.data, st.session_state.datetime_format)
            st.area_chart(
                plotter.plot(segment_count=st.session_state.get(
                    'segment_count', config.SEGMENT_COUNT)), color='#FF4B4B')

            st.select_slider(
                "Statistics step",
                options=list(range(2, 15)) + list(range(15, 101, 5)),
                value=config.SEGMENT_COUNT,
                key='segment_count'
            )
        except:
            st.write('Settings do not fit the file. Please change them.')


with data:
    if st.session_state.data is not None:
        st.dataframe(st.session_state.data, use_container_width=True)

