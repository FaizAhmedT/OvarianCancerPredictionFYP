import streamlit as st
import joblib
import numpy as np

model = joblib.load("./ovarian_cancer_model.pkl")

test_data = {}

st.subheader("Select patient feature values: ")

col1, col2 = st.columns(2)

with col1:
    test_data["AFP"] = st.slider("AFP", 0.0, 20.0, step=0.1, value=2.75, key="AFP")
    test_data["AG"] = st.slider("AG", 0.0, 40.0, step=0.1, value=16.6)
    test_data["ALB"] = st.slider("ALB", 20.0, 55.0, step=0.1, value=39.2)
    test_data["ALP"] = st.slider("ALP", 20.0, 800.0, step=0.1, value=26.0)
    test_data["ALT"] = st.slider("ALT", 2.0, 100.0, step=0.1, value=16.0)
    test_data["AST"] = st.slider("AST", 5.0, 50.0, step=0.1, value=17.0)
    test_data["Age"] = st.slider("Age", 10, 90, value=45)
    test_data["BASO#"] = st.slider("BASO#", 0.00, 2.00, step=0.0001, value=0.05)
    test_data["BASO%"] = st.slider("BASO%", 0.00, 2.00, step=0.0001, value=0.74)
    test_data["BUN"] = st.slider("BUN", 0.00, 8.00, step=0.0001, value=5.27)
    test_data["CA125"] = st.slider("CA125", 5.0, 2800.0, step=0.1, value=2555.0)
    test_data["CA19-9"] = st.slider("CA19-9", 0.0, 1200.0, step=0.1, value=18.41)
    test_data["CEA"] = st.slider("CEA", 0.0, 100.0, step=0.1, value=0.82)
    test_data["CL"] = st.slider("CL", 90.0, 110.0, step=0.1, value=103.2)
    test_data["CO2CP"] = st.slider("CO2CP", 10.0, 40.0, step=0.1, value=24.0)
    test_data["CREA"] = st.slider("CREA", 40.0, 100.0, step=0.1, value=65.7)
    test_data["Ca"] = st.slider("Ca", 0.0, 4.0, step=0.01, value=2.35)
    test_data["DBIL"] = st.slider("DBIL", 0.0, 8.0, step=0.01, value=2.9)
    test_data["EO#"] = st.slider("EO#", 0.00, 0.50, step=0.01, value=0.00)
    test_data["EO%"] = st.slider("EO%", 0.0, 6.0, step=0.1, value=0.07)
    test_data["GGT"] = st.slider("GGT", 0.0, 120.0, step=1.0, value=17.0)
    test_data["GLO"] = st.slider("GLO", 10.0, 50.0, step=0.1, value=26.9)
    test_data["GLU."] = st.slider("GLU.", 2.0, 15.0, step=0.1, value=4.76)

with col2:
    test_data["HCT"] = st.slider("HCT", 0.00, 0.50, step=0.001, value=0.372)
    test_data["HE4"] = st.slider("HE4", 25.0, 1500.0, step=0.1, value=853.5)
    test_data["HGB"] = st.slider("HGB", 50.0, 180.0, step=0.1, value=123.0)
    test_data["IBIL"] = st.slider("IBIL", 1.0, 20.0, step=0.1, value=8.0)
    test_data["K"] = st.slider("K", 2.00, 6.00, step=0.01, value=4.7)
    test_data["LYM#"] = st.slider("LYM#", 0.00, 5.00, step=0.01, value=1.73)
    test_data["LYM%"] = st.slider("LYM%", 1.0, 50.0, step=0.1, value=27.2)
    test_data["MCH"] = st.slider("MCH", 10.0, 50.0, step=0.1, value=30.6)
    test_data["MCV"] = st.slider("MCV", 50.0, 110.0, step=0.1, value=92.6)
    test_data["MONO#"] = st.slider("MONO#", 0.00, 1.0, step=0.01, value=0.42)
    test_data["MONO%"] = st.slider("MONO%", 1.00, 12.00, step=0.01, value=6.55)
    test_data["Menopause"] = st.slider("Menopause", 0, 1, step=1, value=1)
    test_data["Mg"] = st.slider("Mg", 0.00, 1.50, step=0.01, value=1.11)
    test_data["NEU"] = st.slider("NEU", 30.0, 100.0, step=0.1, value=65.5)
    test_data["Na"] = st.slider("Na", 100.0, 180.0, step=0.1, value=139.1)
    test_data["PCT"] = st.slider("PCT", 0.00, 1.00, step=0.01, value=0.25)
    test_data["PDW"] = st.slider("PDW", 5.0, 25.0, step=0.1, value=17.4)
    test_data["PHOS"] = st.slider("PHOS", 0.50, 2.00, step=0.01, value=1.25)
    test_data["PLT"] = st.slider("PLT", 100.0, 550.0, step=0.1, value=339.0)
    test_data["RBC"] = st.slider("RBC", 2.00, 6.00, step=0.01, value=4.01)
    test_data["RDW"] = st.slider("RDW", 8.00, 25.00, step=0.01, value=14.6)
    test_data["TBIL"] = st.slider("TBIL", 2.00, 25.00, step=0.01, value=10.9)
    test_data["TP"] = st.slider("TP", 35.0, 85.0, step=0.1, value=66.1)
    test_data["UA"] = st.slider("UA", 100.0, 450.0, step=0.1, value=215.6)

test_data_array = np.array(
    [
        test_data["Age"],
        test_data["IBIL"],
        test_data["CA19-9"],
        test_data["Menopause"],
        test_data["ALB"],
        test_data["CA125"],
        test_data["NEU"],
        test_data["HE4"],
        test_data["GLO"],
        test_data["LYM%"],
        test_data["ALP"],
        test_data["HGB"],
        test_data["PCT"],
        test_data["LYM#"],
        test_data["TBIL"],
        test_data["Ca"],
        test_data["MONO#"],
        test_data["AST"],
        test_data["CEA"],
        test_data["PLT"],
        test_data["EO#"],
        test_data["BASO%"],
        test_data["PDW"],
        test_data["EO%"],
        test_data["TP"],
        test_data["DBIL"],
        test_data["GLU."],
        test_data["AFP"],
        test_data["MCH"],
        test_data["RBC"],
        test_data["MONO%"],
        test_data["HCT"],
        test_data["BASO#"],
        test_data["CO2CP"],
        test_data["Na"],
        test_data["Mg"],
        test_data["CREA"],
        test_data["ALT"],
        test_data["K"],
        test_data["AG"],
        test_data["UA"],
        test_data["MCV"],
        test_data["RDW"],
        test_data["PHOS"],
        test_data["BUN"],
        test_data["CL"],
        test_data["GGT"],
    ]
).reshape(1, -1)

with st.sidebar:
    st.title("Ovarian Cancer FYP Demo")

    if st.button("Predict Ovarian Cancer", use_container_width=True):
        prediction = model.predict(test_data_array)[0]
        if prediction == 1:
            st.error("Ovarian Cancer Detected", icon="⚠️")
        else:
            st.success("No Ovarian Cancer Detected", icon="✅")
