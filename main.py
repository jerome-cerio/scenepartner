import os
import streamlit as st
import PyPDF2
import scriptreader

from io import StringIO
from streamlit.runtime.uploaded_file_manager import UploadedFile
from typing import Tuple


def display_widgets() -> Tuple[UploadedFile, str]:
  script_file = st.file_uploader(label="Upload your scene here",type="pdf")
  script_text = st.text_area("Or copy and paste your code here (press Ctrl + Enter to send")

  if not (script_text or script_file):
    st.error("Supply your code with one of the options from above.")

  return script_file, script_text

def get_text():
  uploaded_script, pasted_script = display_widgets()
  if uploaded_script:
    # read from pdf
    pdf_text = StringIO(uploaded_script.getvalue().decode("utf-8"))
    if pdf_text:
      return pdf_text
    else:
      st.error("Error reading your PDF. Please try again.")
  return pasted_script or ""

def main():
  st.title("Scene Reader for Scripts")

  # Request script input from user. 
  st.write("Upload a script file to read out the characters and dialogue.")
  character_list = ""
  lines = ""
  
  if script_input := get_text():
    with st.spinner("Reading your script..."):
      # Use partials defined in scriptreader.py to send script to OpenAI model.
      character_list = scriptreader.retrieve_characters(script_input)
      lines = scriptreader.retrieve_lines(script_input)

      st.write(character_list)
      st.write(lines)

  # Have the user choose the character they intend to read.
  user_character = st.selectbox("Choose YOUR character to read: ", list(character_list))

  
if __name__ == "__main__":
  main()