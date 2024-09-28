import streamlit as st

projectTitle = 'Become a Virtual Groninger'
projectIcon = '🎮'

headerText = f'{projectTitle}'
videoLink = 'https://youtu.be/'

client1 = 'Marketing Groningen'
client2 = 'AAN ZET communicatie'
liveLink = ''
tableData = [
    {'Client 1': 'https://www.merkgroningen.nl/nl/marketinggroningen', 'Client 2': 'https://www.aanzetcommunicatie.nl/', 'Team Size': '2', 'Platforms': 'Web'}
]

infoText = """
We received the task to create a cost-effective alternative to flight simulators for Corendon Airlines.

The pilots get to practice the de-icing procedure in VR supported by hand tracking.

We collaborated closely with an experienced pilot to implement the features our target audience is looking for.
"""

rolesAndResponsibilitiesText = """ 
**Game Design**
- VR Controls
- Hand tracking

**Level Design**
- Recreated real life dimensions of a Boeing 737 cockpit in VR

**Code**
- Oculus integration
- MRTK hand tracking
- Interactable buttons, switches and levers
- UI
- Sounds
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
            'Client 1': st.column_config.LinkColumn(
                'Client 1', display_text=client1
            ),
            'Client 2': st.column_config.LinkColumn(
                'Client 2', display_text=client2
            )
        }, use_container_width=True, hide_index=True)
    else:
        st.dataframe(tableData, column_config={
            'Client 1': st.column_config.LinkColumn(
                'Client 1', display_text=client1
            ),
            'Client 2': st.column_config.LinkColumn(
                'Client 2', display_text=client2
            )
        }, use_container_width=True, hide_index=True)

def info():
    st.header('Info')
    infoText

    st.subheader('Roles & Responsibilities')
    rolesAndResponsibilitiesText

def main():
    header()
    st.image("./projects/become-a-virtual-groninger/Screenshot_2.jpg")
    #st.video(videoLink)
    quickFacts()
    info()

if __name__ == '__main__':
    main()    