import streamlit as st
import requests

# """
# # Zoologist front
# """

# st.markdown("""
# Remember that there are several ways to output content into your web page...

# Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
# """)

st.markdown("## 🐧 Zoologist")

# """
# ## Here we would like to add some controllers in order to ask the user to input the characteristics of the penguin. We need to know all the inputs required by our model to make a prediction.

# 1. Let's ask for:
# - island (the location where the penguin lives: Biscoe, Dream or Torgersen)
# - bill length (in mm)
# - bill depth (in mm)
# - flipper length (in mm)
# - body mass (in g)
# - sex ("Male" or "Female")
# """
option_island = st.selectbox("Island", ["Torgersen", "Biscoe", "Dream"])
option_bill_length = st.slider("Bill length (in mm)", 32.1, 59.6, 44.0, 0.01)
option_bill_depth = st.slider("Bill depth (in mm)", 13.1, 21.5, 17.0, 0.01)
option_flipper_length = st.slider("Flipper length (in mm)", 172.0, 231.0, 200.0, 0.01)
option_body_mass = st.slider("Body mass (in g)", 2700.0, 6300.0, 4200.0, 1.0)
option_sex = st.selectbox("Sex", ["Male", "Female"])

# """
# ## Once we have these, let's call our API in order to retrieve a prediction
# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...
# 🤔 How could we call our API ? Of course... The `requests` package 💡
# What are the steps to follow in order to call an API ?
# 1. Which url will you use? Save it in a variable so you can easily change it later...
# 2. Let's build a dictionary containing the parameters for our API...
# 3. Let's call our API using the `requests` package...
# 4. Let's retrieve the prediction from the **JSON** returned by the API...
# ## Finally, we can display the prediction to the user
# """

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

st.markdown(f"URL : {response.url}")
as_json = response.json()
st.markdown(f"Response : {as_json["species"]}")
st.markdown(f"Probability : {as_json["probability"]*100:.2f} %")
