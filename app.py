import streamlit as st
import streamlit.components.v1 as components
from uniprot_test import get_protein_info,get_structure

st.title("🧬 Protein Structure Explorer")

protein = st.text_input("Enter protein name")

species = st.text_input("Enter species")

if st.button("Search"):

    st.session_state["proteins"] = get_protein_info(protein, species)


if "proteins" in st.session_state:

    proteins = st.session_state["proteins"]

    st.write("Matching proteins:")

    options = [
        f"{p['name']} — {p['accession']}"
        for p in proteins
    ]

    selected = st.selectbox(
        "Choose one from the dropdown:",
        options
    )

    st.write("You selected:", selected)
    selected_accession = selected.split(" — ")[1]

    st.write("Selected accession:", selected_accession)
    if st.button("View Structure"):
        structure_url = get_structure(selected_accession)
        st.write("Structure downloaded!")

        components.iframe(
        "http://localhost:8000/molstar/viewer.html",
        height=650
    )

    #st.write("Protein information:")
    #st.write(protein_info)

    #st.write("Structure URL:")
    #st.write(structure_url)
    #components.iframe(
        #"http://localhost:8000/molstar/viewer.html",
        #height=650
    #)