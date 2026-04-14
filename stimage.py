import streamlit as st
import google.generativeai as genai
from PIL import Image
genai.configure(api_key="")
model=genai.GenerativeModel("gemini-2.5-flash")
st.title("Image Q&A with Gemini")
a=st.file_uploader("Upload an image", type=["jpg", "jpeg", "png","webp"])
prompt=st.text_input("Enter your question about the image:")
c="""you are a wildfire analysis expert. Analyze the satellite images and provide me :
Analyze wildfire satellite images to map the burn perimeter and estimate the affected forest area in hectares.
1. Burn perimeter mapping
2. Estimation of affected forest area in hectares
3. Analysis of fire intensity and spread patterns
4. Identification of potential causes and contributing factors
5. Recommendations for wildfire prevention and mitigation strategies
If the image is not a wildfire satellite image, reply exactly: 'Sorry, I can only analyze wildfire satellite images.'"""
if st.button('submit'):
    img=Image.open(a)
    response=model.generate_content([prompt,img])
    st.write(response.text)
