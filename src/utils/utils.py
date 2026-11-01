import cv2
import os



def load_img(img_path:str):
    image = cv2.imread(img_path)
    return image


def load_bbox(bbox_path:str):
    try:
        with open(bbox_path,"r") as file:
            content = file.read()
            data = content.split()
            if (len(data) != 5):
                return 0
            coordinates = list(map(float,data[1:]))
            return coordinates
    except Exception as e:
        print(bbox_path)




def crop_it(image,bbox):
    x_min,y_min,x_max,y_max = bbox
    cp = image[
        int(y_min):int(y_max),
        int(x_min):int(x_max)
    ]
    crop_rgb = cv2.cvtColor(cp,cv2.COLOR_BGR2RGB)
    return crop_rgb

def resize(cropped_img):
    return resized_img

def save_it(resized_img,img_path):
    crp_root = r"C:\Users\Rahul Yadav\Desktop\cropped_img\train"
    rm = img_path.split('\\')[6]
    rm1 = img_path.split('\\')[7]
    path = os.path.join(crp_root,rm)
    i_path = os.path.join(crp_root,rm,rm1)
    os.makedirs(path,exist_ok=True)
    cv2.imwrite(i_path,resized_img)




