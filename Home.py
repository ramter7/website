import streamlit as st
import time
import datetime
from base64 import b64encode

# Page config (Title, icon, layout, collapsed sidebar and menu) ⭐🌟📄🧑‍💻🚀❤️🤖🏂🪧🏠 
st.set_page_config(
    page_title='Home',
    page_icon='🏠',
    layout='centered',                      #centered or wide
    initial_sidebar_state='collapsed',      #collapsed sidebar
    #menu_items={                           #menu items in top right
    #    'Get Help': 'https://www.extremelycoolapp.com/help',
    #    'Report a bug': 'https://www.extremelycoolapp.com/bug',
    #    'About': '# This is a header. This is an *extremely* cool app!'
    #}
)

# Remove some top padding
def removeTopPadding():
    st.html("""
        <style>
            .stAppViewBlockContainer {
                padding-top: 3rem;
            }
        </style>
    """)

# Pulse animation on hover
def pulseHover():
    st.html("""
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
    """)

    #st.markdown('<h1 class='pulse'>Hover over me!</h1>', unsafe_allow_html=True)

# Color change on hover
def textHover():
    st.html("""
        <style>
            .text-hover:hover {
                color: #FF5733; /* Change color on hover */
                #transform: scale(1.1);
                transition: all 0.3s ease;
            }
        </style>
    """)

    #st.markdown('<h1 class='text-hover'>Hover over this text!</h1>', unsafe_allow_html=True)

# Image zoom on hover
def imageHover():
    st.html("""
        <style>
            .image-hover:hover {
                transform: scale(1.1);
                transition: transform 0.3s ease;
            }
        </style>
    """)

    st.html("""
        <style>
            img {
                #border-radius: 5px;
            }

            img:hover {
                transform: scale(1.05);
                transition: transform 0.3s ease;
            }
        </style>
    """)

    #imageHtml = "<img src='https://via.placeholder.com/300' class='image-hover' style='width: 300px;'/>"
    #st.markdown(imageHtml, unsafe_allow_html=True)

# Button zoom on hover
def buttonHover():
    st.html("""
        <style>
            .stButton > button:hover {
                transform: scale(1.05);
                transition: transform 0.3s ease;
            }
        </style>
    """)

    #st.button('Button')

# Hide image fullscreen option
def hideImageFullscreenOption():
    st.html("""
        <style>
            button[title='View fullscreen']{visibility: hidden;}
        </style>
    """)

def aboutText():
    st.html(f"""
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
                15% {{ transform: rotate(14.0deg) }}
                30% {{ transform: rotate(-8.0deg) }}
                40% {{ transform: rotate(14.0deg) }}
                50% {{ transform: rotate(-4.0deg) }}
                60% {{ transform: rotate(10.0deg) }}
                70% {{ transform: rotate( 0.0deg) }}
                100% {{ transform: rotate( 0.0deg) }}
            }}
        </style>        
    """)

    st.write(f"""
        <div style='text-align: center; padding-bottom: 2%;'>
            <span class='text-hover' style='font-size: 32px; text-align: center;'>Hello! My name is Tassio Steinmann<span class='waving-hand'>👋</span></span>
        </div>
    """, unsafe_allow_html=True)

def profileImg():
    with open('./images/avatar.jpg', 'rb') as imgFile:
        img = 'data:image/png;base64,' + b64encode(imgFile.read()).decode()

    st.html(f"""
        <style>
            .box img {{
                width: 240px;
                border-radius: 50%;
            }}
        </style>        
    """)

    st.write(f"""      
        <div style='display: flex; justify-content: center; margin-bottom: 2%'>
            <div class='box'>
                <img class='pulse' src='{img}' alt='Tassio Steinmann'>
            </div>
        </div>
    """, unsafe_allow_html=True)

def profileImgCaption():
    st.write(f"""<div class='text-hover' style='font-size: 24px; text-align: center;'>Game Developer & Software Engineer</div>""", unsafe_allow_html=True)  

# Profile image
def profileImage():
    profileImg()
    profileImgCaption()

# Social Icons
def socialIcons():
    socialIconsData = {
        'LinkedIn': ['https://www.linkedin.com/in/tassios/', 'https://cdn-icons-png.flaticon.com/128/3536/3536505.png'],
        #'Kaggle': ['https://www.kaggle.com/tassio', 'https://www.kaggle.com/static/images/site-logo.svg'],
        #'GitHub': ['https://github.com/tassio', 'https://cdn-icons-png.flaticon.com/128/5968/5968866.png'],
        #'YouTube': ['https://www.youtube.com/tassio', 'https://cdn-icons-png.flaticon.com/128/1384/1384060.png'],
        #'Medium': ['https://medium.com/tassio', 'https://cdn-icons-png.flaticon.com/128/5968/5968906.png']
    }
    
    socialIconsHtml = [f"""
        <a class='pulse' href='{socialIconsData[platform][0]}' target='_blank' style='margin-right: 10px;'>
        <img class='social-icon' src='{socialIconsData[platform][1]}' alt='{platform}' style='width: 25px; height: 25px;'></a>
    """ for platform in socialIconsData]

    st.write(f"""
        <div style="display: flex; justify-content: center; margin-bottom: 2%;">
            {''.join(socialIconsHtml)}
        </div>
    """, unsafe_allow_html=True)

# Education
def education():
    st.subheader('Education')
    education = ['🎓Bachelor of Science in Communication & Multimedia Design, Game Design at Hanze University Groningen, Netherlands', '🎓Bachelor of Science in Computer Science (4 semesters) at University of Bern, Switzerland', '🎓Swiss Gymnasium (Grammar school) at Gymnasium Köniz-Lerbermatt, Switzerland']
    for e in education:
        st.write(e)

