import streamlit as st
from stmol import showmol
from stmol import *
import os
import py3Dmol
from PIL import Image



class PSPUtil(object):
    """ This class is the base structure for all protein structure prediction models.
    Mainly, it provides the general methods for introduce, task process and submit the given data.
    """

    def __find_squence_index(self, lines):
        index = []
        for i in range(len(lines)):
            if ">" in lines[i]:
                index.append(i)
        return index


    def __find_squence(self, lines, index):
        len_index_list = len(index)
        len_lines = len(lines)
        squence_list = []
        for i in range(len_index_list):
            if i < len_index_list - 1:
                start_lines = index[i] + 1
                end_lines = index[i + 1]
            else:
                start_lines = index[i] + 1
                end_lines = len_lines
            squence = ''
            for j in range(start_lines, end_lines):
                new_squence = lines[j].strip()
                squence += new_squence
            squence = squence.upper()
            specialChars = "*-_"
            for specialChar in specialChars:
                squence = squence.replace(specialChar, '')
            squence = squence.strip()
            squence_list.append(squence)
        return squence_list


    def __squence_name(self, lines, index_list, n):
        name_list = []
        for i in index_list:
            name = lines[i][1:n].strip()
            name_list.append(name)
        return name_list


    # 定义输出固定宽度的文件，num为文件名序号， width为固定输出每行的字符数， name为文件开头的名字，squence为要输出的序列

    def __output_sequence_with_fix_width(self, num, width, name, squence, fasta_dir):
        num_str = str(num)
        file_name = name + '_' + num_str + '.fasta'
        file_name_in = '>' + name + '_' + num_str
        squence_len = len(squence)
        lines = squence_len // width + 1
        file_write = open(fasta_dir + file_name, 'a+')
        # print(file_name_in,file=file_write)
        file_write.write(f"{file_name_in}\n")
        while lines > 0:
            squence_width = squence[:width]
            # file_write = open(fasta_dir+file_name,'a+')
            # print(squence_80,file=file_write)
            file_write.write(f"{squence_width}\n")
            squence = squence[width:]
            lines -= 1
        file_write.write(squence[:-1])
        # print(squence[:-1],file=file_write,end="")
        file_write.close()


    # 定义书写序列列表的函数，squence_list为生成的序列， width为定义的每行字符的个数，name为想要输出的名字）

    def __write_squence(self, squence_list, name_list, fasta_dir):
        for i in range(len(squence_list)):
            squence_i = squence_list[i]
            name_i = name_list[i].split('.')[0]
            self.__output_sequence_with_fix_width(num=i, width=79, name=name_i, squence=squence_i, fasta_dir=fasta_dir)



    # process input sequence
    def __sequence_process(cls, loaded_file):
        # save upload file
        fdisk = open(f"//me4012_sw/web_database/pro_str_prediction/fasta/{loaded_file.name}", 'wb')
        fdisk.write(loaded_file.getvalue())
        fdisk.close()
     
        # obtain upload file name(multi-sequence file)
        name =  ''.join(loaded_file.name).rsplit('.', 1)
      
        # create new path for every upload mutli-sequence file, this path save splicted single fasta file.
        os.makedirs(f"//me4012_sw/web_database/pro_str_prediction/fasta/{name[0]}/")
       
        # splict mutli-sequence file and save
        with open(f"//me4012_sw/web_database/pro_str_prediction/fasta/{loaded_file.name}", 'r') as f:
            lines = f.readlines()
            new_index_list = self.__find_squence_index(lines)
            squence_list = self.__find_squence(lines, new_index_list)
            name_list = self.__squence_name(lines, new_index_list, 14)
            self.__write_squence(squence_list=squence_list, name_list=name_list, fasta_dir=f'//me4012_sw/web_database/pro_str_prediction/fasta/{name[0]}/')
        # return upload file(multi-sequence file name)
        return name[0]

    @classmethod
    def submit(cls, loaded_files, user_name):

        if loaded_files:
            # process input sequence and obtain file name
            name = cls.__sequence_process(loaded_files)

            # define qsub log file output path
            error_log = "/opt/sge/users/allsw2022/alphafold-2.2.0/qsub_log/error_log"
            standard_Log = "/opt/sge/users/allsw2022/alphafold-2.2.0/qsub_log/standard_log"

            # submi job
            os.popen(f"cd /opt/sge/users/allsw2022/alphafold-2.2.0;qsub -e {error_log} -o {standard_Log} alphafold_auto_qsub_xub.sh {name}")
            st.success('Upload Success!', icon="✅")
        else:pass


    def read_path(self, mydir):
        """Read a dir and list all the folder name to save a list()
        Arguments:
            dir (str): The path of need process
        Return:
            file_names (list): the average loss value based on the calculation of loss function with given test set.
        """
        file_names = os.listdir(mydir)
        return [file_lists for file_lists in file_names]


    def view_pdb(self, pdb):
            # create py3Dmol object
            view = py3Dmol.view(width=500, height=500)
            # load pdb file
            view.addModel(pdb, 'pdb')
            # set pdb style
            view.setStyle({'cartoon': {'color': 'spectrum'}})
            # set ligand color
            view.addStyle({"elem": "C", "hetflag": True},
                          {"stick": {"color": "green", "radius": 0.2}})
            view.addStyle({"hetflag": True},
                          {"stick": {"radius": 0.2}})
            view.zoomTo()
            view.setBackgroundColor('#ffffff')
            # show pdb
            showmol(view, height=500, width=500)        



