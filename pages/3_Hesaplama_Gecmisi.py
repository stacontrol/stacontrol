import streamlit as st
st.set_page_config(
    page_title="Betonarme Hesap Aracı",
    page_icon="🔨",
    layout="wide",
    initial_sidebar_state="collapsed"
)
from sidebar import setup_sidebar

import pandas as pd
from database import get_hesaplamalar
from session_config import init_session_state
from utils import top_right_login



init_session_state()

setup_sidebar()

# Sağ üstte giriş/kayıt butonları
top_right_login()

# Başlık ve stil
st.markdown(
    """
    <h1 style='text-align: center; color: #2c3e50;'>Hesaplama Geçmişi</h1>
    <p style='text-align: center; color: #7f8c8d;'>Kayıtlı hesaplamalarınızı kategoriye göre görüntüleyin.</p>
    """, 
    unsafe_allow_html=True
)

# Oturum kontrolü
if not st.session_state.get("logged_in"):
    st.markdown(
        """
        <div style='text-align: center; padding: 20px; background-color: #fcecdc; border-radius: 10px;'>
            <p style='color: #e74c3c; font-size: 18px;'>Geçmiş kayıtları görüntülemek için lütfen giriş yapınız.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.stop()

# Kullanıcı adını session'dan al
username = st.session_state["username"]

# Kullanıcının hesaplama kayıtlarını getir
df = get_hesaplamalar(username)

if df.empty:
    st.markdown(
        """
        <div style='text-align: center; padding: 20px; background-color: #ecf0f1; border-radius: 10px;'>
            <p style='color: #7f8c8d; font-size: 16px;'>Henüz kayıtlı hesaplama sonucu bulunmuyor.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
else:
    # Kategori seçim kutusu
    kategoriler = ["Kolon Eksenel", "Göreli Kat Ötelemesi" , "Perde Eksenel", "Perde Kesme", "Kiriş Kesme"]
    secilen_kategori = st.selectbox(
        "Bir kategori seçin:",
        kategoriler,
        key="kategori_secim",
        help="Görmek istediğiniz hesaplama kategorisini seçin."
    )

    # Seçilen kategoriye göre filtreleme
    if secilen_kategori == "Kolon Eksenel":
        filtrelenmis_kayitlar = df[df['kaynak_sayfa'] == "kolon_kapasite"]
        hedef_sayfa = "/kolon_kapasite"
    elif secilen_kategori == "Göreli Kat Ötelemesi":
        filtrelenmis_kayitlar = df[df['kaynak_sayfa'] == "goreli_kat_otelemesi"]
        hedef_sayfa = "/goreli_kat_otelemesi"
    elif secilen_kategori == "Perde Eksenel":
        filtrelenmis_kayitlar = df[df['kaynak_sayfa'] == "perde_kapasite"]
        hedef_sayfa = "/perde_kapasite"
    elif secilen_kategori == "Perde Kesme":
        filtrelenmis_kayitlar = df[df['kaynak_sayfa'] == "perde_kesme"]
        hedef_sayfa = "/perde_kesme"
    elif secilen_kategori == "Kiriş Kesme":  # "Kiriş Kesme" olarak güncellendi
        filtrelenmis_kayitlar = df[df['kaynak_sayfa'] == "kiris_kesme"]
        hedef_sayfa = "/kiris_kesme"

    # Filtrelenmiş kayıtları göster
    st.markdown(f"### {secilen_kategori} Hesaplamaları", unsafe_allow_html=True)
    if filtrelenmis_kayitlar.empty:
        st.markdown(
            """
            <div style='padding: 10px; background-color: #ecf0f1; border-radius: 5px;'>
                <p style='color: #7f8c8d;'>Bu kategoride kayıt bulunmuyor.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    else:
        for index, row in filtrelenmis_kayitlar.iterrows():
            saved_id = row['id']
            hesap_tipi = row['hesap_tipi']
            hesap_tarihi = row['hesap_tarihi']
            st.markdown(
                f"""
                <div style='padding: 10px; background-color: #f9f9f9; border-radius: 5px; margin-bottom: 10px;'>
                    <strong>{hesap_tipi}</strong> <br> 
                    <span style='color: #7f8c8d;'>{hesap_tarihi}</span> <br>
                    <a href='{hedef_sayfa}?saved_id={saved_id}' target='_self' style='color: #3498db; text-decoration: none;'>Görüntüle</a>
                </div>
                """, 
                unsafe_allow_html=True
            )