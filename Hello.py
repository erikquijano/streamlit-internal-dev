import streamlit as st

# Create session state variables for managing login status and user session
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

def login(username, password):
    # Simple check for username and password
    if username == "admin" and password == "testuser20":
        st.session_state['login_status'] = True
    else:
        st.session_state['login_status'] = False
        st.error("Incorrect Username or Password")

def logout():
    st.session_state['login_status'] = False

# Layout for login
def main():
    st.title("Streamlit Application")

    # Check if the user is logged in
    if st.session_state['login_status']:
        st.success("Logged in as admin")
        st.button("Logout", on_click=logout)
        # Your application code goes here
        st.write("Welcome to the secure part of the app!")

    else:
        # Login form
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login", on_click=login, args=(username, password))
            if login_button:
                if st.session_state['login_status']:
                    st.success("Login Successful!")
                else:
                    st.error("Login Failed. Try Again!")

if __name__ == "__main__":
    main()
