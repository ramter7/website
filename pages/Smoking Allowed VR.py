import streamlit as st

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

    st.subheader('Roles & Responsibilities')
    rolesAndResponsibilitiesText

def main():
    header()
    st.video(videoLink)
    quickFacts()
    info()

if __name__ == '__main__':
    main()    