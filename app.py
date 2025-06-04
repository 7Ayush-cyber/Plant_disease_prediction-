# # import streamlit as st
# # import tensorflow as tf
# # import numpy as np
# # from PIL import Image
# # from predict import predict_plant_disease
# # import os

# # # Config
# # IMG_SIZE = (224, 224)
# # MODEL_PATH = 'C:/streamlit run app.pyUsers/ayush/Documents/Coding/Agriscan/plant_disease_mobilenetv2.h5'
# # CLASS_NAMES = [
# #     "Pepper__bell___Bacterial_spot",
# #     "Pepper__bell___healthy",
# #     "Potato___Early_blight",
# #     "Potato___healthy",
# #     "Potato___Late_blight",
# #     "Tomato_Target_Spot",
# #     "Tomato_Tomato_mosaic_virus",
# #     "Tomato_Tomato_YellowLeaf__Curl_Virus",
# #     "Tomato_Bacterial_spot",
# #     "Tomato_Early_blight",
# #     "Tomato_healthy",
# #     "Tomato_Late_blight",
# #     "Tomato_Leaf_Mold",
# #     "Tomato_Septoria_leaf_spot",
# #     "Tomato_Spider_mites_Two_spotted_spider_mite"
# # ]

# # @st.cache_resource
# # def load_model():
# #     return tf.keras.models.load_model(MODEL_PATH)

# # model = load_model()

# # # Title and UI
# # st.title("Plant Disease Classifier")
# # st.write("Upload a leaf image to detect the plant disease.")

# # uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# # if uploaded_file:
# #     image = Image.open(uploaded_file)
# #     st.image(image, caption="Uploaded Image", use_column_width=True)

# #     if st.button("Predict"):
# #         # Save temp file and predict
# #         image_path = "temp_image.jpg"
# #         image.save(image_path)

# #         prediction = predict_plant_disease(image_path, model, CLASS_NAMES)
# #         st.success(f"Predicted Disease: **{prediction}**")


# import streamlit as st
# import tensorflow as tf
# import numpy as np
# from PIL import Image
# from predict import predict_plant_disease
# import os

# # Config
# IMG_SIZE = (224, 224)
# CLASS_NAMES = [
#     "Pepper__bell___Bacterial_spot",
#     "Pepper__bell___healthy",
#     "Potato___Early_blight",
#     "Potato___healthy",
#     "Potato___Late_blight",
#     "Tomato_Target_Spot",
#     "Tomato_Tomato_mosaic_virus",
#     "Tomato_Tomato_YellowLeaf__Curl_Virus",
#     "Tomato_Bacterial_spot",
#     "Tomato_Early_blight",
#     "Tomato_healthy",
#     "Tomato_Late_blight",
#     "Tomato_Leaf_Mold",
#     "Tomato_Septoria_leaf_spot",
#     "Tomato_Spider_mites_Two_spotted_spider_mite"
# ]

# MODEL_PATHS = {
#     "MobileNetV2": "C:/Users/ayush/Documents/Coding/Agriscan/plant_disease_mobilenetv2.h5",
#     "CNN": "C:/Users/ayush/Documents/Coding/Agriscan/plant_disease_cnn_model.h5",
#     # "ResNet18": "models/plant_disease_resnet18.h5",
#     # "EfficientNet": "models/plant_disease_efficientnet.h5"
# }

# # Load models once and cache
# @st.cache_resource
# def load_model(model_name):
#     return tf.keras.models.load_model(MODEL_PATHS[model_name])

# # UI
# st.title("Plant Disease Classifier")
# st.write("Upload a leaf image and choose a model to detect plant disease.")

# # Model selection
# model_choice = st.selectbox("Select a model", list(MODEL_PATHS.keys()))
# model = load_model(model_choice)

# # File upload
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image", use_column_width=True)

#     if st.button("Predict"):
#         image_path = "temp_image.jpg"
#         image.save(image_path)

#         prediction = predict_plant_disease(image_path, model, CLASS_NAMES)
#         st.success(f"Model: **{model_choice}**\n\nPrediction: **{prediction}**")


import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from predict import predict_plant_disease


IMG_SIZE = (224, 224)

CLASS_NAMES = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___healthy",
    "Potato___Late_blight",
    "Tomato_Target_Spot",
    "Tomato_Tomato_mosaic_virus",
    "Tomato_Tomato_YellowLeaf__Curl_Virus",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_healthy",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite"
]

MODEL_PATHS = {
    "MobileNetV2": "C:/Users/ayush/Documents/Coding/Agriscan/plant_disease_mobilenetv2.h5",
    "CNN": "C:/Users/ayush/Documents/Coding/Agriscan/plant_disease_cnn_model.h5", 
    "ResNet18": "C:/Users/ayush/Documents/Coding/Agriscan/plant_disease_ResNet18.h5",
     # "EfficientNet": "models/plant_disease_efficientnet.h5"
    
}


