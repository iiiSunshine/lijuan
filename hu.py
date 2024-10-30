import streamlit as  st
st.title("Chatbot")
c1,c2,c3,c4=st.columns(4)
with c1:
    st.image("https://c-ssl.duitang.com/uploads/blog/202204/02/20220402195223_815f6.jpg",use_column_width=True)
    flag1 = st.button("我是你的宝贝",use_container_width=True)
    if flag1:
        st.switch_page("pages/demo1.py")
with c2:
    st.image("https://th.bing.com/th/id/OIP.Rhil-o1qJ42UjFWcTziO7gAAAA?w=400&h=400&rs=1&pid=ImgDetMain",use_column_width=True)
    flag2 = st.button("花花",use_container_width=True)
    if flag2:
        st.switch_page("pages/demo2.py")
with c3:
    #flag3=st.button("小白")
    #if flag3:
        st.switch_page("pages/demo1.py")
with c4:
    #flag4=st.button("美美")
    #if flag4:
        #st.switch_page("pages/demo1.py")
with c4:
    #flag4=st.button("图片")
    #if flag4:
        vst.switch_page("pages/image.py")
