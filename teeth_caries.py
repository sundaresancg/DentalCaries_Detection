import cv2
import numpy as np
from PIL import Image
import streamlit as st
import sklearn 
from skimage import transform
from tensorflow.keras.models import load_model

model1 = load_model('DentalCaries_Detection/caries_model1.h5')

st.subheader(':orange[Dental Caries Detection]')

uploaded_file = st.file_uploader("Upload a dental panoramic xray image(.png)", type=['png','jpg'])

if uploaded_file is not None:
    image_file = Image.open(uploaded_file)

    img_array = np.array(image_file).astype('float32')/255

    img_res = transform.resize(img_array, (256,256,3))

    img_res = np.expand_dims(img_res, axis=0)


    st.image(image_file, caption='uploaded panoramic dental Xray', use_column_width=True)

    st.write("...")

    pred = model1.predict(img_res)

    if round(pred[0][0]) == 1:  
        st.subheader("No caries detected")
        confidence = pred[0][0]*100
    else:
        st.subheader("Caries presence detected")
        confidence = 100 - (pred[0][0]*100)
    
    st.write("Confidence Level : ", confidence, " %")

else:

    st.write("Waiting for Upload...")
