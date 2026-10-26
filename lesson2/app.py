import streamlit as st

st.set_page_config(page_title="My super-app", page_icon="https://images.icon-icons.com/1465/PNG/512/440monkey_100806.png", layout="wide")

st.title("Nice to see you there!")
tab1, tab2, tab3 = st.tabs(["About me", "My instrument", "Useful referencs"])

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

with tab3:
    st.header("Feel free to use them!")
    col1, col2 = st.columns([1, 2])
    with col1:
            st.markdown("- Chat GPT: [Helps you with arranging your working time and making notes](https://www.google.com/aclk?sa=L&pf=1&ai=DChsSEwi9wLauydeXAxXtyrEHHUMtCd0YACICCAEQABoCbHI&co=1&ase=2&gclid=EAIaIQobChMIvcC2rsnXlwMV7cqxBx1DLQndEAAYASAAEgIdsPD_BwE&cid=CAASugHkaPzCrbqaCTnXDeiVQ0uu6WWvqrerfSE6getTBQMkteUhoFScDCdAIMFZVoZ-1-L0N4TP-Sc8we4xeVw38d34ywCseKaUPAwGQwQsYBrQBXlRPZxeSKvyAKCqcrG1ras8U9ZXsW84YxVvu4HnqvEwveHFVyd2XnaDFVy___KddCSL_u_K8_xQBgN806a0HI6fhe0Vsg6i01osBaL1jVJME3jX2UdT0anKXe9N74B40aSRzOXpgeXgb2k&cce=2&category=acrcp_v1_32&sig=AOD64_3e2jfViaFy45S4VdiXttjkNRMDkw&q&nis=4&adurl=https://chatgpt.com?utm_source%3Dgoogle%26utm_medium%3Dpaid_search%26c_id%3D22472177954%26c_agid%3D175689713502%26c_crid%3D747938588585%26c_kwid%3Dkwd-1927051708782%26c_ims%3D%26c_pms%3D9197953%26c_nw%3Dg%26c_dvc%3Dc%26gad_source%3D1%26gad_campaignid%3D22472177954%26gbraid%3D0AAAAA-I0E5cBEtJbnhAaHmAqIXT0b_Pq3%26gclid%3DEAIaIQobChMIvcC2rsnXlwMV7cqxBx1DLQndEAAYASAAEgIdsPD_BwE&ved=2ahUKEwj2u7CuydeXAxVhEhAIHYU5Pd4Q0Qx6BAgOEAE)")
            st.markdown("- Pi-stacja: [Youtube channel with lots of useful videos on different themes](https://m.youtube.com/@pistacja-ua)")
            st.markdown("- GeoGebra: [Helps you to understand math better. There are both Algebra and Geometry](https://www.geogebra.org/)")
            st.markdown("- Quizlet: [Can create and share tests or mini-games that help learning.](https://quizlet.com/ru)")

    with col2:
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQROq6TUn52DjU4SyVdDFLvgvCEvPHdrDyh3eOw7guNzw&s", width = 60)
            st.image("https://yt3.googleusercontent.com/ivn4pspZtCCoqHHoJbcCI_zYtNwfdKeKs2QJ0WTLeie6KZd2bie-Eb6WHYC2bBXorERc79bJmEM=s900-c-k-c0x00ffffff-no-rj", width = 60)
            st.image("https://play-lh.googleusercontent.com/4t7gA_OjypYytPFasTf_npykgPOBnjegJLLK0SeR0EBQWbv6FdXoNXBW7vN91_P7tMWTp6Xp4uFXLKL1AZVtmg", width = 60)
            st.image("https://play-lh.googleusercontent.com/7BXrWf3G_EtynmKAl54Gi8Dljx_0U1auRSzvEYEUZfUdUncrJ7H49ayPbVCw4DwM4tY", width = 60)