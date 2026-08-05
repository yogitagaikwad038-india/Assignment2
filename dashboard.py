import streamlit as st
import pandas as pd
import plotly.express as px

from app import investigate
from app import chunks

st.set_page_config(
    page_title="AI Fake News & Rumor Buster",
    layout="wide"
)

st.title("🕵️ AI Fake News & Rumor Buster")

st.markdown(
"""
Compare Official Sources,
Internal Logs,
and Social Media Rumors.
"""
)

official = len(
    [x for x in chunks
     if x.metadata["source_type"] == "Official"]
)

internal = len(
    [x for x in chunks
     if x.metadata["source_type"] == "Internal"]
)

rumor = len(
    [x for x in chunks
     if x.metadata["source_type"] == "Rumor"]
)

# Sidebar

st.sidebar.header("Statistics")

st.sidebar.metric(
    "Total Chunks",
    len(chunks)
)

st.sidebar.metric(
    "Official Sources",
    official
)

st.sidebar.metric(
    "Internal Logs",
    internal
)

st.sidebar.metric(
    "Rumor Posts",
    rumor
)

# Pie Chart

chart_df = pd.DataFrame({
    "Source": [
        "Official",
        "Internal",
        "Rumor"
    ],
    "Count": [
        official,
        internal,
        rumor
    ]
})

fig = px.pie(
    chart_df,
    names="Source",
    values="Count",
    title="Source Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Investigation Section

question = st.text_input(
    "Ask a Question",
    "Was the AI Product cancelled?"
)

if st.button("Investigate"):

    result = investigate(question)

    st.subheader(
        "Fact Check Result"
    )

    st.write(result)

# Metadata Table

st.subheader("Document Metadata")

data = []

for chunk in chunks:

    data.append({
        "Source":
            chunk.metadata["source_type"],

        "Date":
            chunk.metadata["date"],

        "Preview":
            chunk.page_content[:100]
    })

st.dataframe(data)