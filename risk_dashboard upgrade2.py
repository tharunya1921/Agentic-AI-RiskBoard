import streamlit as st
import pandas as pd

st.set_page_config(page_title="Comprehensive Risk Register", layout="centered")
st.title("📋 Agentic AI Risk Register")

# Initialize session
if "risk_log" not in st.session_state:
    st.session_state.risk_log = []

# Input form
with st.form("risk_form"):
    st.subheader("🧾 Record a New Risk")

    risk_id = st.text_input("📌 Risk ID")
    title = st.text_input("📝 Risk Title")
    desc = st.text_area("🔍 Risk Description")
    originator = st.text_input("👤 Originator (Who identified this risk)")
    owner = st.text_input("🛡️ Risk Owner (Responsible person or role)")
    associated_events = st.text_area("📎 Associated Events")
    project = st.text_input("📁 Project Name (or Programme/Portfolio)")
    
    likelihood = st.slider("⚠️ Likelihood (1 = Low, 5 = High)", 1, 5)
    consequence = st.slider("🔥 Consequence (1 = Low, 5 = High)", 1, 5)
    score = likelihood * consequence
    rating = "High" if score >= 20 else "Medium" if score >= 10 else "Low"

    response_category = st.selectbox("📚 Response Category", ["Accept", "Mitigate", "Transfer", "Avoid"])
    response_action = st.text_area("✅ Response Taken")
    economic_impact = st.text_area("💰 Economic Impact")
    benefit_impact = st.text_area("🎯 Impact on Benefits")
    objective_impact = st.text_area("🧭 Impact on Objectives")
    secondary_consequence = st.text_area("🔄 Secondary Consequences")
    status = st.selectbox("📡 Risk Status", ["Open", "Closed", "Monitoring"])

    submitted = st.form_submit_button("➕ Add Risk")

    if submitted and title:
        st.session_state.risk_log.append({
            "Risk ID": risk_id,
            "Title": title,
            "Description": desc,
            "Originator": originator,
            "Owner": owner,
            "Associated Events": associated_events,
            "Project": project,
            "Likelihood": likelihood,
            "Consequence": consequence,
            "Score": score,
            "Risk Rating": rating,
            "Response Category": response_category,
            "Response Action": response_action,
            "Economic Impact": economic_impact,
            "Impact on Benefits": benefit_impact,
            "Impact on Objectives": objective_impact,
            "Secondary Consequences": secondary_consequence,
            "Status": status
        })
        st.success(f"✅ Risk '{title}' added to the register.")

# Show all risks
if st.session_state.risk_log:
    st.subheader("🗂️ Current Risk Register")
    df = pd.DataFrame(st.session_state.risk_log)
    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📤 Download Risk Register as CSV", data=csv, file_name="risk_register.csv", mime="text/csv")
else:
    st.info("No risks recorded yet. Use the form above to begin.")