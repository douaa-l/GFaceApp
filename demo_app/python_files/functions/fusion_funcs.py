import numpy as np
import cv2
import os
import sys
import pandas as pd

from demo_app.python_files.utils import get_name_num_from_img, calcul_threshold_acc

#function to retrieve feature fusion score for one pair
def ff_pair(path_img1,path_img2,rest_models,rec_model):
    ff_df=pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject\demo_app\data\files\feature_fusion_scores.csv")
    ff_df['image1'] = ff_df['image1'].astype(int)
    ff_df['image2'] = ff_df['image2'].astype(int)
    name1,img1=get_name_num_from_img(path_img1)
    name2, img2 = get_name_num_from_img(path_img2)
    print(name1,name2,img2,img1)
    col=""
    # create the column name
    if len(rest_models)==3:
        col=f"ff_all_{rec_model.lower()}"
    elif len(rest_models)==2:
        col=f"ff_{rest_models[0].lower()}_{rest_models[1].lower()}_{rec_model.lower()}"
        if col not in ff_df.columns:
            col = f"ff_{rest_models[1].lower()}_{rest_models[0].lower()}_{rec_model.lower()}"

    line = ff_df.loc[
        (ff_df['name1'] == name1) & (ff_df['name2'] == name2) & (ff_df['image1'] == img1) & (ff_df['image2'] == img2)]
    i=line.index[0]//600
    score=line[col].iloc[0]
    threshold,acc,far,frr=calcul_threshold_acc(ff_df[[col]],i)
    return score,threshold

#function to retrieve feature fusion for one fold
def ff_fold(nb_fold,rest_models,rec_model):
    ff_df = pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject\demo_app\data\files\feature_fusion_scores.csv")
    ff_df['image1'] = ff_df['image1'].astype(int)
    ff_df['image2'] = ff_df['image2'].astype(int)
    if len(rest_models)==3:
        col=f"ff_all_{rec_model.lower()}"
    elif len(rest_models)==2:
        col=f"ff_{rest_models[0].lower()}_{rest_models[1].lower()}_{rec_model.lower()}"
        if col not in ff_df.columns:
            col = f"ff_{rest_models[1].lower()}_{rest_models[0].lower()}_{rec_model.lower()}"

    threshold, acc, far, frr = calcul_threshold_acc(ff_df[[col]], nb_fold)
    return acc, threshold
# function to retrieve feature fusion for al dataset
def ff_all(rest_models,rec_models):
    THR=[]
    ACC=[]
    FAR=[]
    FRR=[]
    ff_df = pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject\demo_app\data\files\feature_fusion_scores.csv")
    ff_df['image1'] = ff_df['image1'].astype(int)
    ff_df['image2'] = ff_df['image2'].astype(int)
    if len(rest_models) == 3:
        col = f"ff_all_{rec_model.lower()}"
    elif len(rest_models) == 2:
        col = f"ff_{rest_models[0].lower()}_{rest_models[1].lower()}_{rec_model.lower()}"
        if col not in ff_df.columns:
            col = f"ff_{rest_models[1].lower()}_{rest_models[0].lower()}_{rec_model.lower()}"

    for i in range(10):
        threshold, acc, far, frr = calcul_threshold_acc(ff_df[[col]], i)
        THR.append(threshold)
        ACC.append(acc)
        FAR.append(far)
        FRR.append(frr)
    total_acc=sum(ACC)/len(ACC)
    return total_acc

#*****************************************************************************************

#function to retrieve score level fusion for one pair
def sf_pair(path_img1,path_img2,rest_models,rec_model):
    sf_df = pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject\demo_app\data\files\score_fusion_file.csv")
    sf_df['image1'] = sf_df['image1'].astype(int)
    sf_df['image2'] = sf_df['image2'].astype(int)
    name1, img1 = get_name_num_from_img(path_img1)
    name2, img2 = get_name_num_from_img(path_img2)

    print(name1, name2, img2, img1)
    col = ""
    # create the column name
    col = f"sf_{rest_models[0].lower()}_{rest_models[1].lower()}_{rec_model.lower()}"
    if col not in sf_df.columns:
        col = f"sf_{rest_models[1].lower()}_{rest_models[0].lower()}_{rec_model.lower()}"

    line = sf_df.loc[
        (sf_df['name1'] == name1) & (sf_df['name2'] == name2) & (sf_df['image1'] == img1) & (sf_df['image2'] == img2)]
    i = line.index[0] // 600
    score = line[col].iloc[0]
    threshold, acc, far, frr = calcul_threshold_acc(sf_df[[col]], i)
    return score, threshold

#function to retrieve score fusion for one fold
def sf_fold(nb_fold,rest_models,rec_model):
    sf_df = pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject\demo_app\data\files\score_fusion_file.csv")
    sf_df['image1'] = sf_df['image1'].astype(int)
    sf_df['image2'] = sf_df['image2'].astype(int)
    col = f"sf_{rest_models[0].lower()}_{rest_models[1].lower()}_{rec_model.lower()}"
    if col not in sf_df.columns:
        col = f"sf_{rest_models[1].lower()}_{rest_models[0].lower()}_{rec_model.lower()}"

    threshold, acc, far, frr = calcul_threshold_acc(sf_df[[col]], nb_fold)
    return acc, threshold
