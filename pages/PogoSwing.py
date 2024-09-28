import streamlit as st

projectTitle = 'PogoSwing'
projectIcon = '🎮'

headerText = f'{projectTitle} - [Play](https://ramter77.github.io/PogoSwing-WebGL/)'
videoLink = 'https://youtu.be/kCh-6frxRMg'

client = 'Hanze'
liveLink = 'https://ramter77.github.io/PogoSwing-WebGL/'
tableData = [
    {'Live Link': liveLink, 'Client': 'https://www.hanze.nl/en', 'Team Size': '1', 'Engine': 'Unity', 'Platforms': 'Windows, MacOS, Linux, VR (WIP)'}
]

infoText = """
I wanted to make a fast paced, first-person 3D platformer game with a underrepresented mechanic: a pogo stick. The VR version is still WIP.

The player controls a human jumping up & down on a pogo stick that has a grappling hook in each hand to traverse the challenging environment.

The focus is entirely on gameplay with free movement & simple goals limited by time & the environment.
"""

rolesAndResponsibilitiesText = """ 
**Game Design**
- Concept (VR) gameplay
- Controls (Keyboard/Mouse & Gamepad) & VR

**Level Design**
- Replicated real life terrain in the Patagonian Andes using heightmaps from the area around the “Torres del Paine” National Park & added assets like trees & rocks that extend the gameplay & visuals
- Concept for 5 different levels

**Code**
- Player character
- UI
- Grapple mechanics
- VR integration (WIP)

**Art**
- Sounds
- Universal Render Pipeline integration
- Post processing
"""

######################################################################################

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
        
        <span class='animated-text' style='font-size: 32px;'>{headerText}<span class='waving'>🕹️</span></span>
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

    st.subheader('Roles & Responsibilities')
    rolesAndResponsibilitiesText

def main():
    header()
    st.video(videoLink)
    quickFacts()
    info()

if __name__ == '__main__':
    main()    