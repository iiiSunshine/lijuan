# 制作聊天界面
import streamlit as st
from langchain_openai import ChatOpenAI


st.title("韩丽娟 ChatOpenAI")

# 构建大模型 智谱
model = ChatOpenAI(
    temperature=0.8,  # 创新性
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="534c7cc9f092ca9b41d4a4c344bc27a8.Jca2Uii4HiEGjIZ9",
)

# 构建缓存保存聊天记录
if "cache" not in st.session_state:
    st.session_state.cache = []
for message in st.session_state.cache:
       with st.chat_message(message['role']):
          st.write(message["content"])

# 创建聊天输入框
problem = st.chat_input("请输入你的问题")

# 确定问题被输入
if problem:
    # 输入问题、调用大模型回答问题、将大模型回答的问题输出
    with st.chat_message("user"):
        st.write(problem)
        st.write("思考中...")
    # 将用户消息添加到缓存
    st.session_state.cache.append({"role": "user", "content": problem})
    # 调用大模型获取回答
    result = model.invoke(problem)
    # 将大模型的回答添加到缓存
    with st.chat_message("assistant"):
        st.write("思考完成...")
        st.write(result.content)
    st.session_state.cache.append({"role": "assistant", "content": result.content})

