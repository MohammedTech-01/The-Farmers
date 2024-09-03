import streamlit as st
import time
import os

# Function to read the alert from the file
def read_alert(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()
    return None

# Function to display alerts and healed messages
def display_alert(file_path):
    previous_message = None
    alert_placeholder = st.empty()

    while True:
        current_message = read_alert(file_path)
        
        if current_message != previous_message:  # Check if there is a new alert or heal message
            alert_placeholder.empty()  # Clear the previous message
            if current_message:
                if current_message.startswith("Alert"):
                    # Display the alert message with red text
                    alert_placeholder.markdown(
                        f"""
                        <div style="background-color: red; padding: 10px; border-radius: 5px;">
                            <p style="color: white;">{current_message}</p>
                        </div>
                        """, unsafe_allow_html=True
                    )
                elif current_message.startswith("The soil"):
                    # Display the healed message with green text
                    alert_placeholder.markdown(
                        f"""
                        <div style="background-color: green; padding: 10px; border-radius: 5px;">
                            <p style="color: white;">{current_message}</p>
                        </div>
                        """, unsafe_allow_html=True
                    )
            else:
                alert_placeholder.info("No detected")  # Display a default message if the file is empty

            previous_message = current_message
        
        time.sleep(1)  # Wait for 1 second before checking again

# Streamlit application layout
st.title("Soil Quality Detector")
st.write("Monitoring soil quality...")

alert_file_path = 'alert.txt'  # Path to the alert file

# Call the function to display alerts
display_alert(alert_file_path)
