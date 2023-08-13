import streamlit as st

def main():
    st.title("多页面应用演示")

    # 显示导航菜单
    page = st.sidebar.selectbox("选择页面", ("页面1", "页面2"))

    # 根据页面选择显示不同的内容
    if page == "页面1":
        display_page1()
    elif page == "页面2":
        display_page2()

def display_page1():
    st.header("页面1")
    st.write("这是页面1的内容")
    # 添加页面1的其他内容和交互元素

def display_page2():
    st.header("页面2")
    st.write("这是页面2的内容")
    # 添加页面2的其他内容和交互元素

if __name__ == "__main__":
    main()