import streamlit as st
import google.generativeai as genai
from PIL import Image
import streamlit as st
# Custom CSS for a professional, "edgy" look
st.markdown("""
    <style>
    /* 1. Main background - Deep charcoal gradient */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #ffffff;
    }
    
    /* 2. Glassmorphism effect for the sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* 3. Edgy buttons - Neon border and hover glow */
    div.stButton > button:first-child {
        background-color: transparent;
        color: #00f2fe;
        border: 2px solid #00f2fe;
        border-radius: 10px;
        transition: all 0.3s ease-in-out;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #00f2fe;
        color: #000000;
        box-shadow: 0 0 20px #00f2fe;
    }
    
    /* 4. Professional Headings */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        letter-spacing: -1px;
        background: -webkit-linear-gradient(#eee, #333);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Setup API Key (Get one at aistudio.google.com)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
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