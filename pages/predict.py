import streamlit as st
import requests

## Header
st.markdown("## 🐧 Zoologist")

## Predict
col1, col2 = st.columns(2)
with col1:
    option_island = st.selectbox("Island", ["Torgersen", "Biscoe", "Dream"])
    option_sex = st.radio(
        "Sex",
        ["Male", "Female"],
        horizontal=True,
    )

with col2:
    option_bill_length = st.slider("Bill length (in mm)", 32.1, 59.6, 44.0, 0.01)
    option_bill_depth = st.slider("Bill depth (in mm)", 13.1, 21.5, 17.0, 0.01)
    option_flipper_length = st.slider(
        "Flipper length (in mm)", 172.0, 231.0, 200.0, 0.01
    )
    option_body_mass = st.slider("Body mass (in g)", 2700.0, 6300.0, 4200.0, 1.0)

hostname = st.secrets["API_URL"]
base_url = f"{hostname}/predict"
params = {
    "island": option_island,
    "bill_length_mm": option_bill_length,
    "bill_depth_mm": option_bill_depth,
    "flipper_length_mm": option_flipper_length,
    "body_mass_g": option_body_mass,
    "sex": option_sex,
}
response = requests.get(base_url, params=params)

## Display predictions
# st.markdown(f"URL : {response.url}")

as_json = response.json()
# with st.container(border=True):
confidence = as_json["probability"] * 100
confidence_level = (
    "high"
    if confidence > 90
    else ("good" if confidence > 80 else "a bit low" if confidence > 70 else "low")
)
confidence_block = (
    st.success
    if confidence > 90
    else (st.info if confidence > 80 else st.warning if confidence > 70 else st.error)
)
# with st.success():
prediction: str = as_json["species"]
a_or_an = "an" if prediction[0].lower() in list("aeiouy") else "a"

confidence_block(
    f"Their confidence is **{confidence_level} : {confidence:.1f}%**",
    icon="✅",
    title=f"Experts think it's {a_or_an} :red[{prediction}]",
)
