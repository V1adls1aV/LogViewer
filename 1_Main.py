import streamlit as st
from io import StringIO
from app.dataflow.parsing import LogFileParser
from app.visualizations.load_hist import HistOfLoad
from app.core import config


def get_date_format(data):
    need_data = "%" + data[0]
    for i in range(1, len(data)):
        if not data[i].isalpha():
            need_data += data[i] + "%"
        elif data[i] != data[i - 1]:
            need_data += data[i]
    return need_data


if "data" not in st.session_state:
    st.session_state.data = None

if "log_format" not in st.session_state:
    st.session_state.log_format = ''

if "datetime_format" not in st.session_state:
    st.session_state.datetime_format = ''

if "file" not in st.session_state:
    st.session_state.file = None

with st.container():
    col1, col2 = st.columns(2)

    file = col1.file_uploader(label="Upload log-file")
    if file is not None:
        st.session_state.file = file

    st.select_slider("Statistics step",
                     options=list(range(2, 15)) + list(range(15, 101, 5)),
                     value=config.SEGMENT_COUNT,
                     key='segment_count')

    log_format = col2.text_input("Log Format")
    if log_format != '':
        st.session_state.log_format = log_format

    datetime_format = col2.text_input("Datetime Format")
    if datetime_format != '':
        st.session_state.datetime_format = get_date_format(datetime_format)

with st.container():
    if st.session_state.file is not None and st.session_state.log_format != '':
        try:
            parser = LogFileParser(StringIO(file.getvalue().decode(config.ENCODING)))
            st.session_state.data = parser.parse(st.session_state.log_format)
        except:
            st.write('Invalid log format.')

    if st.session_state.data is not None and st.session_state.datetime_format != '':
        plotter = HistOfLoad(st.session_state.data, st.session_state.datetime_format)
        st.area_chart(plotter.plot(segment_count=st.session_state.segment_count), color='#FF4B4B')

    if st.session_state.data is not None:
        st.dataframe(st.session_state.data, use_container_width=True)
