import streamlit as st
import datetime

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
During my internship at Indietopia I helped create the improved version of ‘Become a Virtual Groninger’ for our clients Marketing Groningen and AAN ZET communicatie.

‘Become a Virtual Groninger’ aims to introduce new students to the city of Groningen with an interactive experience supported by 360° photos.

Users can use the map to navigate the game as well as the city and save their favorite locations or share them with others!
"""

rolesAndResponsibilitiesText = """ 
**Game Design**
- UI

**Code**
- Navigation bar
- Map
- Favorites
- Sharing
- Download ‘City guide’
- Fullscreen
- Mobile compatibility
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

def footer():
    st.caption(f':blue-background[©] :rainbow[Tassio Steinmann] {datetime.date.today().year}')

def main():
    textHover()

    header()
    st.image("./projects/Become a Virtual Groninger 2D/Screenshot_2.jpg")
    #st.video(videoLink)
    quickFacts()
    info()
    footer()

if __name__ == '__main__':
    main()    