# function to retrieve score fusion for al dataset
def sf_all(rest_models,rec_model):
    THR = []
    ACC = []
    FAR = []
    FRR = []
    sf_df = pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject\demo_app\data\files\score_fusion_file.csv")
    sf_df['image1'] = sf_df['image1'].astype(int)
    sf_df['image2'] = sf_df['image2'].astype(int)
    col = f"sf_{rest_models[0].lower()}_{rest_models[1].lower()}_{rec_model.lower()}"
    if col not in sf_df.columns:
        col = f"sf_{rest_models[1].lower()}_{rest_models[0].lower()}_{rec_model.lower()}"

    for i in range(10):
        threshold, acc, far, frr = calcul_threshold_acc(sf_df[[col]], i)
        THR.append(threshold)
        ACC.append(acc)
        FAR.append(far)
        FRR.append(frr)
    total_acc = sum(ACC) / len(ACC)
    return total_acc


#*****************************************************************************************

#function to retrieve hybrid level fusion for one pair
def hf_pair(path_img1,path_img2,rest_models_lev1,rest_model_lev2,rec_model):
    hf_df = pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject\demo_app\data\files\hybrid_fusion_scores.csv")
    hf_df['image1'] = hf_df['image1'].astype(int)
    hf_df['image2'] = hf_df['image2'].astype(int)
    name1, img1 = get_name_num_from_img(path_img1)
    name2, img2 = get_name_num_from_img(path_img2)

    print(name1, name2, img2, img1)
    col = ""
    # create the column name
    if len(rest_models)==3:
        col=f"hf_l1_all_l2_gfpgan_{rec_model.lower()}"
    elif len(rest_models)==2:
        col = f"hf_l1_{rest_models_lev1[0].lower()}_{rest_models_lev1[1].lower()}_l2_{rest_model_lev2.lower()}_{rec_model.lower()}"
        if col not in hf_df.columns:
            col = f"hf_l1_{rest_models_lev1[1].lower()}_{rest_models_lev1[0].lower()}_l2_{rest_model_lev2.lower()}_{rec_model.lower()}"

    line = hf_df.loc[
        (hf_df['name1'] == name1) & (hf_df['name2'] == name2) & (hf_df['image1'] == img1) & (hf_df['image2'] == img2)]
    i = line.index[0] // 600
    score = line[col].iloc[0]
    threshold, acc, far, frr = calcul_threshold_acc(hf_df[[col]], i)
    return score, threshold

#function to retrieve score fusion for one fold
def hf_fold(nb_fold,rest_models_lev1,rest_model_lev2,rec_model):
    hf_df = pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject\demo_app\data\files\hybrid_fusion_scores.csv")
    hf_df['image1'] = hf_df['image1'].astype(int)
    hf_df['image2'] = hf_df['image2'].astype(int)
    if len(rest_models) == 3:
        col = f"hf_l1_all_l2_gfpgan_{rec_model.lower()}"
    elif len(rest_models) == 2:
        col = f"hf_l1_{rest_models_lev1[0].lower()}_{rest_models_lev1[1].lower()}_l2_{rest_model_lev2.lower()}_{rec_model.lower()}"
        if col not in hf_df.columns:
            col = f"hf_l1_{rest_models_lev1[1].lower()}_{rest_models_lev1[0].lower()}_l2_{rest_model_lev2.lower()}_{rec_model.lower()}"

    threshold, acc, far, frr = calcul_threshold_acc(hf_df[[col]], nb_fold)
    return acc, threshold
# function to retrieve score fusion for al dataset
def hf_all(rest_models_lev1,rest_model_lev2,rec_model):
    THR = []
    ACC = []
    FAR = []
    FRR = []
    hf_df = pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject\demo_app\data\files\hybrid_fusion_scores.csv")
    hf_df['image1'] = hf_df['image1'].astype(int)
    hf_df['image2'] = hf_df['image2'].astype(int)
    if len(rest_models) == 3:
        col = f"hf_l1_all_l2_gfpgan_{rec_model.lower()}"
    elif len(rest_models) == 2:
        col = f"hf_l1_{rest_models_lev1[0].lower()}_{rest_models_lev1[1].lower()}_l2_{rest_model_lev2.lower()}_{rec_model.lower()}"
        if col not in hf_df.columns:
            col = f"hf_l1_{rest_models_lev1[1].lower()}_{rest_models_lev1[0].lower()}_l2_{rest_model_lev2.lower()}_{rec_model.lower()}"

    for i in range(10):
        threshold, acc, far, frr = calcul_threshold_acc(hf_df[[col]], i)
        THR.append(threshold)
        ACC.append(acc)
        FAR.append(far)
        FRR.append(frr)
    total_acc = sum(ACC) / len(ACC)
    return total_acc

if __name__ == '__main__':

    #path_img1 = "demo_app/data/images/XQLFW/Nathalie_Baye_0002.jpg"
    #path_img2 = "demo_app/data/images/XQLFW/Nathalie_Baye_0004.jpg"
    #path_img1 = "demo_app/data/images/XQLFW/Jonathan_Edwards_0005.jpg"
    #path_img2 = "demo_app/data/images/XQLFW/Mark_Hurlbert_0003.jpg"
    rest_models=['sgpn','GFPgan']
    rec_model='adaFace'
    #score,threshold=hf_pair(path_img1, path_img2, rest_models,'GPEN', rec_model)
    #acc,threshold=hf_fold(9,rest_models,'gpen',rec_model)
    acc=hf_all(rest_models,'gpen',rec_model)
    print(f"score is {acc}")
