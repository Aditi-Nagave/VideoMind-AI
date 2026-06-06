import streamlit as st
import pandas as pd
import plotly.express as px

from utils.api import (
    get_dashboard_stats
)

if "token" not in st.session_state:

    st.switch_page(
        "pages/Login.py"
    )

st.title(
    "📊 Dashboard Analytics"
)

data = get_dashboard_stats(
    st.session_state["token"]
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "📹 Total Videos",
        data["total_videos"]
    )

with col2:

    st.metric(
        "📝 Summaries",
        data["total_summaries"]
    )

col3, col4 = st.columns(2)

with col3:

    st.metric(
        "💬 Questions Asked",
        data["total_questions"]
    )

with col4:

    st.metric(
        "📊 Total Chats",
        data["total_chats"]
    )

st.markdown("---")

chart_df = pd.DataFrame(
    {
        "Metric": [
            "Videos",
            "Summaries",
            "Questions",
            "Chats"
        ],
        "Count": [
            data["total_videos"],
            data["total_summaries"],
            data["total_questions"],
            data["total_chats"]
        ]
    }
)

fig = px.bar(
    chart_df,
    x="Metric",
    y="Count",
    title="User Activity Overview"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig2 = px.pie(
    chart_df,
    values="Count",
    names="Metric",
    title="Activity Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)