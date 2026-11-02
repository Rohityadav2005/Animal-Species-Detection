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
    h, w = cropped_img.shape[:2]

    target_size = 384

    scale = target_size / max(h, w)
    new_w, new_h = int(round(w * scale)), int(round(h * scale))

    resized_img = cv2.resize(cropped_img, (new_w, new_h), interpolation=cv2.INTER_AREA if scale < 1 else cv2.INTER_LINEAR)

    pad_w = target_size - new_w
    pad_h = target_size - new_h

    top = pad_h // 2
    bottom = pad_h - top
    left = pad_w // 2
    right = pad_w - left

    resized_img = cv2.copyMakeBorder(
        src=resized_img,
        top=top,
        bottom=bottom,
        left=left,
        right=right,
        borderType=cv2.BORDER_CONSTANT,
        value=(128, 128, 128)
    )

    return resized_img

def save_it(resized_img,img_path):
    crp_root = r"C:\Users\Rahul Yadav\Desktop\cropped_img\train"
    rm = img_path.split('\\')[6]
    rm1 = img_path.split('\\')[7]
    path = os.path.join(crp_root,rm)
    i_path = os.path.join(crp_root,rm,rm1)
    os.makedirs(path,exist_ok=True)
    cv2.imwrite(i_path,resized_img)




