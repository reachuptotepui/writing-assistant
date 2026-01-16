import streamlit as st
from streamlit import text_input

from UTILES import generate_xiaohongshu

st.header("爆款小红书AI写作助手")
with st.sidebar:
    deepseek_api_key =text_input("请输入deepseek密钥：",type="password")
    st.markdown("[获取deepseek密钥](https://platform.deepseek.com/)")
theme=st.text_input ("主题")
button=st.button("开始写作")

if button and not deepseek_api_key :
    st.info ("请输入你的deepseekAPI密钥")
    st.stop()
if button and not theme :
    st.info ("请输入主题")
    st.stop()
if button:
    with st.spinner ("AI正在思考中"):
        result=generate_xiaohongshu(theme, deepseek_api_key)
    st.divider()
    left,right=st.columns(2)
    with left:
        st.markdown("##### 小红书标题1")
        st.write(result.titles[0])
        st.markdown("##### 小红书标题2")
        st.write(result.titles[1])
        st.markdown("##### 小红书标题3")
        st.write(result.titles[2])
        st.markdown("##### 小红书标题4")
        st.write(result.titles[3])
        st.markdown("##### 小红书标题5")
        st.write(result.titles[4])
    with right:
        st.markdown("##### 小红书正文")
        st.write(result.content)

    