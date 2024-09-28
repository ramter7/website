# Reading Profile
    #with open("Profile.pdf", "rb") as pdf_file:
    #   pdf_bytes = pdf_file.read()

#ICON LOCATION
#icons = "./icons/"
#skills = "./icons/skills/"
#countries = "./icons/countries/"

#invert colors for dark mode?
#filter:invert(100%)

import streamlit as st
#from streamlit_extras.switch_page_button import switch_page #to switch_page without reloading
from base64 import b64encode

#Page config (Title, icon, layout and collapsed sidebar) ⭐ 🌟 📄 🧑‍💻🚀❤️🤖🏂🪧🏠 
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="centered",                      #centered or wide
    initial_sidebar_state="collapsed",      #collapsed sidebar
    #menu_items={                           #menu items in top right
    #    'Get Help': 'https://www.extremelycoolapp.com/help',
    #    'Report a bug': "https://www.extremelycoolapp.com/bug",
    #    'About': "# This is a header. This is an *extremely* cool app!"
    #}
)
# Remove some top padding



st.markdown("""
<style>
    .stAppViewBlockContainer {
        padding-top: 0rem;
    }
</style>
""", unsafe_allow_html=True)


#st.markdown('<style>stVerticalBlock{padding-top:0rem; gap: 0rem;}</style>', unsafe_allow_html=True)

#st.markdown('<style>div.block-container{padding-top:0rem; gap: 0.5rem;}</style>', unsafe_allow_html=True)

def pulseKeyframes():
    st.markdown("""
    <style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }

    .pulse:hover {
        animation: pulse 1s infinite;
    }
    </style>
    """, unsafe_allow_html=True)

    #st.markdown("<h1 class='pulse'>Hover over me!</h1>", unsafe_allow_html=True)

