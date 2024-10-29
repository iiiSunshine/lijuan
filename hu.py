import streamlit as  st
st.title("Chatbot")
c1,c2,c3,c4=st.columns(4)
with c1:
    st.image("download.jpg",use_column_width=True)
    flag1 = st.button("我是你的宝贝",use_container_width=True)
    if flag1:
        st.switch_page("pages/demo1.py")
with c2:
    st.image("https://pic2.zhimg.com/v2-e9fe02911227e55327de9de4572c1221_r.jpg",use_column_width=True)
    flag2 = st.button("花花",use_container_width=True)
    if flag2:
        st.switch_page("pages/demo1.py")
with c3:
     st.image("https://iknow-pic.cdn.bcebos.com/b64543a98226cffc2585392fab014a90f703ea84",use_column_width=True)
    flag3=st.button("咪咪",use_container_width=True)
    if flag3:
        st.switch_page("pages/demo1.py")
with c4:
     st.image("https://img1.baidu.com/it/u=1493092819,2012763429&fm=253&fmt=auto&app=120&f=JPEG?w=800&h=800",use_column_width=True)
    flag4=st.button("美美",use_container_width=True)
    if flag4:
        st.switch_page("pages/demo1.py")
with c4:
     st.image("https://img2.baidu.com/it/u=3086518359,3242772898&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=667",use_column_width=True)
    flag4=st.button("小黑",use_container_width=True)
    if flag4:
        st.switch_page("pages/image.py")
