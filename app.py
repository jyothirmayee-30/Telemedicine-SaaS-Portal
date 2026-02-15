import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import time
import random

st.set_page_config(page_title="HealthLink SaaS", layout="wide", page_icon="🏥")

st.markdown("""
    <style>
    .main { background-color: #f8fafc; color: #1e293b; }
    .stMetric { background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 15px; }
    </style>
    """, unsafe_allow_html=True)

if 'patient_vitals' not in st.session_state:
    data = {
        'Date': pd.date_range(end=datetime.now(), periods=10).strftime("%Y-%m-%d"),
        'HeartRate': [random.randint(70, 90) for _ in range(10)],
        'BloodPressure': [random.randint(110, 130) for _ in range(10)]
    }
    st.session_state.patient_vitals = pd.DataFrame(data)

st.title("🏥 HealthLink | Telemedicine Portal")
st.write("Secure Clinical Data Management & Patient Monitoring")

tab1, tab2 = st.tabs(["🩺 Doctor's View", "👤 Patient Portal"])

with tab1:
    st.subheader("Patient Queue - Severity Priority")
    queue = pd.DataFrame({
        "Patient ID": ["P-902", "P-441", "P-112"],
        "Symptom Score": [85, 42, 15],
        "Status": ["URGENT", "STABLE", "ROUTINE"]
    })
    st.table(queue)

with tab2:
    st.subheader("My Health Metrics")
    m1, m2, m3 = st.columns(3)
    m1.metric("Avg Heart Rate", "76 bpm", delta="-2 bpm")
    m2.metric("Last BP Reading", "118/78")
    m3.metric("Medication Adherence", "95%")

    fig = px.line(st.session_state.patient_vitals, x='Date', y='HeartRate', title="Heart Rate History")
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    with st.form("log_symptoms"):
        st.write("Daily Symptom Check-in")
        fever = st.checkbox("Fever")
        pain = st.slider("Pain Level", 0, 10, 0)
        submitted = st.form_submit_button("Submit Records")
        if submitted:
            st.success("Health records updated successfully.")
