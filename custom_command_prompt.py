import streamlit as st
import subprocess

# Streamlit app title
st.title("Windows Command Prompt Integration")

# Function to execute a shell command and capture its output
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# Streamlit UI components
st.header("Run Command")
command_input = st.text_input("Enter command")

if st.button("Run"):
    if command_input:
        output = run_command(command_input)
        st.text_area("Output", value=output, height=300)
    else:
        st.warning("Please enter a command.")
