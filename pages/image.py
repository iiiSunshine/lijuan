
from zhipuai import ZhipuAI
import streamlit as st

st.title("AI绘画")
client = ZhipuAI(api_key="534c7cc9f092ca9b41d4a4c344bc27a8.Jca2Uii4HiEGjIZ9")  # 请填写您自己的APIKey

if "cache" not in st.session_state:
    st.session_state.cache = []
for message in st.session_state.cache:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("assistant"):
            st.image(message["content"], width=200)
description = st.chat_input("请输入图片描述")
if description:
    with st.chat_message("user"):
        st.write(description)
        st.write("正在生成图片")
    st.session_state.cache.append({"role": "user", "content": description})
    try:
        response = client.images.generations(
            model="cogview-3-plus",  # 填写需要调用的模型编码
            prompt=description,
        )
        if response and response.data and len(response.data) > 0:
            image_data = response.data[0]
            if image_data.url:
                with st.chat_message("assistant"):
                    st.image(image_data.url, width=300)
                    # 将图片url写入cache
                st.session_state.cache.append({"role": "assistant", "content": image_data.url})
            else:
                st.write("生成的图片失败")
        else:
            st.write("生成的图片失败")
    except Exception as e:
        st.write(f"发生错误: {e}")
