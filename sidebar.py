import streamlit as st

def setup_sidebar():
    with st.sidebar:
        # Sadece bir başlık göster
        st.title("Stacontrol")
        st.markdown("---")
        
      
        
        st.page_link("Anasayfa.py", label="Anasayfa", icon="🏠")
        st.page_link("pages/1_Goreli_Kat_Otelemesi.py", label="Göreli Kat Ötelemesi", icon="📏")
        st.page_link("pages/2_Kolon_Kapasite.py", label="Kolon Eksenel", icon="🏛️")
        st.page_link("pages/4_perde_kapasite.py", label="Perde Eksenel", icon="🛡️")
        st.page_link("pages/5_perde_kesme.py", label="Perde Kesme", icon="🧱")
        st.page_link("pages/6_kiris_kesme.py", label="Kiriş Kesme", icon="⛩")
        st.page_link("pages/metraj_hesaplama.py", label="Metraj", icon="📐")
        st.page_link("pages/3_Hesaplama_Gecmisi.py", label="Kayıtlı Sonuçlar", icon="📜")

        
        # Kullanıcı işlemleri
        st.markdown("---")
        
        # Giriş durumuna göre içerik
        if st.session_state.get("logged_in", False):
            st.write(f"Hoşgeldiniz, {st.session_state['username']}!")
            
            if st.button("Çıkış Yap", key="logout"):
                st.session_state["logged_in"] = False
                st.session_state.pop("username", None)
                cookies = st.session_state.get("cookies")
                if cookies:
                    cookies["logged_in"] = "False"
                    cookies.pop("username", None)
                    cookies.save()
                st.success("Çıkış yapıldı!")
                st.switch_page("pages/üyelik_girisi.py")
        else:
            st.info("Lütfen giriş yapın.")
            st.page_link("pages/üyelik_girisi.py", label="Giriş Yap", icon="🔑")
            st.page_link("pages/kayit_ol.py", label="Kayıt Ol", icon="✍️")