# Interests
def interests():
    st.subheader('Interests')
    interests = ['🎮Games', '🕸️Webdesign', '🖥️Coding', '🕹️VR & XR', '💬Languages', '💭Lucid dreaming']
    for i in interests:
        st.write(i)

# Project style helper
def projectsStyle(projectName, imageWidth, useColumnWidth):
    with st.container(border = True):
        col1, col2 = st.columns(2)
        with col1:
            st.image(f'./projects/{projectName}/featured.jpg', width=imageWidth, use_column_width=useColumnWidth)
        with col2:
            st.header(projectName)
            if st.button('Details', type='primary', key=projectName):
                st.success('Clicked!')
                st.switch_page(f'pages/{projectName}.py')

# Projects
def projects():
    st.header('Projects')
    projectsImageWidth = 300
    useColumnWidth = True

    projects =	{
        'VR for Pilots',
        'Toekomst Coderen AR',
        'Become a Virtual Groninger 2D',
        'Hand Over VR',
        'Skyline VR',
        'Iroukaz 3D',
        'PogoSwing 3D',
        'Defiance 2D',
        'Smoking Allowed VR',
        'Endless Mine 2D',
        'CarCraft 3D'
    }
    for projectName in projects:
        projectsStyle(projectName, projectsImageWidth, useColumnWidth)

# Skills
def skills():
    st.header('Skills')
    skillsSVGwidth = 100
    useColumnWidth = False

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('./icons/code.svg', caption='C#', width=skillsSVGwidth, use_column_width=useColumnWidth)
        st.image('./icons/js.svg', caption='Java Script', width=skillsSVGwidth, use_column_width=useColumnWidth)
        
    with col2:
        st.image('./icons/unity.svg', caption='Unity', width=skillsSVGwidth, use_column_width=useColumnWidth)
        st.image('./icons/python.svg', caption='Python', width=skillsSVGwidth, use_column_width=useColumnWidth)

    with col3:
        st.image('./icons/git.svg', caption='Git', width=skillsSVGwidth, use_column_width=useColumnWidth)
        st.image('./icons/html5.svg', caption='HTML&CSS', width=skillsSVGwidth, use_column_width=useColumnWidth)

# Languages
def languages():
    st.header('Languages')
    languagesSVGwidth = 100
    useColumnWidth = False

    col1, col2, col3 = st.columns(3)
    with st.container():
        with col1:
            st.image('./icons/switzerland.svg', caption='Swiss', width=languagesSVGwidth, use_column_width=useColumnWidth)
            st.image('./icons/germany.svg', caption='German', width=languagesSVGwidth, use_column_width=useColumnWidth)
            
        with col2:
            st.image('./icons/catalonia.svg', caption='Catalan', width=languagesSVGwidth, use_column_width=useColumnWidth)
            st.image('./icons/spain.svg', caption='Spanish', width=languagesSVGwidth, use_column_width=useColumnWidth)

        with col3:
            st.image('./icons/united-kingdom.svg', caption='English', width=languagesSVGwidth, use_column_width=useColumnWidth)
            st.image('./icons/france.svg', caption='French', width=languagesSVGwidth, use_column_width=useColumnWidth)

# Accomplishments
def accomplishments():
    st.header('Accomplishments')
    containerBorder = True
    containerDivider = True

    with st.container(border=containerBorder):
        st.subheader('Minor: Digital Product Lab ([Hanze University](https://www.hanze.nl/en) Jan 2020 – Jul 2020)', divider=containerDivider) 
        st.write('[SnowLimits](https://snowlimits.nl/) approached us with the idea of making their indoor skiing slopes more exciting with the addition of VR.')
        
    with st.container(border=containerBorder):
        st.subheader('Meteor & React Course ([Udemy](https://www.udemy.com/) Jul 2018)', divider=containerDivider)
        st.write('Certificate of Completion, Meteor and React for Realtime Apps.') 

    with st.container(border=containerBorder):
        st.subheader('IELTS Academic ([IELTS Official](https://ielts.org/) May 2017)', divider=containerDivider)    
        st.write('IELTS Academic English test.')

    with st.container(border=containerBorder):
        st.subheader('Scientific contributor to clinical studies ([Inselspital Bern](https://www.insel.ch/de/) Jan 2015 – Jul 2015)', divider=containerDivider)
        st.write('Visualizing clinical data using graphs and charts created by using the programming language R as well as the JavaScript framework ‘D3’ as part of my civil service for Switzerland.')

# Footer
def footer():
    st.write(f':blue-background[©] :rainbow[Tassio Steinmann] :gray[{datetime.date.today().year}]')
    #st.caption(f':blue-background[©] :rainbow[Tassio Steinmann] {datetime.date.today().year}')     #shows too big on some devices

def CSS():
    removeTopPadding()
    pulseHover()
    textHover()
    imageHover()
    buttonHover()
    hideImageFullscreenOption()

def expanders():
    with st.expander('Education & Interests', icon='💖'):
        col1, col2 = st.columns(2)
        with col1:
            education()
        with col2:
            interests()

    with st.expander('Projects', icon='🔥'):
        projects()

    with st.expander('Skills', icon='⭐'):
        skills()

    with st.expander('Languagues', icon='🌟'):    
        languages()

    with st.expander('Accomplishments', icon='🚀'):
        accomplishments()

def Content():
    st.logo("./images/logoB.png", link="https://www.linkedin.com/in/tassios/")

    aboutText()
    profileImage()
    socialIcons()

    expanders()

    footer()

# Main
def main():
    #st.balloons()   
    #st.snow()

    CSS()
    Content()

if __name__ == '__main__':
    main()
