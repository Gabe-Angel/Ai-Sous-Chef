import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Setup API Key (Get one at aistudio.google.com)
genai.configure(api_key="AIzaSyC3bQ_r5hxMp0D_ES6rOoV7b7gjMUlvexo")
model = genai.GenerativeModel('gemini-2.5-flash-lite')

st.set_page_config(page_title="AI Sous Chef", page_icon="🍳")
st.title("🍳 AI Sous Chef")
st.write("Take a photo of your ingredients, and I'll tell you what to cook!")

# 2. Image Upload / Camera Input
img_file = st.camera_input("Snap a photo of your fridge or pantry")

if img_file:
    img = Image.open(img_file)
    st.image(img, caption="Ingredients detected!", use_container_width=True)
    
    with st.spinner('Analyzing your ingredients...'):
        # 3. Prompting the AI
        prompt = """
        Identify all the food ingredients in this image. 
        Then, suggest 3 creative recipes I can make using these items. 
        Include:
        1. Recipe Name
        2. Estimated prep time
        3. Simple step-by-step instructions
        """
        
        response = model.generate_content([prompt, img])
        
        st.markdown("---")
        st.subheader("👨‍🍳 Recipe Suggestions")
        st.write(response.text)
