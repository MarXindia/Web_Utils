import streamlit as st
import subprocess

# Streamlit app title
st.title("Windows Task Manager")

# Function to execute a shell command and capture its output
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# Streamlit UI components
st.header("List Running Processes")

# Run tasklist command to list running processes
tasklist_output = run_command("tasklist")

st.header("Kill Process")

# Input field for process name or PID to kill
process_input = st.text_input("Enter Process Name or PID to Kill")
# Display output in Streamlit text area
st.text_area("Tasklist Output", value=tasklist_output, height=600)



# Button to kill process
if st.button("Kill"):
    if process_input:
        # Run taskkill command to terminate process
        taskkill_output = run_command(f"taskkill /F /IM {process_input}")
        st.text_area("Taskkill Output", value=taskkill_output, height=100)
    else:
        st.warning("Please enter a process name or PID.")
