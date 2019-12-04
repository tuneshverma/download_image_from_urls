from PIL import Image
import requests
from io import BytesIO
import cv2
import os
import pandas as pd
from tqdm import tqdm


# loop over the image URLs
def download(folder_path):
    csv = os.listdir(folder_path)
    for deo in csv:

        url_data = pd.read_csv(folder_path + '/' + str(deo))
        list_of_urls = url_data['Thumbnail']

        for url in tqdm(list_of_urls):
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            img.save('data/' + deo.split('.')[0] + '/' + (url.split('/'))[-1])


download('D:\MintM\deo_classifier\csv_data')
