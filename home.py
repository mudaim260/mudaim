
import streamlit as st

st.set_page_config(
    page_title="my profile|syarifah",
    page_icon="🧕",
    layout="wide"
)
st.title("WELCOME TO MY PORTFOLIO 🧕")

st.sidebar.success("PORTOFOLIO")

from PIL import Image

st.title('mySelf👩‍🎓')


image = Image.open('me.jpg')
st.image(image, width=300)
st.subheader("NAMA : SYARIFAH MUDAIM")
st.caption("NIM : 0402201079 ")
st.markdown('''
            - Tempat Tanggal Lahir : Brebes, 02 April 2002
            - Alamat               : Kubangsari - Ketanggungan - Brebes
            - Hobi                 : Tour and MaTour
            - Cita-cita            : Masih difikirkan 
            - Hal yang disukai     : Menyangkal
            - Status               : Nasib hamba Allah
            """
            ''')


st.markdown('## Tentang Saya', unsafe_allow_html=True)
st.info('''
       

st.header("*THANK YOU*")


