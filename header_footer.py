import streamlit as st

# Function to create a beautiful header
def create_header():
    st.title("Rainfall Prediction App")
    st.image("rainfall.png", use_column_width=True)

# Function to create a beautiful footer
def create_footer():
    st.write(
        """
        ---
        ### Contact Information
        For inquiries, please contact us at [shyamp665@gmail.com](mailto:shyamp665@gmail.com).
        
        ### Credits
        This app is powered by [Flanker](https://www.flankershyam.tech/).
        """
    )