import streamlit as st
import random
import re

st.set_page_config(page_title='National Identification', page_icon='ssn.png', layout="centered", initial_sidebar_state="auto", menu_items=None)

hide_streamlit_style = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def ssn():
    def generate_ssn():
        ssn = ''
        for _ in range(3):
            ssn += str(random.randint(0, 9))
        ssn += '-'
        for _ in range(2):
            ssn += str(random.randint(0, 9))
        ssn += '-'
        for _ in range(4):
            ssn += str(random.randint(0, 9))
        return ssn

    def is_valid_ssn(ssn):
        regex = "^\d{3}-\d{2}-\d{4}$"
        return bool(re.match(regex, ssn))

    def calculate_check_digit(ssn):
        ssn_digits = re.findall(r'\d', ssn)
        weighted_sum = sum(int(digit) * weight for digit, weight in zip(ssn_digits[:-1], [9, 8, 7, 6, 5, 4, 3, 2, 1]))
        check_digit = (11 - (weighted_sum % 11)) % 10
        return check_digit == int(ssn_digits[-1])

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Valid SSN "
        "Generator(USA)</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate SSN"):
        ssn = generate_ssn()
        st.code(ssn)
        if is_valid_ssn(ssn) and calculate_check_digit(ssn):
            st.success("Valid SSN!")
        else:
            st.error("Invalid SSN!")


def sin():
    def generate_sin():
        sin = ''
        for _ in range(9):
            sin += str(random.randint(0, 9))
        return sin

    def is_valid_sin(sin):
        sin_list = list(sin)
        check_digit = int(sin_list.pop())
        sin_list.reverse()
        transformed = [int(digit) * (2 if i % 2 == 0 else 1) for i, digit in enumerate(sin_list)]
        transformed = [digit // 10 + digit % 10 for digit in transformed]
        return (sum(transformed) * 9) % 10 == check_digit

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Valid SIN Number "
        "Generator(Canada)</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate SIN"):
        sin = generate_sin()
        st.code(sin)
        if is_valid_sin(sin):
            st.success("Valid SIN!")
        else:
            st.error("Invalid SIN!")



def nin():
    def generate_nin():
        first_letters = random.choices('ABCDEFGHJKLMNPQRSTUVWXYZ', k=2)

        digits = random.choices('0123456789', k=6)

        last_letter = random.choice('ABCDEFGHJKLMNPQRSTUVWXYZ')

        nin = first_letters + digits + [last_letter]
        return ''.join(nin)

    def is_valid_nin(nin):
        if len(nin) != 9:
            return False

        first_letters = nin[:2]
        digits = nin[2:8]
        last_letter = nin[8]

        if not first_letters.isalpha() or not last_letter.isalpha():
            return False

        if not digits.isdigit():
            return False

        check_sum = 0
        check_letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'

        for i in range(6):
            check_sum += int(digits[i]) * (7 - i)

        check_sum %= 23

        return check_letters[check_sum] == last_letter

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Valid NIN Number "
        "Generator(UK)</h1></center>",
        unsafe_allow_html=True)

    st.markdown(
        "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
        unsafe_allow_html=True
    )

    if st.button("Generate NIN"):
        nin = generate_nin()
        st.code(nin)
        if is_valid_nin(nin):
            st.success("Valid NIN!")
        else:
            st.error("Invalid NIN!")




st.sidebar.markdown("""
            <style>
                .sidebar-text {
                    text-align: center;
                    font-weight: 600;
                    font-size: 32px;
                    font-family: 'Comic Sans MS', cursive;
                }
            </style>
            <p class="sidebar-text">Identify</p>
            <br/>
        """, unsafe_allow_html=True)

st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGPEdP2ExEq_mTIuBUPtj6hPh6bxqYd_b8RQ&usqp=CAU")
st.sidebar.markdown(
            "<center><h1 style='font-family: Comic Sans MS; font-weight: 600; font-size: 18px;'>National "
            "Identification</h1></center>",
            unsafe_allow_html=True)
sidebar_options = {
    "SSN": ssn,
    "SIN": sin,
    "NIN": nin,
}

selected_option = st.sidebar.radio("Select a URL shortener:", list(sidebar_options.keys()))

if "prev_option" not in st.session_state:
    st.session_state.prev_option = selected_option

if st.session_state.prev_option != selected_option:
    if selected_option == "SSN":
        st.session_state.long_url_1 = ""
    elif selected_option == "SIN":
        st.session_state.long_url_2 = ""
    elif selected_option == "NIN":
        st.session_state.long_url_3 = ""


st.session_state.prev_option = selected_option
sidebar_options[selected_option]()
