import os
import gdown


DRIVE_LINKS = {
    "plant_disease_cnn_model.h5": "https://drive.google.com/file/d/1y7-wa7ZYsw9I4K3FvSX5tslaHhLjpXmZ/view?usp=sharing",
    "efficientnetb0_finetuned.h5": "https://drive.google.com/file/d/11p0cbeVlOUWSydje6DPZnpZzjW5V0eq_/view?usp=sharing"
}

def download_model(filename, url):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        gdown.download(url, filename, quiet=False)
    else:
        print(f"{filename} already exists.")

def download_all_models():
    for fname, url in DRIVE_LINKS.items():
        download_model(fname, url)
