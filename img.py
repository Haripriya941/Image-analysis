import google.generativeai as genai
from PIL import Image
img=Image.open(r"C:\Users\mguna\Downloads\image.avif")
genai.configure(api_key="AIzaSyAMbYMsot49vBAMKoDMddEofRiNyJtKYzk")
model=genai.GenerativeModel("gemini-2.5-flash")
prompt=input("Enter the Questions:")            
response=model.generate_content([prompt,img])        
print(response.text)