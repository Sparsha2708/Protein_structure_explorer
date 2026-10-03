# Protein_structure_explorer
## Protein Structure Explorer 🧬

A Streamlit-based application that allows users to search for proteins by **name and species**, select the desired protein from matching UniProt entries, and visualize its **predicted 3D structure** interactively using Mol*.

The application uses **UniProt** to retrieve protein information and accession IDs, then uses the **AlphaFold database** in the backend to obtain the predicted protein structure as a PDB file. The downloaded structure is rendered in an interactive **Mol*** 3D viewer.

### Tech Stack

* Python
* Streamlit
* UniProt REST API
* AlphaFold Database API
* Mol*
* HTML/CSS/JavaScript

### Workflow

```text
Protein name + Species
        ↓
      UniProt
        ↓
Matching proteins
        ↓
User selects protein
        ↓
UniProt accession
        ↓
AlphaFold Database
        ↓
PDB structure
        ↓
Interactive Mol* visualization
```
