import streamlit as st
from stmol import showmol
import streamlit.components.v1 as components
import py3Dmol
import pandas as pd
import numpy as np
from PIL import Image
import webbrowser
from link_button import link_button

class MolGeneration:
    def __init__(self):
        st.set_page_config(layout="wide")
        hide_streamlit_style = """
                    <style>
                    MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        image = Image.open("//me4012_sw/xub2023/WEB_CONTENT/logo.png")
        col1.image(image, width=250)
        col2.markdown("# MolGeneration")
        col2.markdown(" ### Scaffold-Constrained Drug Design with Graph Transformer-based Reinforcement Learning")
        st.markdown("***")

    def intro(self):
        st.markdown("### :balloon: Introduction")
        st.markdown(
            "***DrugGPT*** presents a ligand design strategy based on the autoregressive model, GPT2, focusing on chemical space exploration and the discovery of ligands for specific proteins. More detail about model please go to: <https://github.com/LIYUESEN/druggpt> ."
        )
        st.write("With the rapid development of computational chemistry and artificial intelligence, computational methods and tools in drug design are becoming increasingly important.")
        st.write("Our project combines computational chemistry and AI technologies to offer users an intuitive and efficient solution for molecular generation.")
        st.markdown("***")

    def usage(self):
        st.write("1. **Visit the official website**: Users can directly access the Molecular Generation Online project through our official website without the need for account registration.")
        st.write("2. **Navigate to the molecular generation tool**: On the website's homepage, you will find an intuitive navigation menu that includes various options for molecular generation tools.")
        st.write("3. **Input molecular features and parameters**: In the tool interface, you can **input the desired molecular features and parameters**, such as target structure, molecular weight range, drug activity, etc.")
        st.write("4. **Initiate molecular generation process**: Click the **'Generate'** button to initiate the molecular generation process. The project will utilize computational chemistry and AI algorithms to generate multiple molecular structures that meet the specified requirements.")
        st.write("5. **Browse and filter generated molecules**: Once the generation process is complete, you will receive a list of generated molecules. You can **browse detailed information** about these molecules and filter/sort them according to your needs to find the most suitable ones.")
        st.write("6. **Download and save molecular results**: Once you find satisfactory molecular structures, you can choose to **download related data, images, or files** for further analysis and use. You can also save the molecules to your device for future access and utilization.")

    # def my_button(self, items, name, content):
    #     items.button(name, on_click=self.go_link(content))
    #

    def side_bar(self):
        myside_bar = st.sidebar
        with myside_bar:
            myside_bar.markdown('## Database_Related links')
            c1, c2 = st.columns(2)
            with c1:
                link_button("ZINC", "https://rdkit.org/")
                link_button("DrugBank", "https://www.drugbank.com/")
            with c2:
                link_button("ChEMBL", "https://www.ebi.ac.uk/chembl/")
                link_button("PubChem", "https://pubchem.ncbi.nlm.nih.gov/")
        with myside_bar:
            myside_bar.markdown('## Generated_Model_Related links')
            cc1, cc2, cc3 = st.columns(3)
            with cc1:
                link_button("GENTRL", "https://github.com/insilicomedicine/gentrl")
                link_button("MolGPT", "https://github.com/devalab/liggpt")
            with cc2:
                link_button("ORGAN", "https://github.com/Hanjun-Dai/sdvae")
                link_button("REINVENT", "https://github.com/MarcusOlivecrona/REINVENT")
            with cc3:
                link_button("JT-VAE", "https://github.com/wengong-jin/icml18-jtnn")
                link_button("MolRNN", "https://github.com/kevinid/molecule_generator")
        with myside_bar:
            myside_bar.markdown('## Benchmarking_Platform_Related links')
            ccc1, ccc2, ccc3 = st.columns(3)
            with ccc1:
                link_button("MOSES", "https://github.com/molecularsets/moses")
            with ccc2:
                link_button("GuacaMol", "https://www.benevolent.com/")
            with ccc3:
                link_button("SMINA-Docking", "https://github.com/cieplinski-tobiasz/smina-docking-benchmark")


if __name__ == '__main__':
    My_mol_gen = MolGeneration()
    My_mol_gen.intro()
    My_mol_gen.usage()
    My_mol_gen.side_bar()
