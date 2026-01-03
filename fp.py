import streamlit as st
import user_form

def main():
    user_form.init_state()

    if st.session_state.page == 1:
        user_form.user_profile_form()
    elif st.session_state.page == 2:
        user_form.user_pl_form()
    elif st.session_state.page == 3:
        user_form.user_ret_ratios()
    elif st.session_state.page == 4:
        user_form.user_retirement_cal()

main()


