import streamlit as st
from base64 import b64encode

projectTitle = 'Skyline VR'
projectIcon = '🎮'

headerText = f'{projectTitle}'
videoLink = 'https://youtu.be/V0qNzP6-el4'

client = 'SnowLimits Ski Center Groningen'
liveLink = ''
tableData = [
    {'Client': 'https://www.snowlimits.nl/', 'Team Size': '5', 'Engine': 'Unity', 'Platforms': 'Oculus Quest'}
]

# Image zoom on hover
def imageHover():
    st.markdown("""
    <style>
    .image-hover:hover {
        transform: scale(1.1);
        transition: transform 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

# Image
def infoImg():
    with open('./projects/skyline/SnowLimits-Overview.png', 'rb') as img_file:
        img = 'data:image/png;base64,' + b64encode(img_file.read()).decode()
    
    # HTML to display the image with the hover effect
    image_html = f"""
    <div style='display: flex; justify-content: center; margin-bottom: 2%'>
        <img class='image-hover' src='{img}' style='width: 75%;' alt='Snowlimits'>
    </div>
    """
    st.markdown(image_html, unsafe_allow_html=True)

infoText = """
Snowlimits offers indoor skiing and snowboarding on an endless indoor roller track. Check out the Snowlimits website for more information.
"""

infoText2 = """
SnowLimits approached us with the idea of making their indoor skiing slopes more exciting with the addition of VR.

We created a game that will let their teachers choose a tailored exercise with adjustable difficulty levels to match the customers needs.

The data from the VR headset gets sent to a server in the cloud which validates it and then sends it to our smartphone app right into the hands of the teacher so that he can see his student’s view alongside all the data he needs.

We also integrated hand tracking so more advanced students could train on their own by adjusting settings directly in the game!
"""

rolesAndResponsibilitiesText = """ 
**Game Design**
- Concept for the communication of the app with the game on the Oculus Quest through a server
- Concept for VR gameplay
- VR Controls

**Level Design**
- Replicated real life dimensions of slope in VR & added a mountain terrain

**Code**
- Player character
- UI
- Sounds
- VR setup & Hand tracking
- Server communication

**Art**
- Universal Render Pipeline integration
- Post processing

**More**
- Workshop to explain Unity & Servers to the group
- Skiing on the slope in VR
"""

######################################################################################

if liveLink != '':
    liveLinkIcon = '🕹️'
else:
    liveLinkIcon = ''

st.set_page_config(
    page_title=projectTitle,
    page_icon=projectIcon,         #🎮 for games, 🖥️? for apps?, 
    layout='centered',
    initial_sidebar_state='collapsed'
)
# Remove some top padding
st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

def textHover():
    st.markdown("""
    <style>
    .animated-text:hover {
        color: #FF5733; /* Change color on hover */
        transition: color 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

def header():
    col1, col2 = st.columns([0.075, 0.925])
    with col1:
        if st.button('🏠', type="primary"):
            st.switch_page('Home.py')

    with col2:
        st.write(f"""
        <style>                      
        .animated-text:hover {{  
        color: #FF5733; /* Change color on hover */
        transition: color 0.3s ease;
        }}

        .waving {{
        animation-name: wave-animation;
        animation-duration: 2.5s;
        animation-iteration-count: infinite;
        #transform-origin: 50% 50%;
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
        
        <span class='animated-text' style='font-size: 32px;'>{headerText}<span class='waving'>{liveLinkIcon}</span></span>
        """, 
        unsafe_allow_html=True)

def quickFacts():
    st.header('Quick Facts')

    if liveLink != '':
        st.dataframe(tableData, column_config={
            'Live Link': st.column_config.LinkColumn(
                'Live Link', display_text='Link'
            ),
            'Client': st.column_config.LinkColumn(
                'Client', display_text=client
            )
        }, use_container_width=True, hide_index=True)
    else:
        st.dataframe(tableData, column_config={
            'Client': st.column_config.LinkColumn(
                'Client', display_text=client
            )
        }, use_container_width=True, hide_index=True)

def info():
    st.header('Info')
    infoText
    infoImg()
    infoText2

    st.subheader('Roles & Responsibilities')
    rolesAndResponsibilitiesText

def main():
    imageHover()

    header()
    st.video(videoLink)
    quickFacts()
    info()

if __name__ == '__main__':
    main()    