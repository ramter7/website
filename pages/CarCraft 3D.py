import streamlit as st

projectTitle = 'CarCraft'
projectIcon = '🎮'

headerText = f'{projectTitle}'
videoLink = 'https://youtu.be/jLP_34_Vz7E'

client = 'Myself'
liveLink = ''
tableData = [
    {'Client': 'https://www.linkedin.com/in/tassios/', 'Team Size': '1', 'Engine': 'Unity', 'Platforms': 'Windows'}
]

infoText = """
This is the second game I made in my free time in 2013 by combining the aspects of a car with those of an aircraft.

The player can steer the car with the arrow keys and uses the WASD keys to control the speed of the propellers and the angle of the rudders.

The goal is to compete against simple opponents which drive a normal car and others which just fly by to finish the race in first place.
"""

rolesAndResponsibilitiesText = """ 
**Game Design**
- Concept for a racing game
- Concept for how to combine the driving & flying mechanic
- Controls (Keyboard/Mouse)

**Level Design**
- Terrain with circuit and obstacles

**Code**
- Combined driving & flying mechanic
- Opponents
- Sounds

**Art**
- VFX: Smoke particles & trails
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