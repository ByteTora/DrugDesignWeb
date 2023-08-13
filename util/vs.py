import os
import pandas as pd
import streamlit as st
import argparse
import plotly.graph_objects as go
        
class VSUtil(object):
    """
    Introduction page class,
    """
    @classmethod
    def my_expander(self, lists, name):
        chosen_item = []
        with st.expander(name):
            st.write(f'choose {name} (at least one):')
            for item in lists:
                chosen_item.append(item) if st.checkbox(item) is True else None
        return chosen_item


    @classmethod
    def file_load(self, file):
        file_dir = f"//me4012_sw/web_database/vir_screening/{file.name}"
        fdisk = open(file_dir, 'wb')
        fdisk.write(file.getvalue())
        fdisk.close()
        return file_dir


    @classmethod
    def str_process(self, lists):
        new_str = ''
        length = len(lists)
        if length >1:
            for i in range(length-1):
                new_str = lists[i] + ' ' + lists[i+1]
                lists[i+1] = new_str
            return f'"{new_str}"'
        else:
            return f'"{lists[0]}"'


    @classmethod
    def data_process(self, train_data_file, model_list, split_list, descriptor):
        model_list = self.str_process(model_list)
        split_list = self.str_process(split_list)
        descriptor = self.str_process(descriptor)
        log_file = "/opt/sge/users/allsw2022/VS/log/"
        os.popen(f"cd /opt/sge/users/allsw2022/VS;qsub -cwd run_VS.sh -f {train_data_file} -m {model_list} -s {split_list} -d {descriptor} ")


    @classmethod
    def show_chart(self, data):
        model_order = ['SVM', 'RF', "XGB", "KNN"]
        fig = go.Figure()
        color_palette = ['#FF7F0E', '#1F77B4', '#FFDC00', '#2CA02C']

        fig.add_trace(go.Bar(
            x=data['model'],
            y=data['auc_roc'],
            name='AUC-ROC',
            marker_color=color_palette[0]
        ))

        fig.add_trace(go.Bar(
            x=data['model'],
            y=data['f1_score'],
            name='F1 Score',
            marker_color=color_palette[1]
        ))

        fig.add_trace(go.Bar(
            x=data['model'],
            y=data['acc'],
            name='Accuracy',
            marker_color=color_palette[2]
        ))

        fig.add_trace(go.Bar(
            x=data['model'],
            y=data['mcc'],
            name='MCC',
            marker_color=color_palette[3]
        ))

        fig.update_layout(
            title='Model Performance',
            xaxis_tickangle=-45,
            xaxis=dict(
                title='Model',
                categoryorder='array',
                categoryarray=model_order
),
            yaxis=dict(title='Scores'),
            barmode='group',
            legend=dict(
                x=1.02, 
                y=1,
                xanchor='left',
                yanchor='top'),
                font=dict(size=14)
        )
        st.plotly_chart(fig, use_container_width=True)        


    @classmethod
    def prediction(self):
        with st.expander("Data format"):
            st.markdown("123")
            train_data_file = st.file_uploader("## Upload predict file")
            view_data = st.checkbox("check your predict data")
            if view_data:
                if train_data_file is not None:
                    dataframe = pd.read_csv(train_data_file)
                    st.dataframe(dataframe)
                else:
                    st.warning("please upload file!")           