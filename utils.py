import os
import streamlit as st
import hashlib
from streamlit_cookies_manager import EncryptedCookieManager
from database import verify_user
from session_config import init_session_state

# Çerez yöneticisini başlatıyoruz
cookies = EncryptedCookieManager(
    prefix="my_app/",
    password=os.environ.get("COOKIES_PASSWORD", "My secret password"),
)

if not cookies.ready():
    # Çerezlerin yüklenmesini bekle
    st.stop()

# Oturum durumunu initialize ediyoruz.
init_session_state()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def top_right_login():
    """
    Sayfanın sağ üst köşesinde Giriş Yap / Kayıt Ol butonlarını
    veya giriş yapıldıysa 'Hoşgeldiniz' butonu ve 'Çıkış Yap' butonunu yan yana gösterir.
    """
    # Sayfanın üstünde 2 sütun: solda içerik (8 birim), sağda giriş/kayıt (2 birim)
    col1, col2 = st.columns([8, 2])
    
    with col2:
        # Çerezlerde giriş bilgisi varsa session'a aktar
        if cookies.get("logged_in") == "True":
            st.session_state["logged_in"] = True
            st.session_state["username"] = cookies.get("username", "")

        # Kullanıcı giriş yaptıysa:
        if st.session_state.get("logged_in", False):
            # Butonları yan yana yerleştirmek için sütunlar
            welcome_col, logout_col = st.columns([1.5, 1])
            
            with welcome_col:
                # Streamlit buton yerine markdown ile stillendirilmiş metin
                st.markdown(
                    f'<div style="background-color:#4CAF50; color:white; padding:8px 16px; '
                    f'border-radius:5px; text-align:center; font-size:14px; margin:2px 0;">'
                    f'Hoşgeldiniz, {st.session_state["username"]}</div>',
                    unsafe_allow_html=True
                )
            
            with logout_col:
                # Streamlit'in kendi butonu
                if st.button("Çıkış Yap", type="primary", use_container_width=True):
                    st.session_state.clear()
                    cookies["logged_in"] = "False"
                    cookies["username"] = ""
                    cookies.save()
                    st.rerun()

        # Kullanıcı giriş yapmadıysa:
        else:
            # Sütunlar oluştur
            login_col, register_col = st.columns([1, 1])
            
            with login_col:
                # Streamlit butonunu link davranışı için JavaScript kullanarak ayarla
                st.markdown(
                    '<a href="/üyelik_girisi" target="_self" style="text-decoration:none; display:block;">'
                    '<button style="background-color:#4CAF50; color:white; border:none; padding:8px 16px; '
                    'width:100%; border-radius:5px; cursor:pointer; font-size:14px;">'
                    'Giriş Yap</button></a>',
                    unsafe_allow_html=True
                )
            
            with register_col:
                st.markdown(
                    '<a href="/kayit_ol" target="_self" style="text-decoration:none; display:block;">'
                    '<button style="background-color:#008CBA; color:white; border:none; padding:8px 16px; '
                    'width:100%; border-radius:5px; cursor:pointer; font-size:14px;">'
                    'Kayıt Ol</button></a>',
                    unsafe_allow_html=True
                )