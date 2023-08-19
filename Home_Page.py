import streamlit as st
import py3Dmol
from stmol import showmol
from stmol import *


st.set_page_config(layout="wide",page_title="DrugDesignWeb",page_icon="home_icon.png")
hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
                body {
        font-size: 100px;
    }
            </style>

            """
def my_main():
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.sidebar.success("Select a demo above.")
    col1, col2 = st.columns(2)

    # 上传自定义蛋白
    my_pdb = open("AF-Q1ACB3-F1-model_v4.pdb",'r').read()

    view = py3Dmol.view(width=400, height=400)
    view.addModel(my_pdb, "pdb")

    # pymol分子实际大小
    # view = py3Dmol.view(query='3K8Y', width=300, height=300)

    chA = {"chain": 'A'}
    chB = {"chain": 'B'}
    # 设置条带颜色
    view.setStyle({"cartoon": {"color": "spectrum"}})
    # 设置配体颜色
    view.addStyle({"elem": 'C', "hetflag": True},
                  {"stick": {"color": "green", "radius": 0.2}})

    view.addStyle({"hetflag": True},
                  {"stick": {"radius": 0.2}})
    # 设置缩放
    view.zoomTo()
    # 设置旋转
    view.spin()
    view.setBackgroundColor("#ffffff")

    with col1:
        showmol(view, height=400, width=400)
        st.markdown(" **Homogentisate Solanesyl Transferase**(HST) by Alphafold2(UniProt: [Q1ACB3](https://www.uniprot.org/uniprotkb/Q1ACB3/entry#structure))")
    col2.markdown("# Computational Biology Department")
    col2.markdown(" ### A platform that integrates commonly used biological computing ")
    col2.markdown("Create by xubiao ")
    st.markdown("***")
    st.markdown('<style>body { font-size: 16px; }</style>', unsafe_allow_html=True)
    st.markdown("Welcome to the Computational Biology Department, an online platform that provides various computational tools for researchers, biologists, and pharmaceutical developers. Our website offers a range of functionalities such as molecule generation, virtual screening, protein structure prediction, and ADMET prediction, helping you accelerate research progress, discover new drug candidates, and understand the pharmacokinetic properties of drugs.")
    st.markdown("**Key Features:**")
    st.markdown("1. **Molecule Generation:** Utilize our powerful algorithms and models to quickly generate molecules with specific structures or properties. This feature supports drug development, compound design, and molecular simulation research.")
    st.markdown("2. **Virtual Screening:** Through virtual screening techniques, we efficiently screen vast compound libraries to identify potential molecules with drug-like activity. This significantly reduces experimental costs and time, expediting the process of drug discovery.")
    st.markdown("3. **Protein Structure Prediction:** Utilizing advanced protein structure prediction models, we can predict the three-dimensional structure of proteins based on given protein sequences. This provides vital insights for studying protein function, related diseases, and drug design.")
    st.markdown("4. **ADMET Prediction:** ADMET (Absorption, Distribution, Metabolism, Excretion, and Toxicity) properties are crucial factors in drug development. Our ADMET prediction feature allows you to assess the bioactivity, pharmacokinetic properties, and toxicity potential of candidate molecules rapidly. This assists in screening the most promising drug candidates.")
    st.markdown("Whether you are involved in drug development, pharmacology research, or molecular simulation, the Computational Biology Department offers powerful computational tools and accurate prediction results to support your scientific research and pharmaceutical innovations.")
    st.markdown("***")
    st.markdown("**Author:** xubiao")
    st.markdown("**Email:** 1224897184@qq.com")


if __name__ == '__main__':
    my_main()
