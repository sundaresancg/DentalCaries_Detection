# DentalCaries_Detection
A deep learning model to detect the presence of dental caries from a panoramic X-ray image.

Dataset : Panoramic Dental Xray Dataset (source: data.mendeley.com)
116 images originally, 94 caries and 22 non-caries images;
Approx Dimensions = 1200 x 2800


Augmentation : Rotation, Vertical Flip, Horizontal Flip

New dataset after augmentation : 
94 caries and 88 non-caries images

Preprocessing : Images resized to 256x256

Built a Convolutional Neural Network for classification and achieved an accuracy of 94%.

Launched in browser using Streamlit :
Prompts to upload an dental Xray image, 
Returns whether any presence of caries is detected or not, along with the confidence level(%).