def textHover():
    st.markdown("""
    <style>
    .animated-text:hover {
        color: #FF5733; /* Change color on hover */
        transition: color 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

    #st.markdown("<h1 class='animated-text'>Hover over this text!</h1>", unsafe_allow_html=True)

def imageHover():
    st.markdown("""
    <style>
    .image-hover:hover {
        transform: scale(1.1);
        transition: transform 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

    # HTML to display the image with the hover effect
    #image_html = """
    #<img src="https://via.placeholder.com/300" class="image-hover" style="width: 300px;"/>
    #"""

    #st.markdown(image_html, unsafe_allow_html=True)
    #st.image("./images/avatar.jpg", class_="image-hover", width=300)


def buttonHover():
    st.markdown("""
    <style>
    .stButton > button:hover {
        #background-color: #4CAF50; /* Green */
        color: white;
        transform: scale(1.05);
        transition: all 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

    #st.button("Button")

pulseKeyframes()
textHover()
imageHover()
buttonHover()

# Hide image fullscreen option
def hideImageFullscreenOption():
    hide_img_fs = """
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
    """
    st.markdown(hide_img_fs, unsafe_allow_html=True)

# Header
def header():
    st.write("Header")

# Profile image
def profileImage():
    # Open Profile Image
    with open("./images/avatar.jpg", "rb") as img_file:
        img = "data:image/png;base64," + b64encode(img_file.read()).decode()
    
    # Profile image
    st.write(f"""
    <style>
    @keyframes slowTilt {{
    0%, 100% {{transform: rotate(-5deg);}}
    50% {{transform: rotate(5deg);}}
    }}
    .box img {{
    width: 300px;
    height: 300px;
    border-radius: 50%;
    #animation: slowTilt 2s ease-in-out infinite;
    }}
    </style>
             
    <div style="display: flex; justify-content: center; margin-bottom: 2%">
    <div class="box">
    <img class='pulse' src="{img}" alt="Tassio Steinmann">
    </div>
    </div>
    """, 
    unsafe_allow_html=True)

    # Profile image caption
    st.write(f"""<div class='animated-text' style="font-size: 22px; text-align: center;">Game Developer & Software Engineer</div>""", unsafe_allow_html=True)

# Social Icons
def socialIcons():
    social_icons_data = {
    #"Kaggle": ["https://www.kaggle.com/tassio", "https://www.kaggle.com/static/images/site-logo.svg"],
    "LinkedIn": ["https://www.linkedin.com/in/tassios/", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
    #"GitHub": ["https://github.com/tassio", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
    #"YouTube": ["https://www.youtube.com/tassio", "https://cdn-icons-png.flaticon.com/128/1384/1384060.png"],
    #"Medium": ["https://medium.com/tassio", "https://cdn-icons-png.flaticon.com/128/5968/5968906.png"]
    }
    social_icons_html = [
    f"<a class='pulse' href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'>"
    f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'"
    f" style='width: 25px; height: 25px;'></a>"
    for platform in social_icons_data]
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
    {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

# About
def about():
    st.write(f"""
    <style>
    .waving-hand {{
    animation-name: wave-animation;
    animation-duration: 2.5s;
    animation-iteration-count: infinite;
    transform-origin: 70% 70%;
    display: inline-block;
    }}

    @keyframes wave-animation {{
    0% {{ transform: rotate( 0.0deg) }}
    15% {{ transform: rotate(14.0deg) }}  /* The following five values can be played with to make the waving more or less extreme */
    30% {{ transform: rotate(-8.0deg) }}
    40% {{ transform: rotate(14.0deg) }}
    50% {{ transform: rotate(-4.0deg) }}
    60% {{ transform: rotate(10.0deg) }}
    70% {{ transform: rotate( 0.0deg) }}  /* Reset for the last half to pause */
    100% {{ transform: rotate( 0.0deg) }}
    }}
    </style>
             
    <span class='animated-text' style='font-size: 32px;'>Hello! My name is Tassio Steinmann<span class="waving-hand">👋</span></span>
    """, 
    unsafe_allow_html=True)

    profileImage()
    socialIcons()

# Education
def education():
    st.subheader("Education")
    education = ["🎓Bachelor of Science in Communication & Multimedia Design, Game Design at Hanze University Groningen, Netherlands", "🎓Bachelor of Science in Computer Science (4 semesters) at University of Bern, Switzerland", "🎓Swiss Gymnasium (Grammar school) at Gymnasium Köniz-Lerbermatt, Switzerland"]
    for e in education:
        st.write(e)

# Interests
def interests():
    st.subheader("Interests")
    interests = ["🎮Games", "🕸️Webdesign", "🖥️Coding", "🕹️VR & XR", "💬Languages", "💭Lucid dreaming"]
    for i in interests:
        st.write(i)

# Project style helper
def projectsStyle(projectName, projectImagePath, imageWidth, useColumnWidth):
    with st.container(border = True):
        col1, col2 = st.columns(2)
        with col1:
            st.image(f"./projects/{projectImagePath}/featured.jpg", width=imageWidth, use_column_width=useColumnWidth)
        with col2:
            st.header(projectName)
            if st.button("Details", key=projectName):
                st.success('Clicked!')
                st.switch_page(f"pages/{projectName}.py")

# Projects
def projects():
    st.header("Projects")
    projectsImageWidth = 300
    useColumnWidth = True

    projects =	{
    "VR for Pilots": "vr-for-pilots",
    "Toekomst Coderen": "toekomst-coderen",
    "Become a Virtual Groninger": "become-a-virtual-groninger",
    "Hand Over": "hand-over",
    "Skyline": "skyline",
    "Iroukaz": "iroukaz",
    "PogoSwing": "pogoswing",
    "Defiance": "defiance",
    "Smoking Allowed": "smoking-allowed",
    "Endless Mine": "endless-mine",
    "CarCraft": "carcraft"
    }

    for projectName, projectImagePath in projects.items():
        projectsStyle(projectName, projectImagePath, projectsImageWidth, useColumnWidth)

# Skills
def skills():
    st.header("Skills")
    skillsSVGwidth = 80
    useColumnWidth = False

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("./icons/code.svg", caption="C#", width=skillsSVGwidth, use_column_width=useColumnWidth)
        st.image("./icons/js.svg", caption="Java Script", width=skillsSVGwidth, use_column_width=useColumnWidth)
        #st.image("./icons/git.svg", caption="Git", width=skillsSVGwidth, use_column_width=useColumnWidth)
        
    with col2:
        st.image("./icons/unity.svg", caption="Unity", width=skillsSVGwidth, use_column_width=useColumnWidth)
        st.image("./icons/python.svg", caption="Python", width=skillsSVGwidth, use_column_width=useColumnWidth)
        #st.image("./icons/git.svg", caption="Git", width=skillsSVGwidth, use_column_width=useColumnWidth)

    with col3:
        st.image("./icons/git.svg", caption="Git", width=skillsSVGwidth, use_column_width=useColumnWidth)
        st.image("./icons/html5.svg", caption="HTML&CSS", width=skillsSVGwidth, use_column_width=useColumnWidth)
        #st.image("./icons/git.svg", caption="Git", width=skillsSVGwidth, use_column_width=useColumnWidth)

        #value_if_true if condition else value_if_false

# Languages
def languages():
    st.header("Languages")
    languagesSVGwidth = 80
    useColumnWidth = False

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("./icons/switzerland.svg", caption="Swiss", width=languagesSVGwidth, use_column_width=useColumnWidth)
        st.image("./icons/germany.svg", caption="German", width=languagesSVGwidth, use_column_width=useColumnWidth)
        
    with col2:
        st.image("./icons/catalonia.svg", caption="Catalan", width=languagesSVGwidth, use_column_width=useColumnWidth)
        st.image("./icons/spain.svg", caption="Spanish", width=languagesSVGwidth, use_column_width=useColumnWidth)

    with col3:
        st.image("./icons/united-kingdom.svg", caption="English", width=languagesSVGwidth, use_column_width=useColumnWidth)
        st.image("./icons/france.svg", caption="French", width=languagesSVGwidth, use_column_width=useColumnWidth)

# Accomplishments
def accomplishments():
    st.header("Accomplishments")

    with st.container(border = True):
        st.subheader("Minor: Digital Product Lab ([Hanze University](https://www.hanze.nl/en) Jan 2020 – Jul 2020)")   
        st.write("[SnowLimits](https://snowlimits.nl/) approached us with the idea of making their indoor skiing slopes more exciting with the addition of VR.")
        
    with st.container(border = True):
        st.subheader("Meteor & React Course ([Udemy](https://www.udemy.com/) Jul 2018)")
        st.write("Certificate of Completion, Meteor and React for Realtime Apps.") 

    with st.container(border = True):
        st.subheader("IELTS Academic ([IELTS Official](https://ielts.org/) May 2017)")    
        st.write("IELTS Academic English test.")

    with st.container(border = True):
        st.subheader("Scientific contributor to clinical studies ([Inselspital Bern](https://www.insel.ch/de/) Jan 2015 – Jul 2015)")
        st.write("Visualizing clinical data using graphs and charts created by using the programming language R as well as the JavaScript framework ‘D3’ as part of my civil service for Switzerland.")

# Footer
def footer():
    st.write("© Tassio Steinmann 2024")

# Custom expander CSS 
st.markdown(
    '''
    <style>
    .stExpander {
        background-color: #444444;
        color: white; # Adjust this for expander header color
        border-radius: 25px;
        border: 2px solid white;
    }
    </style>
    ''',
    unsafe_allow_html=True
)
#background-color: black;
#color: white; # Adjust this for expander header color
#border-radius: 25px;
#border: 2px solid white;

# Main
def main():
    hideImageFullscreenOption()

    #navigation()

    #header()

    about()

    with st.expander("Education & Interests", icon="💖"):
        col1, col2 = st.columns(2)
        with col1:
            education()

        with col2:
            interests()

    with st.expander("Projects", icon="🔥"):
        projects()

    with st.expander("Skills", icon="⭐"):
        skills()

    with st.expander("Languagues", icon="🌟"):    
        languages()

    with st.expander("Accomplishments", icon="🚀"):
        accomplishments()

    footer()
    #st.write("##")

if __name__ == "__main__":
    main()