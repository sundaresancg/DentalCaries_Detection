# DentalCaries_Detection
A deep learning model to detect the presence of dental caries from a panoramic X-ray image.

Dataset : Panoramic Dental Xray Dataset (116 images originally, 94 caries and 22 non-caries images, approx dimensions = 1200 x 2800)

Augmentation : Rotate 180, Vertical Flip, Horizontal Flip

New dataset after augmenting : 94 caries and 88 non-caries images

Preprocessing : Images resized to 256x256

Model used : Convolutional Neural Network

Launched in browser using Streamlit :
Prompts to upload an dental Xray image, 
Returns whether any presence of caries is detected or not, along with the confidence level(%).
