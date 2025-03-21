#############################################################################
# app.py
#
# This file contains the entrypoint for the app.
#
#############################################################################

import streamlit as st
from modules import display_profile, display_my_custom_component, display_post, display_genai_advice, display_activity_summary, display_recent_workouts

userId = 'user1'


def display_app_page():
    """Displays the home page of the app."""
    st.title('[Welcome to SDS!')

    # An example of displaying a custom component called "my_custom_component"
    user_id = st.text_input('Enter your user ID')
    # display_my_custom_component(user_id)
    display_profile(user_id)


# This is the starting point for your app. You do not need to change these lines
if __name__ == '__main__':
    display_app_page()
