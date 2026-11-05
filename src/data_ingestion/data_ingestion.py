import cv2
import os
import pandas as pd 
from torch.utils.data import Dataset,DataLoader
from PIL import Image


# class DataIngestion:
#     def get_image(root:str):
#         image = []
#         bbox = []
#         for sub_fol in os.listdir(root):
#             if os.path.isdir(root):
#                 files = os.path.join(root,sub_fol)
#                 for img in os.listdir(files):
#                     img_path = os.path.join(files,img)
#                     file_name = os.path.basename(img_path)
#                     name = file_name.split(".")[0]
#                     name = name + ".txt"
#                     bbox_path = os.path.join(root,"label",name)
#                     image.append(img_path)
#                     bbox.append(bbox_path)
#         return {"Image":image,
#                 "Bbox":bbox}
                
class Animal(Dataset):
    def __init__(self,df,tf):
        self.paths,self.ys,self.tf = df['Path'],df['y'],tf
    def __len__(self):
        return len(self.paths)
    def __getitem__(self,i):
        img = Image.open(self.paths[i]).convert('RGB')
        return self.tf(img),self.ys[i]








    


