import streamlit as  st
st.title("Chatbot")
c1,c2,c3,c4=st.columns(4)
with c1:
    flag1 = st.button("初级")
    if flag1:
        st.switch_page("pages/demo1.py")
with c2:
    flag2 = st.button("进阶1")
    if flag2:
        st.switch_page("pages/demo1.py")
with c3:
    flag3=st.button("进阶2")
    if flag3:
        st.switch_page("pages/demo1.py")
with c4:
    flag4=st.button("进阶3")
    if flag4:
        st.switch_page("pages/demo1.py")
with c4:
    flag4=st.button("图片")
    if flag4:
        st.switch_page("pages/image.py")