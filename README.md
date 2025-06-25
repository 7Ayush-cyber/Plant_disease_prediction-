# AgriScan - Plant Disease Detector

AgriScan is a deep learning-powered web application that identifies plant diseases from leaf images. It leverages multiple CNN architectures like **MobileNetV2**, **ResNet18**, **EfficientNetB0**, and a custom **CNN** to provide accurate predictions along with **treatment suggestions** (both natural and chemical) and **plant care tips**.

---

##  Features

- Upload a leaf image to detect plant disease.
- Choose from 4 trained models: MobileNetV2, ResNet18, EfficientNetB0, and Custom CNN.
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
- **EfficientNetB0** – Scalable and high-performing model fine-tuned for accurate plant disease classification.

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


---

## Results & Performance Metrics

| Model         | Validation Accuracy | Precision        | Recall           | F1-score         | Support (Val) | Notes                                                               |
|---------------|---------------------|------------------|------------------|------------------|---------------|--------------------------------------------------                   |
| Custom CNN    | 69.43%              | Macro: 0.5662    | Macro: 0.5563    | Macro: 0.5234    | 4,122         | From-scratch CNN baseline                                           |
| ResNet-18     | 81.39%              | Weighted: 0.8797 | Weighted: 0.8139 | Weighted: 0.8242 | 4,127         | Pretrained + fine-tune                                              |
| MobileNetV2   | 94.00%              | Weighted: 0.95   | Weighted: 0.94   | Weighted: 0.94   | 4,122         | Pretrained + fine-tune; rapid convergence                           |
| EfficientNet  | 93.23%              | Weighted: 0.95   | Weighted: 0.94   | Weighted: 0.94   | 4,122         | Pretrained; two-stage fine-tuning (feature-lock → low-LR full-tune) |

---

## Key Findings

1. **Baseline CNN underfits**: Achieved only ~69% validation accuracy, indicating limited representational power when trained from scratch.  
2. **ResNet-18 gains from transfer learning**: Fine-tuning a pretrained ResNet-18 boosts accuracy to ~81%, with strong weighted precision and F1 performance.  
3. **MobileNetV2 excels in speed & accuracy**: Lightweight architecture converges rapidly and achieves ~94% validation accuracy, making it ideal for resource-constrained deployments.  
4. **EfficientNet matches top accuracy**: After a two-phase tuning schedule, EfficientNet also reaches ~93.2%, at the cost of a more complex training procedure.  
5. **Recommended model**: Use **MobileNetV2** for the best trade-off between ease of training, inference speed, and classification performance.  



_For full training scripts and hyperparameter settings, see the corresponding Jupyter notebooks in this repository._  

---

For each disease, the model provides:

- Natural Treatment
- Chemical Treatment
- Preventive Care Tips

---

##  How to Use the Web App

1. **Download the Repository & Model Files**  
   - Clone this repo locally:  
     ```bash
     git clone https://github.com/7Ayush-cyber/Plant_disease_prediction-.git
     cd Plant_disease_prediction-
     ```  
   - (Optional) Manually download any large models into the project root:  
     - `plant_disease_cnn_model.h5`  
     - `plant_disease_mobilenetv2.h5`  
     - `plant_disease_ResNet18.h5`  
     - `efficientnetb0_finetuned.h5`

2. **Set Up & Run Locally**  
   ```bash
   # create a virtual environment
   python3 -m venv venv && source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   Launch the Streamlit App (streamlit run app.py)


