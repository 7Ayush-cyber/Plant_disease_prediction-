# AgriScan - Plant Disease Detector

AgriScan is a deep learning-powered web application that identifies plant diseases from leaf images. It leverages multiple CNN architectures like **MobileNetV2**, **ResNet18**, and a custom **CNN** to provide accurate predictions along with **treatment suggestions** (both natural and chemical) and **plant care tips**.

---

##  Features

- Upload a leaf image to detect plant disease.
- Choose from 3 trained models: MobileNetV2, ResNet18, and Custom CNN.
- Get actionable treatment suggestions:
  - Natural remedies
  - Chemical solutions
  - Plant care and prevention tips
- Easy-to-use Streamlit web interface.

---

## Models Used

- **MobileNetV2** – Efficient and lightweight.
- **ResNet18** – Deep architecture for robust predictions.
- **Custom CNN** – Tailored for plant disease detection with flexibility.

Each model was trained on a labeled dataset of tomato, potato, and bell pepper diseases.

---

## Supported Classes

- `Pepper__bell___Bacterial_spot`
- `Pepper__bell___healthy`
- `Potato___Early_blight`
- `Potato___Late_blight`
- `Potato___healthy`
- `Tomato_Bacterial_spot`
- `Tomato_Early_blight`
- `Tomato_Late_blight`
- `Tomato_Leaf_Mold`
- `Tomato_Septoria_leaf_spot`
- `Tomato_Spider_mites_Two_spotted_spider_mite`
- `Tomato_Tomato_mosaic_virus`
- `Tomato_Tomato_YellowLeaf__Curl_Virus`
- `Tomato_Target_Spot`
- `Tomato_healthy`

For each disease, the app provides:

- Natural Treatment
- Chemical Treatment
- Preventive Care Tips

---



