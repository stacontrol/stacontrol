import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import comtypes.client
import os

# Page configuration (kept at the top as required)
logo_path = 'C:/Users/Emin/Desktop/deneme2/assets/logo.png'

st.set_page_config(
    page_title="Stacontrol",
    page_icon=logo_path,  # Dosya yolunu string olarak kullanıyoruz
    layout="wide",
    initial_sidebar_state="collapsed"
)

from sidebar import setup_sidebar
from utils import top_right_login
from session_config import init_session_state
ShowSidebarNavigation = False
# Initialize session state
init_session_state()

setup_sidebar()

# Right-top login/register buttons
top_right_login()

# ETABS Bağlantısı için fonksiyon
def get_active_etabs_filename():
    try:
        # COM nesnelerini başlat
        comtypes.CoInitialize()
        
        # Doğrudan aktif ETABS nesnesini al
        etabs_object = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
        SapModel = etabs_object.SapModel
        
        # Get file path
        file_path = SapModel.GetModelFilename()
        if file_path:
            # Sadece dosya adını al (yolunu değil)
            file_name = os.path.basename(file_path)
            return file_name
        else:
            return None
    except Exception as e:
        return None

# Aktif ETABS dosyası adını al
active_etabs_file = get_active_etabs_filename()

# Enhanced CSS styles for a professional look
st.markdown("""
    <style>
    /* Reset default Streamlit padding */
    .stApp {
        padding-top: 0 !important;
        background: linear-gradient(135deg, #f0f4f8 0%, #e2e8f0 100%);
        min-height: 100vh;
    }

    /* General typography */
    body {
        font-family: 'Inter', sans-serif;
        color: #1e293b;
    }

    /* Header styling */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #1e293b;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 5px;
        letter-spacing: -1px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px; /* Space between image and text */
    }
    .subtitle {
        font-size: 16px;
        color: #64748b;
        text-align: center;
        max-width: 900px;
        margin: 0 auto 30px auto;
        line-height: 1.5;
    }
    
    /* ETABS file info */
    .etabs-file-info {
        font-size: 14px;
        color: #3b82f6;
        text-align: center;
        font-weight: 600;
        background-color: rgba(59, 130, 246, 0.1);
        padding: 6px 12px;
        border-radius: 6px;
        margin: 0 auto 20px auto;
        max-width: 800px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .etabs-file-icon {
        margin-right: 8px;
    }

    /* Card styling */
    .card {
        padding: 20px;
        border-radius: 12px;
        background: #ffffff;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
        text-align: center;
        width: 100%;
        height: 220px;
        margin-left: auto;
        margin-right: auto;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    }
    .card-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 8px;
        color: #1e293b;
    }
    .card-text {
        color: #64748b;
        font-size: 14px;
        line-height: 1.4;
        margin-bottom: 15px;
        flex-grow: 1;
    }
    .icon {
        font-size: 32px;
        margin-bottom: 10px;
        color: #3b82f6;
        transition: transform 0.3s ease;
    }
    .card:hover .icon {
        transform: scale(1.15);
    }

    /* Button styling */
    .hesapla-button, .analiz-button {
        background: linear-gradient(90deg, #3b82f6 0%, #60a5fa 100%);
        color: white !important;
        padding: 8px 20px;
        border-radius: 6px;
        border: none;
        text-decoration: none;
        font-size: 14px;
        font-weight: 600;
        display: block;
        transition: background 0.3s ease, transform 0.2s ease;
        width: 150px;
        margin: 0 auto;
        text-align: center;
    }
    .hesapla-button:hover, .analiz-button:hover {
        background: linear-gradient(90deg, #2563eb 0%, #3b82f6 100%);
        transform: translateY(-2px);
    }
    .coming-soon {
        color: #94a3b8;
        font-style: italic;
        font-size: 14px;
        margin-top: 15px;
    }

    /* Footer styling */
    .footer {
        text-align: center;
        color: #64748b;
        padding: 30px 0;
        font-size: 14px;
        border-top: 1px solid #e2e8f0;
        margin-top: 40px;
        background: #ffffff;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .main-title {
            font-size: 32px;
        }
        .subtitle {
            font-size: 15px;
        }
        .card {
            height: auto;
            min-height: 180px;
            padding: 15px;
        }
        .card-title {
            font-size: 18px;
        }
        .card-text {
            font-size: 13px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Function to convert image to base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

# Load the images with PIL using the updated paths
image = Image.open('C:/Users/Emin/Desktop/deneme2/assets/goreli_kat_otelemesi.png')
image2 = Image.open('C:/Users/Emin/Desktop/deneme2/assets/kolon_kapasite.png')
image3 = Image.open('C:/Users/Emin/Desktop/deneme2/assets/perde_kapasite.png')
image4 = Image.open('C:/Users/Emin/Desktop/deneme2/assets/perde_kesme.png')
image5 = Image.open('C:/Users/Emin/Desktop/deneme2/assets/kiris_kesme.png')
image6 = Image.open('C:/Users/Emin/Desktop/deneme2/assets/metraj.png')
# Load the new image for the title
title_image = Image.open('C:/Users/Emin/Desktop/deneme2/assets/logo.png')  

# Convert each image to base64
img_base64 = image_to_base64(image)
img_base64_2 = image_to_base64(image2)
img_base64_3 = image_to_base64(image3)
img_base64_4 = image_to_base64(image4)
img_base64_5 = image_to_base64(image5)
img_base64_6 = image_to_base64(image6)
title_img_base64 = image_to_base64(title_image)

# Main Title and Subtitle
st.markdown(f"""
    <h1 class='main-title'>
        <img src="{title_img_base64}" style="width: 50px; height: 50px; vertical-align: middle;"> Stacontrol
    </h1>
""", unsafe_allow_html=True)

# ETABS dosya bilgisi gösterimi (başlığın hemen altında)
if active_etabs_file:
    st.markdown(f"""
        <div class='etabs-file-info'>
            <span class='etabs-file-icon'>🟢</span>  {active_etabs_file} bağlandınız betonarme yapı elemanlarınızı hızlı ve güvenilir bir şekilde analiz edin. 
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
        <div class='etabs-file-info'>
            <span class='etabs-file-icon'>⚠️</span> ETABS açık değil veya bağlantı kurulamadı
        </div>
    """, unsafe_allow_html=True)

# Cards (First Row)
col1, col2, col3 = st.columns([1, 1, 1], gap="medium")

with col1:
    st.markdown(f"""
        <div class="card">
            <div>
                <img src="{img_base64}" style="width: 50px; height: 50px; margin-bottom: 5px; transition: transform 0.3s ease;" class="icon">
                <div class="card-title">Göreli Kat Ötelemesi</div>
                <div class="card-text">Göreli kat ötelemesi kontrolü</div>
            </div>
            <a href="/goreli_kat_otelemesi" target="_self" class="analiz-button">Analiz Yap</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="card">
            <div>
                <img src="{img_base64_2}" style="width: 50px; height: 50px; margin-bottom: 5px; transition: transform 0.3s ease;" class="icon">
                <div class="card-title">Kolon Eksenel</div>
                <div class="card-text">Kolon eksenel kuvvet konrolü.</div>
            </div>
            <a href="/kolon_kapasite" target="_self" class="analiz-button">Analiz Yap</a>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="card">
            <div>
                <img src="{img_base64_3}" style="width: 50px; height: 50px; margin-bottom: 5px; transition: transform 0.3s ease;" class="icon">
                <div class="card-title">Perde Eksenel</div>
                <div class="card-text">Perde eksenel kuvvet kontrolü</div>
            </div>
            <a href="/perde_kapasite" target="_self" class="analiz-button">Analiz Yap</a>
        </div>
    """, unsafe_allow_html=True)

# Cards (Second Row)
col4, col5, col6 = st.columns([1, 1, 1], gap="small")

with col4:
    st.markdown(f"""
        <div class="card">
            <div>
                <img src="{img_base64_4}" style="width: 50px; height: 50px; margin-bottom: 5px; transition: transform 0.3s ease;" class="icon">
                <div class="card-title">Perde Kesme</div>
                <div class="card-text">Perde kesme kuvveti analizi ve kontrolleri</div>
            </div>
            <a href="/perde_kesme" target="_self" class="analiz-button">Analiz Yap</a>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
        <div class="card">
            <div>
                <img src="{img_base64_5}" style="width: 50px; height: 50px; margin-bottom: 5px; transition: transform 0.3s ease;" class="icon">
                <div class="card-title">Kiriş Kesme</div>
                <div class="card-text">Kiriş kesme kuvveti hesaplamaları</div>
            </div>
            <a href="/kiris_kesme" target="_self" class="analiz-button">Analiz Yap</a>
        </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown(f"""
        <div class="card">
            <div>
                <img src="{img_base64_6}" style="width: 50px; height: 50px; margin-bottom: 5px; transition: transform 0.3s ease;" class="icon">
                <div class="card-title">Metraj</div>
                <div class="card-text">Yapı elemanları için metraj tahminleri</div>
            </div>
            <a href="/metraj_hesaplama" target="_self" class="analiz-button">Analiz Yap</a>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        © 2025 Stacontrol | eminsade108@gmail.com
    </div>
""", unsafe_allow_html=True)