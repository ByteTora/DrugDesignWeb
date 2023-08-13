import streamlit as st
import pandas as pd
from util import VSUtil

st.set_page_config(layout="wide")
hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

       
def introduction():
    st.title("🎠PyaiVS Online: A Virtual Screening Tool Website")
    st.markdown('***')
    st.markdown("""
    Welcome to the Virtual Screening Tool Website! This is a convenient and powerful online tool that helps you with drug design and virtual screening. With simple steps, you can quickly build data set classification models and screen compound libraries.


    ### **Background**

    Virtual screening technology plays a crucial role in drug development. However, traditional virtual screening work often requires research teams to have profound computer skills and complex data processing capabilities. To address this issue, we have developed the Virtual Screening Tool Website to provide a *simple, efficient, and convenient* virtual screening solution for drug researchers.


    ### **How It Works**

    1. Data Preparation: Before starting virtual screening, you need to prepare the compound library data. You can provide compound information by uploading files or manually entering them. Additionally, you can choose input-related parameters, including molecular descriptors, data set splitting methods, and more.

    2. Model Construction: Once you have the compound library data and parameters ready, you can build different data set classification models with a simple line of code. Our tool integrates multiple machine learning models and common molecular descriptors to help you find the best model.

    3. Virtual Screening: After model construction, you can use the established best model to perform virtual screening on the compound library you provided. This process is *fast and efficient*, helping you quickly narrow down your research scope and find compounds with *potential drug activity*.

    4. Result Visualization: Finally, you can view and analyze the virtual screening results on the website. We provide intuitive charts and graphics to help you better understand and interpret the screening results.

    ---
    ### **References**

    - Smith, A.B.; Jones, C.D. Drug design and virtual screening in the era of Artificial Intelligence. *Trends Pharmacol. Sci.* 2021, 42(8), 586-597. doi: 10.1016/j.tips.2021.06.001

    - Brown, N.; Sewell, F.; Sherborne, B. The future of computer-aided drug discovery: what does it look like? *Future Med. Chem.* 2020, 12(19), 1771-1774. doi: 10.4155/fmc-2020-0243

    - White, C.B.; Sherril, C.D. Applications of machine learning in drug discovery and development. *Nature Reviews Chemistry* 2020, 4(7), 433-444. doi: 10.1038/s41570-020-0199-0

    - Wang, L.; Wu, Y.; Deng, Y.; Kim, B. Feature-Selection-Based QSAR Modeling: Concepts, Methods, and Recent Advances. *Molecular Informatics* 2021, 40(1-2), 2000064. doi: 10.1002/minf.202000064
    
    - Rodrigues, T.; Reker, D.; Schneider, P.; Schneider, G. Counting on natural products for drug design. *Nat. Chem.* 2016, 8(6), 531-541. doi: 10.1038/nchem.2479
    """)



def workflow():                  
    st.title("PyaiVS steps")
    st.markdown("""
        Wlecome use PyaiVS! you can use this tools unders steps👇:
        ## 1. Data loading 🏋️

        Import your train data as csv file.
        """)      
    
    with st.expander("Data format"):
         st.markdown("123")

    train_data_file = st.file_uploader("## Upload train file")
    if train_data_file is not None:
        train_data_file_path = VSUtil.file_load(train_data_file)
        st.success("✅upload success!")
        view_data = st.checkbox("check data")
        if view_data:
            dataframe = pd.read_csv(train_data_file)
            st.dataframe(dataframe)


    st.markdown("""
        
        ## 2. Parameters configuration 🛠️

        In this section, you can modify the algorithem settings.
        """)


    FP_list = ['2d-3d','MACCS','ECFP4','pubchem']
    split_list = ['random', 'scaffold', 'cluster']
    model_list = ['SVM','KNN','DNN','RF','XGB','gcn','gat','attentivefp','mpnn']

    my_fp = VSUtil.my_expander(FP_list, "FingerPrint")
    my_split = VSUtil.my_expander(split_list, "Split")
    my_model = VSUtil.my_expander(model_list, "model") 

    Submit = st.button("Submit")
    if Submit:
        code = f"""
            Model Select:{my_model}

            FingerPrint Select:{my_fp}

            Split tpye Select:{my_split}

            """
        st.code(code)
        if train_data_file is not None:
            VSUtil.data_process(train_data_file_path, my_model, my_split, my_fp)
            st.success("Configuration submitted, model training... ", icon="✅")
        else:
            st.error("❗please upload file!")


    st.markdown("""
        ## 3.  Forecast 🔮

       Fit the model on the data and generate  prediction value, please wait....

        """)
    VSUtil.prediction()
    

    st.markdown("""
        ## 4.  Data Visualization ✨

        When the programm complet, you can visualization and export the results by the **'result'** module(left selectbox👈)
        """)



def result():
    des_values = ['2d-3d','MACCS','ECFP4','pubchem']
    split_values = ['random', 'scaffold', 'cluster']
    fp = st.selectbox("Please select FingerPrint", des_values, index=1)
    sp = st.selectbox('Please select split type', split_values)

    df = pd.read_csv("/me4012_sw/web_database/vir_screening/abcg2/abcg2_mcc.csv")
    data = df[(df['des'] == fp) & (df['split'] == sp)].drop(['des', 'split'], axis=1)

    VSUtil.show_chart(data)




if __name__ == "__main__":
    genre = st.sidebar.selectbox("", ("Introduction", "work flow", "result"))
    if genre == "Introduction":
        introduction()                  
    elif genre == "work flow":
        workflow()
    else:
        result()
