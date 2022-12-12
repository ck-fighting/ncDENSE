import numpy as np
file_train = 'Ten_Fold_Data/Train_6'
file_test = 'Ten_Fold_Data/Test_6'

# List_A_Eight = [1, 0, 0, 0]
# List_U_Eight = [0, 0, 1, 0]
# List_G_Eight = [0, 1, 0, 0]
# List_C_Eight = [0, 0, 0, 1]
# List_N_Eight = [0, 0, 0, 0] #The coding rules

# List_A_Eight = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
# List_U_Eight = [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1]
# List_G_Eight = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
# List_C_Eight = [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0]
# List_N_Eight = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #The coding rules
List_A_Eight = [1, 0, 0, 0, 0, 0, 1, 0]
List_U_Eight = [0, 0, 1, 0, 1, 0, 0, 0]
List_G_Eight = [0, 1, 0, 0, 0, 0, 0, 1]
List_C_Eight = [0, 0, 0, 1, 0, 1, 0, 0]
List_N_Eight = [0, 0, 0, 0, 0, 0, 0, 0]


# def train_data_50():#将训练集的碱基放入
#     Train_Matrix = []
#     Train_label = []
#     for line in open(file_train):
#         if(line[0] == ">"):
#             if (line.split()[-1] == '5S_rRNA'):
#                  Train_label.append(0)
#             if (line.split()[-1] == '5_8S_rRNA'):
#                 Train_label.append(1)
#             if (line.split()[-1] == 'tRNA'):
#                  Train_label.append(2)
#             if (line.split()[-1] == 'ribozyme'):
#                 Train_label.append(3)
#             if (line.split()[-1] == 'CD-box'):
#                 Train_label.append(4)
#             if (line.split()[-1] == 'miRNA'):
#                 Train_label.append(5)
#             if (line.split()[-1] == 'Intron_gpI'):
#                 Train_label.append(6)
#             if (line.split()[-1] == 'Intron_gpII'):
#                 Train_label.append(7)
#             if (line.split()[-1] == 'HACA-box'):
#                 Train_label.append(8)
#             if (line.split()[-1] == 'riboswitch'):
#                 Train_label.append(9)
#             if (line.split()[-1] == 'IRES'):
#                 Train_label.append(10)
#             if (line.split()[-1] == 'leader'):
#                 Train_label.append(11)
#             if (line.split()[-1] == 'scaRNA'):
#                 Train_label.append(12)
#         else:
#             Tem_List = []
#             for i in range(150):
#                 if (i < len(line) - 1):
#                     if (line[i] == 'A' or line[i] == 'a'):
#                         Tem_List.append(List_A_Eight)
#                     elif (line[i] == 'T' or line[i] == 't'):
#                         Tem_List.append(List_U_Eight)
#                     elif (line[i] == 'C' or line[i] == 'c'):
#                         Tem_List.append(List_C_Eight)
#                     elif (line[i] == 'G' or line[i] == 'g'):
#                         Tem_List.append(List_C_Eight)
#                     else:
#                         Tem_List.append(List_N_Eight)
#                 else:
#                     Tem_List.append(List_N_Eight)
#             Tem_List = np.array(Tem_List)
#             Train_Matrix.append(Tem_List)
#     Train_Matrix = np.array(Train_Matrix)
#     Train_label = np.array(Train_label)
#     return Train_Matrix, Train_label
#
# def test_data_50():
#     Test_Matrix = []  # Save the matrix of ncRNAs
#     Test_label = []
#     for line in open(file_test):
#         if(line[0] == ">"):
#             if (line.split()[-1] == '5S_rRNA'):
#                 Test_label.append(0)
#             if (line.split()[-1] == '5_8S_rRNA'):
#                 Test_label.append(1)
#             if (line.split()[-1] == 'tRNA'):
#                 Test_label.append(2)
#             if (line.split()[-1] == 'ribozyme'):
#                 Test_label.append(3)
#             if (line.split()[-1] == 'CD-box'):
#                 Test_label.append(4)
#             if (line.split()[-1] == 'miRNA'):
#                 Test_label.append(5)
#             if (line.split()[-1] == 'Intron_gpI'):
#                 Test_label.append(6)
#             if (line.split()[-1] == 'Intron_gpII'):
#                 Test_label.append(7)
#             if (line.split()[-1] == 'HACA-box'):
#                 Test_label.append(8)
#             if (line.split()[-1] == 'riboswitch'):
#                 Test_label.append(9)
#             if (line.split()[-1] == 'IRES'):
#                 Test_label.append(10)
#             if (line.split()[-1] == 'leader'):
#                 Test_label.append(11)
#             if (line.split()[-1] == 'scaRNA'):
#                 Test_label.append(12)
#         else:
#             Tem_List = []
#             for i in range(150):
#                 if (i < len(line) - 1):
#                     if (line[i] == 'A' or line[i] == 'a'):
#                         Tem_List.append(List_A_Eight)
#                     elif (line[i] == 'T' or line[i] == 't'):
#                         Tem_List.append(List_U_Eight)
#                     elif (line[i] == 'C' or line[i] == 'c'):
#                         Tem_List.append(List_C_Eight)
#                     elif (line[i] == 'G' or line[i] == 'g'):
#                         Tem_List.append(List_C_Eight)
#                     else:
#                         Tem_List.append(List_N_Eight)
#                 else:
#                     Tem_List.append(List_N_Eight)
#             Tem_List = np.array(Tem_List)
#             Test_Matrix.append(Tem_List)
#     Test_Matrix = np.array(Test_Matrix)
#     Test_label = np.array(Test_label)
#     return Test_Matrix, Test_label

