import streamlit as st
from util import PSPUtil
from PIL import Image



st.set_page_config(layout="wide")
hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def introduction():
    st.markdown('# 🌏Alphafold2 online')
    st.markdown("Welcome to AlphaFold2 Online! This is an online tool based on Google DeepMind's latest development, AlphaFold2, a protein structure prediction model. With this project, you can conveniently use AlphaFold2 on the web without the need for complex command-line operations. The main objective of this tool is to provide a convenient and accurate protein structure prediction service for researchers, biologists, and drug developers.")
    st.markdown("## 🧬Background")
    st.markdown("Proteins are crucial functional molecules in living organisms, playing key roles in many biological processes. Understanding the three-dimensional structure of proteins is essential for comprehending their functions, studying related diseases, and drug development. However, obtaining protein structures through experimental methods is a challenging and time-consuming task. To address this challenge, DeepMind developed AlphaFold2, an advanced protein structure prediction model.")
    co1, co2 = st.columns(2, gap="large")

    with co1:
        st.markdown("## 💻Usage")
        st.markdown("1. **Enter Protein Sequence:** In the provided ***Browse files*** butto on the website, you can upload the protein sequence of interest.")
        st.markdown("2. **Process your task:** When you upload you files, AlphaFold2 online will automatically analyze and predict the three-dimensional structure of the input protein sequence.")
        st.markdown("3. **Obtain Prediction Result:** Once the prediction is complete, you will receive an accurate protein structure prediction result. You can explore and visualize the protein structure using the visualization tools provided on the website, you can clicked the ***Task status*** button obtain more detail.")
        st.markdown("4. **Analyze the Prediction Result:** AlphaFold2 also provides detailed structure analysis information, including secondary structures, domain boundaries, and structure confidence assessment. These insights will help you better understand the structural characteristics of the protein.")
        st.markdown("5. **Export and Share:** You can choose to export the prediction results in common protein structure file formats for further analysis or sharing with others.")

    with co2:
        image = Image.open('./pipline.png')
        st.image(image)
    st.markdown('***')
    st.markdown("**References:**")
    st.markdown("- Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., ... & Silver, D. (2021). Highly accurate protein structure prediction with AlphaFold. Nature, 596(7873), 583-589. [doi:10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2)")
    st.markdown("- Hou, J., Wu, T., & Wang, Z. (2021). AlphaFold2 and the future of structural biology. *Bioinformatics*, 37(14), 2038-2040. [doi:10.1093/bioinformatics/btab170](https://doi.org/10.1093/bioinformatics/btab170)")
    st.markdown("- Baek, M., DiMaio, F., Anishchenko, I., Dauparas, J., Ovchinnikov, S., & Baker, D. (2021). Accurate prediction of protein structures and interactions using a three-track neural network. *Science*, 373(6556), 871-876. [doi:10.1126/science.abj8754](https://doi.org/10.1126/science.abj8754)")
    st.markdown("- Tunyasuvunakool, K., Adler, J., Wu, Z., Green, T., Zielinski, M., Zidek, A., ... & Bates, P. A. (2021). Highly accurate protein structure prediction for the human proteome. *Nature*, 596(7873), 590-596. [doi:10.1038/s41586-021-03828-1](https://doi.org/10.1038/s41586-021-03828-1)")
    st.markdown("- Streamlit Team. (2021). Streamlit: The fastest way to build custom ML tools. Retrieved from [https://streamlit.io/](https://streamlit.io/)")
    st.markdown("- Allaire, J. J., Xie, Y., McPherson, J., Luraschi, J., Ushey, K., Atkins, A., ... & Arslan, R. (2021). *R Markdown: The Definitive Guide*. Chapman and Hall/CRC. [Link to the book](https://bookdown.org/yihui/rmarkdown)")

def sub_work():
    st.warning(
    '***NOTE:*** Upload sequence single letter representation, uppercase, without special characters appearing, no special line breaks or Chinese characters appear.',
    icon="⚠️") 
    uploaded_files = st.file_uploader("**1. Upload Amino Acid Sequence Files(fasta Format)**")
    title = st.text_input('**2. Please input your name:**')
    if title: st.write('Success!')
    PSPUtil.submit(uploaded_files, title)


def task_status():
    utils = PSPUtil()
    pdb_result_labels = ['ranked_0.pdb', "ranked_1.pdb", "ranked_2.pdb", "ranked_3.pdb", "ranked_4.pdb"]
    result_label = [result_label for result_label in pdb_result_labels]
    dir_name = [dir_name for dir_name in utils.read_path(path)]

    
    select_dir = st.selectbox("Select your job", dir_name, 8)
    if select_dir:
        fasta_name = [fasta_name for fasta_name in utils.read_path(path + '/' + select_dir)]

        fasta_file = st.selectbox("Select your fasta", fasta_name)
        if fasta_file:
            rank_pdbs = st.selectbox("view sort by rank", result_label)
            co1, co2 = st.columns(2)
            try:
                my_pdb = open(f'{path}/{select_dir}/{fasta_file}/{rank_pdbs}', 'r').read()
                utils.view_pdb(my_pdb)
                with co2:
                    st.download_button(f"Download {rank_pdbs}", data=my_pdb, file_name=f"{select_dir}_{fasta_file}_{rank_pdbs}")
            except:
                st.error('Your job not complet, Please wait!', icon="🚨")





if __name__ == "__main__":
    # Choose the Output path
    path = "//me4012_sw/web_database/pro_str_prediction/output"
    st.sidebar.title("Please choose mode")
    genre = st.sidebar.selectbox("", ("Introduction", "Submit work", "Task status"))
    if genre == "Introduction":
        # Calling the intro() method
        introduction()                  
    elif genre == "Submit work":
        # Calling the sub_work() method       
        sub_work()               
    else:
        # Calling the task_process() method  
        task_status()
