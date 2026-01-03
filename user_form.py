import streamlit as st

from fin_func import calculate_retirement_corpus

# ------------------------------
# Page State Initialization
# ------------------------------
def init_state():
    if "page" not in st.session_state:
        st.session_state.page = 1

# ------------------------------
# User Profile form
# ------------------------------

def user_profile_form():
    st.title("Step 1: Personal Details ")

    st.session_state.name = st.text_input("Your Name")
    st.session_state.current_age = st.number_input("Current Age", min_value=0, step=1, max_value=100)
    st.session_state.retirement_age = st.number_input("Retirement Age", min_value=0, step=1, max_value=100)

    if st.button("Next"):
        st.session_state.page = 2
        st.rerun()

def user_pl_form():
    st.title("Step 2: Income & Expenses")

    st.session_state.income = st.number_input("Monthly Income (₹)", min_value=0.0, step=50000.0)
    st.session_state.expense = st.number_input("Monthly Expenses (₹)", min_value=0.0, step=50000.0)

    col1, col2 = st.columns(2)
    if col1.button("Back"):
        st.session_state.page = 1
        st.rerun()

    if col2.button("Next"):
        st.session_state.page = 3
        st.rerun()

# ------------------------------
# Page 3: Inflation & Returns
# ------------------------------
def user_ret_ratios():
    st.title("Step 3: Inflation & Returns")

    st.session_state.inflation = st.number_input(
        "Expected Inflation Rate (%)", value=7.0
    ) / 100

    st.session_state.return_rate = st.number_input(
        "Post-Retirement Return (%)", value=12.0
    ) / 100

    col1, col2 = st.columns(2)
    if col1.button("Back"):
        st.session_state.page = 2
        st.rerun()

    if col2.button("Calculate"):
        st.session_state.page = 4
        st.rerun()

# ------------------------------
# Page 4: Result Page
# ------------------------------
def user_retirement_cal():
    st.title("Step 4: Retirement Corpus")

    years_to_retire = st.session_state.retirement_age - st.session_state.current_age

    corpus = calculate_retirement_corpus(
        current_age=st.session_state.current_age,
        retirement_age=st.session_state.retirement_age,
        current_monthly_expense=st.session_state.expense,
        inflation_rate=st.session_state.inflation,
        post_retirement_return=st.session_state.return_rate
    )

    st.success(f"👤 Hello {st.session_state.name}")
    st.write(f"⏳ You have {years_to_retire} Year to Retire")
    st.write(f"💸 Your Annual Expenses Today is ₹{st.session_state.expense*12:,.0f}")
    st.write("---")
    st.metric("💰 The Required Retirement Corpus is ", f"₹{corpus:,.0f}")

    if st.button("Start Over"):
        st.session_state.page = 1
        st.rerun()
