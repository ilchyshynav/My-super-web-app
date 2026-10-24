import streamlit as st

st.set_page_config(page_title="My super-app", page_icon="https://images.icon-icons.com/1465/PNG/512/440monkey_100806.png", layout="wide")

st.title("Nice to see you there!")
tab1, tab2 = st.tabs(["About me", "My instrument"])

with tab1:
    st.header("Introducing the author")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://i.pinimg.com/736x/2c/6f/38/2c6f381205dadef8bf11149c62450acc.jpg", width = 350)
    with col2:
        st.subheader("Hi! I am a future Python Developer!")
        st.write("My name is Valeria Ilchyshyna. I am 13 years old, in the seventh grade of the Lyceum №121. I study in a Small Computer Academy IT-STEP. I also create cool web-sites and learn about Streamlit!")

        with st.container():
            st.info("My contacts")
            st.markdown("- Github: [My profile](https://github.com)")
            st.markdown("- Gmail: val.ilchyshyna@gmail.com")

with tab2:
    st.info("In proccess of making")