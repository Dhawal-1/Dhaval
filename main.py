import streamlit as st
import google.generativeai as genai
import time

apikey = st.secrets["GOOGLE_API_KEY"]

st.set_page_config(layout="centered",page_title="Dhaval")
st.write("###")
    
@st.experimental_dialog("ChatBot Answer",width="large")
def response_dialog(res):
    st.write(response.text)
    if st.button("Close"):
        st.rerun()
    
#Load CSS
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)


# <-------------------- A.I -------------------->

genai.configure(api_key=apikey)
model = genai.GenerativeModel('gemini-1.5-flash')

persona = """
    You are Dhaval A.I Chabot and you are created by Dhaval. You help people answer their questions about your self that is Dhaval
    Answer as if you are responding .dont answer in secound or third person.
    If you don't know the answer, you simply say "That's a secret !".

    Here is more info about Dhaval:
    Dhaval Patil is a youngest programeer and student. He is a Python developer.
    Dhaval lives in India.
    Dhaval's learn Computer Vision from Murtaza's Workshop - Robotics and AI YouTube Channel.
    He currently studying in 12th standard.
    Dhaval do various things like Learning new things, Developing new things, etc.
    Dhaval's hobby is Making Music..
    Dhaval is currently 17 years old.

    Dhaval's email adress : dhavalpatil876@gmail.com

"""


# <-------------------- NAVBAR -------------------->
st.markdown("""
    <div class="nav">
        <a href="#home" class="bi bi-person">Home</a>
        <a href="#chatbot" class="bi bi-robot">ChatBot</a>
        <a href="#projects" class="bi bi-code-slash">Projects</a>
        <a href="#contact" class="bi bi-chat">Contact</a>    
                       
    </div>

""",unsafe_allow_html=True)


# <-------------------- ABOUT -------------------->
st.write(" ")

st.subheader("Hey there! :wave:",anchor="home")
st.title("Welcome To My Portfolio!",anchor=False)
st.title("I am :blue[Dhaval Patil] !",anchor=False)
st.subheader("A youngest Python developer and student.",anchor=False)

st.divider()

st.title("My Skills")
st.slider("Python",0,100,90)
st.slider("Computer Vision",0,100,85)
st.slider("C++",0,100,75)
st.slider("Game Dev",0,100,69)
st.slider("Web Dev",0,100,60)
st.slider("Music",0,100,50)

st.divider()

# <-------------------- ChatBot -------------------->
st.title("Dhaval's ChatBot",anchor="chatbot")

question = st.text_input("Ask me anything",placeholder="Type your question here...")
if st.button("Ask",help="Ask question to Dhaval's ChatBot",use_container_width=1):
    try:
        question = persona + "Here is the question" + question
        response = model.generate_content(question)
        response_dialog(response)
    except:
        st.toast("Please Wait Some Time... The A.I needs cooldown !",icon = '🥶')
        time.sleep(3)
    

st.divider()

# <-------------------- Projects -------------------->

st.title("Projects",anchor="projects")
col2,col3,col4 = st.columns([2,2,2])

with col2:
    with st.container(border=True):
        st.header("Sticker Genrator")
        if st.button("View Project"):
            st.switch_page("pages/Sticker_Genrator.py")

with col3:
    with st.container(border=True):
        st.header("Blender Addons")
        st.link_button("Open Website","https://blendermarket.com/creators/flowcreations")

with col4:
    with st.container(border=True):
        st.header("Photo Editor")
        if st.button("View Project",key=1):
            st.switch_page("pages/photo_editor.py")

st.divider()

# <-------------------- Contact -------------------->
st.title("Contact Me",anchor="contact")
st.subheader("dhavalpatil876@gmail.com")

st.write("")

st.markdown("""
    <div class="social">
        <a href="https://github.com/Dhawal-1"><i class="bi bi-github" ></i></a>
        <a href="https://instagram.com/dhaval1_0"><i class="bi bi-instagram"></i></a>
    </div>
            
""",unsafe_allow_html=True)

st.subheader("",divider="rainbow")
