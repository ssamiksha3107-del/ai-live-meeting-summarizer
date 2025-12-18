import streamlit as st
from datetime import datetime

st.set_page_config(page_title="AI Live Meeting Summarizer")

st.title("🎙️ AI Live Meeting Summarizer")

st.markdown("Record meetings and generate AI-powered summaries.")

if st.button("Start Recording"):
    st.info("Recording started... (demo mode)")

if st.button("Stop & Summarize"):
    st.success("Recording stopped")
    st.subheader("Transcript")
    st.write("This is a sample transcript of the meeting.")

    st.subheader("Meeting Summary")
    st.write("""
    - Discussion about project deadlines  
    - Agreement on next milestones  
    - Action items assigned to team members
    """)

st.caption(f"Session Time: {datetime.now().strftime('%d %b %Y, %I:%M %p')}")