TREATMENT_GUIDE = {
    "Pepper__bell___Bacterial_spot": {
        "natural": "Use copper-based sprays, prune infected leaves, and ensure good air circulation.",
        "chemical": "Apply fixed copper fungicides or streptomycin sprays.",
        "care": "Avoid overhead watering. Practice crop rotation and use disease-free seeds."
    },
    "Pepper__bell___healthy": {
        "natural": "Maintain proper watering and soil health.",
        "chemical": "No chemical treatment needed.",
        "care": "Regularly inspect plants for early signs of disease."
    },
    "Potato___Early_blight": {
        "natural": "Neem oil spray and compost tea application work well.",
        "chemical": "Use chlorothalonil or mancozeb-based fungicides.",
        "care": "Avoid wetting the foliage and rotate crops annually."
    },
    "Potato___healthy": {
        "natural": "Maintain optimal watering and sunlight.",
        "chemical": "Not applicable.",
        "care": "Use certified disease-free tubers and monitor regularly."
    },
    "Potato___Late_blight": {
        "natural": "Apply garlic oil or compost extract to affected leaves.",
        "chemical": "Spray metalaxyl or dimethomorph-based fungicides promptly.",
        "care": "Destroy infected plants, avoid overhead watering, and rotate crops."
    },
    "Tomato_Target_Spot": {
        "natural": "Use baking soda sprays or neem oil regularly.",
        "chemical": "Apply chlorothalonil or mancozeb fungicides weekly.",
        "care": "Remove infected leaves and maintain proper spacing."
    },
    "Tomato_Tomato_mosaic_virus": {
        "natural": "Remove and destroy infected plants. Practice strict hygiene.",
        "chemical": "No effective chemical cure. Focus on prevention.",
        "care": "Sterilize tools, avoid smoking near plants, and grow resistant varieties."
    },
    "Tomato_Tomato_YellowLeaf__Curl_Virus": {
        "natural": "Use yellow sticky traps to control whiteflies and spray neem oil.",
        "chemical": "Insecticides like imidacloprid can reduce vector populations.",
        "care": "Remove infected plants. Control whiteflies early and avoid planting near cotton."
    },
    "Tomato_Bacterial_spot": {
        "natural": "Spray copper-based solutions and remove infected plant material.",
        "chemical": "Use fixed copper fungicides. Avoid repeated use to prevent resistance.",
        "care": "Avoid overhead irrigation and rotate crops every season."
    },
    "Tomato_Early_blight": {
        "natural": "Compost tea, neem oil, and baking soda sprays help slow spread.",
        "chemical": "Use chlorothalonil, mancozeb, or azoxystrobin fungicides.",
        "care": "Remove lower infected leaves. Water at the base only."
    },
    "Tomato_healthy": {
        "natural": "Continue using compost, neem oil, and maintain proper sunlight exposure.",
        "chemical": "No chemical treatment necessary.",
        "care": "Use mulch, rotate crops, and fertilize regularly with compost."
    },
    "Tomato_Late_blight": {
        "natural": "Spray garlic or horsetail extract and avoid dense planting.",
        "chemical": "Apply fungicides like metalaxyl, cymoxanil, or dimethomorph early.",
        "care": "Destroy infected plants and do not compost them. Improve ventilation."
    },
    "Tomato_Leaf_Mold": {
        "natural": "Use milk spray (1:10 dilution) and improve air circulation.",
        "chemical": "Apply fungicides such as chlorothalonil or copper hydroxide.",
        "care": "Ensure dry foliage overnight. Space plants adequately."
    },
    "Tomato_Septoria_leaf_spot": {
        "natural": "Spray with compost tea or potassium bicarbonate.",
        "chemical": "Apply fungicides like mancozeb or chlorothalonil weekly.",
        "care": "Remove lower infected leaves and avoid wetting leaves when watering."
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "natural": "Spray water to dislodge mites, use neem oil or insecticidal soap.",
        "chemical": "Miticides like abamectin or bifenthrin can be effective.",
        "care": "Maintain humidity, introduce predatory mites (e.g., *Phytoseiulus persimilis*)."
    }
}


@st.cache_resource
def load_model(model_name):
    return tf.keras.models.load_model(MODEL_PATHS[model_name])


st.set_page_config(page_title="AgriScan - Plant Disease Detector", layout="centered")
st.title(" AgriScan - Plant Disease Detector")
st.write("Upload a leaf image and choose a model to detect possible plant diseases. Get treatment and care suggestions too!")


model_choice = st.selectbox("Select a model", list(MODEL_PATHS.keys()))
model = load_model(model_choice)


uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Leaf Image", use_column_width=True)

    if st.button(" Predict Disease"):
        image_path = "temp_image.jpg"
        image.save(image_path)

        prediction = predict_plant_disease(image_path, model, CLASS_NAMES)
        st.success(f" **Prediction:** {prediction}")
        st.info(f" Model Used: {model_choice}")

       
        if prediction in TREATMENT_GUIDE:
            guide = TREATMENT_GUIDE[prediction]

            st.markdown("###  Treatment Suggestions")
            st.markdown(f"<b>Natural Treatment:</b> {guide['natural']}", unsafe_allow_html=True)
            st.markdown(f"<b>Chemical Treatment:</b> {guide['chemical']}", unsafe_allow_html=True)
           

            st.markdown("### Plant Care Tips")
            st.markdown(f"{guide['care']}")
        else:
            st.warning(" No treatment guide available for this class yet.")

