import streamlit as  st
st.title("Chatbot")
c1,c2,c3,c4=st.columns(4)
with c1:
    st.image("https://www.bing.com/images/search?view=detailV2&ccid=sVui2uMK&id=904A3833AF0061FB0BEBAEF67273B45CB0BC464A&thid=OIP.sVui2uMKJQEXCXa8JwEuzgHaF7&mediaurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.b15ba2dae30a2501170976bc27012ece%3frik%3dSka8sFy0c3L2rg%26riu%3dhttp%253a%252f%252fpica.nipic.com%252f2007-11-13%252f20071113151715630_2.jpg%26ehk%3dBRDa7mDdHw8mbMxwXQWjsotm4u4BKYczSIwuQfUa2rc%253d%26risl%3d%26pid%3dImgRaw%26r%3d0&exph=819&expw=1024&q=%e5%b0%8f%e7%8b%97%e5%9b%be%e7%89%87&simid=607997718828045398&FORM=IRPRST&ck=44ABEC9E62D51012D2A1DD21808E9140&selectedIndex=16&itb=0",use_column_width=True)
    flag1 = st.button("快来和我聊天",use_container_width=True)
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