def train_data():
    Train_Matrix = []  # Save the matrix of ncRNAs in test
    Train_label = []  # Save the label of ncRNAs in test
    for line in open(file_train):
        if(line[0] == '>'):
            #print(line.split()[-1])
            if(line.split()[-1] == '5S_rRNA'):
                Train_label.append(0)
            if(line.split()[-1] == '5_8S_rRNA'):
                Train_label.append(1)
            if (line.split()[-1] == 'tRNA'):
                Train_label.append(2)
            if (line.split()[-1] == 'ribozyme'):
                Train_label.append(3)
            if(line.split()[-1] == 'CD-box'):
                Train_label.append(4)
            if(line.split()[-1] == 'miRNA'):
                Train_label.append(5)
            if (line.split()[-1] == 'Intron_gpI'):
                Train_label.append(6)
            if (line.split()[-1] == 'Intron_gpII'):
                Train_label.append(7)
            if (line.split()[-1] == 'HACA-box'):
                Train_label.append(8)
            if(line.split()[-1] == 'riboswitch'):
                Train_label.append(9)
            if(line.split()[-1] == 'IRES'):
                Train_label.append(10)
            if (line.split()[-1] == 'leader'):
                Train_label.append(11)
            if (line.split()[-1] == 'scaRNA'):
                Train_label.append(12)
        else:
            Tem_List = []
            for i in range(len(line[0: -1])):
                if (i < len(line) - 1):
                    if (line[i] == 'A' or line[i] == 'a'):
                        Tem_List.append(List_A_Eight)
                    elif (line[i] == 'T' or line[i] == 't'):
                        Tem_List.append(List_U_Eight)
                    elif (line[i] == 'C' or line[i] == 'c'):
                        Tem_List.append(List_C_Eight)
                    elif (line[i] == 'G' or line[i] == 'g'):
                        Tem_List.append(List_C_Eight)
                    else:
                        Tem_List.append(List_N_Eight)
                else:
                    Tem_List.append(List_N_Eight)
            Tem_List = np.array(Tem_List)
            Train_Matrix.append(Tem_List)

    Train_Matrix = np.array(Train_Matrix)
    Train_label = np.array(Train_label)
    return Train_Matrix, Train_label
def test_data():
    Test_Matrix = []  # Save the matrix of ncRNAs in test
    Test_label = []  # Save the label of ncRNAs in test
    for line in open(file_test):
        if(line[0] == '>'):
            #print(line.split()[-1])
            if(line.split()[-1] == '5S_rRNA'):
                Test_label.append(0)
            if(line.split()[-1] == '5_8S_rRNA'):
                Test_label.append(1)
            if (line.split()[-1] == 'tRNA'):
                Test_label.append(2)
            if (line.split()[-1] == 'ribozyme'):
                Test_label.append(3)
            if(line.split()[-1] == 'CD-box'):
                Test_label.append(4)
            if(line.split()[-1] == 'miRNA'):
                Test_label.append(5)
            if (line.split()[-1] == 'Intron_gpI'):
                Test_label.append(6)
            if (line.split()[-1] == 'Intron_gpII'):
                Test_label.append(7)
            if (line.split()[-1] == 'HACA-box'):
                Test_label.append(8)
            if(line.split()[-1] == 'riboswitch'):
                Test_label.append(9)
            if(line.split()[-1] == 'IRES'):
                Test_label.append(10)
            if (line.split()[-1] == 'leader'):
                Test_label.append(11)
            if (line.split()[-1] == 'scaRNA'):
                Test_label.append(12)
        else:
            Tem_List = []
            for i in range(len(line[0: -1])):

                if (i < len(line) - 1):
                    if (line[i] == 'A' or line[i] == 'a'):
                        Tem_List.append(List_A_Eight)
                    elif (line[i] == 'T' or line[i] == 't'):
                        Tem_List.append(List_U_Eight)
                    elif (line[i] == 'C' or line[i] == 'c'):
                        Tem_List.append(List_C_Eight)
                    elif (line[i] == 'G' or line[i] == 'g'):
                        Tem_List.append(List_C_Eight)
                    else:
                        Tem_List.append(List_N_Eight)
                else:
                    Tem_List.append(List_N_Eight)

            Tem_List = np.array(Tem_List )
            Test_Matrix.append(Tem_List)

    Test_Matrix = np.array(Test_Matrix)
    Test_label = np.array(Test_label)
    return Test_Matrix, Test_label