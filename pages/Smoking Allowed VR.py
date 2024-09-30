import streamlit as st
import datetime

projectTitle = 'Smoking Allowed VR'
projectIcon = '🎮'

headerText = f'{projectTitle}'
videoLink = 'https://youtu.be/-BQAGysXx98'

client = 'Hanze'
liveLink = ''
tableData = [
    {'Client': 'https://www.hanze.nl/en', 'Team Size': '6', 'Engine': 'Unity', 'Platforms': 'Oculus, SteamVR'}
]

infoText = """
We received the task to create a game that would make people think about smoking and its development over the years.

The player gets to experience how prevalent smoking was in the past and then travel into the future after accomplishing a few tasks.

We used tunneling to help immerse the players more while simultaneously lessening nausea.
"""

rolesAndResponsibilitiesText = """ 
**Game Design**
- Concept for the objective structure
- VR Controls

**Level Design**
- Recreated all levels from provided concept art

**Code**
- Oculus & SteamVR integration
- Tunneling
- UI
- Interactable objects
- Dialog system
- Cigarette smoke mechanics
- Randomized NPCs
- Sounds

**Art**
- Lighting
- VFX: Smoke particles & the fire burning in the fireplace
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