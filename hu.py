import streamlit as  st
st.title("Chatbot")
c1,c2,c3,c4=st.columns(4)
with c1:
    st.image("download.jpg",use_column_width=True)
    flag1 = st.button("我是你的宝贝",use_container_width=True)
    if flag1:
        st.switch_page("pages/demo1.py")
with c2:
    st.image("https://iknow-pic.cdn.bcebos.com/10dfa9ec8a136327c1fd81ae838fa0ec08fac71f",use_column_width=True)
    flag2 = st.button("花花",use_container_width=True)
    if flag2:
        st.switch_page("pages/demo1.py")
with c3:
    flag3=st.button("咪咪")
    if flag3:
        st.switch_page("pages/demo1.py")
with c4:
    flag4=st.button("美美")
    if flag4:
        st.switch_page("pages/demo1.py")
with c4:
    flag4=st.button("小黑")
    if flag4:
        st.switch_page("pages/image.py")
