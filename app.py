import streamlit as st
import json

from utils.retrieve import retrieve_guideline
from utils.reviewer import review_claim

st.title("Cotiviti AI Claims Review Assistant")

st.write("A simple demonstration of RAG-based agentic AI for clinical claims review.")

with open("data/synthetic_claims.json", "r", encoding="utf-8") as f:
    sample_cases = json.load(f)

case_names = [case["patient_id"] for case in sample_cases]

selected_case_name = st.selectbox(
    "Select a Sample Case",
    case_names
)

selected_case = next(
    case for case in sample_cases
    if case["patient_id"] == selected_case_name
)

note = st.text_area(
    "Clinical Note",
    value=selected_case["clinical_note"],
    height=200
)

diagnosis = st.text_input(
    "Diagnosis Code",
    value=selected_case["diagnosis_code"]
)

if st.button("Review Claim"):

    guideline = retrieve_guideline(diagnosis)

    if guideline is None:
        st.error("No guideline found.")
        st.stop()

    result = review_claim(note, guideline)

    st.subheader("Recommendation")

    if result["decision"] == "APPROVE":
        st.success(result["decision"])
    else:
        st.warning(result["decision"])

    st.subheader("Retrieved Guideline")

    st.info(guideline["recommendation"])

    st.subheader("Explanation")

    st.write(result["explanation"])

    if result["missing"]:
        st.subheader("Missing Documentation")

        for item in result["missing"]:
            st.write(f"• {item}")

    else:
        st.success("No missing documentation detected.")