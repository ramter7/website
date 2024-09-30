import streamlit as st
import datetime

projectTitle = 'Defiance'
projectIcon = '🎮'

headerText = f'{projectTitle}'
videoLink = 'https://youtu.be/Ef-hb9FmGUo'

client = 'Hanze'
liveLink = ''
tableData = [
    {'Client': 'https://www.hanze.nl/en', 'Team Size': '6', 'Engine': 'Unity', 'Platforms': 'Windows, MacOS, Linux'}
]

infoText = """
We received the task to create an emergent game in a group. The result is a blend of platforming and challenging puzzles set in a procedurally generated labyrinth that’s deeply rooted in Greek mythology.

The labyrinth houses many dangers and secrets, from traps and enemies, to hidden items and potions.

At the end of it three Greek goddesses await you to test your wits and give you a different reward depending on how you choose to deal with the situation.
"""

rolesAndResponsibilitiesText = """ 
**Game Design**
- Concept for an endless runner/platformer
- Controls (Keyboard/Mouse & Gamepad)

**Level Design**
- Extended procedural level generator
- Level editor to enable designers to create levels using our existing structures

**Code**
- Player character
- UI
- Extended procedural level generator
- Interactions, movement abilities & special weapons
- Sounds

**Art**
- Normal maps (WIP)
- VFX: Trail particles
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
                color: #FF4B4B;
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