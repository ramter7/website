import streamlit as st
import datetime

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

if liveLink != '':
    liveLinkIcon = '🕹️'
else:
    liveLinkIcon = ''

st.set_page_config(
    page_title=projectTitle,
    page_icon=projectIcon,
    layout='centered',
    initial_sidebar_state='collapsed'
)

def textHover():
    st.html("""
        <style>
            .animated-text:hover {
                color: #FF5733;
                transition: color 0.3s ease;
            }
        </style>
    """)

def header():
    col1, col2 = st.columns([0.075, 0.925])
    with col1:
        if st.button('🏠', type='primary'):
            st.switch_page('Home.py')

    with col2:
        st.html(f"""
            <style>
                .waving {{
                    animation-name: wave-animation;
                    animation-duration: 2.5s;
                    animation-iteration-count: infinite;
                    #transform-origin: 70% 70%;
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
            <span class='animated-text' style='font-size: 32px;'>{headerText}<span class='waving'>{liveLinkIcon}</span></span>
        """, unsafe_allow_html=True)

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

def footer():
    st.caption(f':blue-background[©] :rainbow[Tassio Steinmann] {datetime.date.today().year}')

def main():
    textHover()

    header()
    st.video(videoLink)
    quickFacts()
    info()
    footer()

if __name__ == '__main__':
    main()    