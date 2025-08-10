import streamlit as st
import os
import json

# Set the title of the app
st.title('Simple Note-Taking App')

# File to store notes
notes_file = 'notes.json'

# Initialize notes storage if file doesn't exist
if not os.path.exists(notes_file):
    with open(notes_file, 'w') as f:
        json.dump([], f)

# Function to load notes from the file
def load_notes():
    with open(notes_file, 'r') as f:
        return json.load(f)

# Function to save notes to the file
def save_notes(notes):
    with open(notes_file, 'w') as f:
        json.dump(notes, f)

# Display the current notes
notes = load_notes()

# Display existing notes in the app
st.subheader("Your Notes")
for idx, note in enumerate(notes):
    st.text_area(f"Note {idx + 1}", value=note, height=100, max_chars=1000, key=f"note_{idx}", disabled=True)
    st.write("---")

# Add a new note
st.subheader("Add a New Note")
new_note = st.text_area("Your new note", height=150, max_chars=1000)

# Button to save the new note
if st.button("Save Note"):
    if new_note.strip():
        notes.append(new_note)
        save_notes(notes)
        st.success("Note saved successfully!")
    else:
        st.warning("Note can't be empty!")

# Delete a note
st.subheader("Delete a Note")
note_to_delete = st.selectbox("Select note to delete", [f"Note {i+1}" for i in range(len(notes))])
if st.button("Delete Note"):
    if note_to_delete:
        notes.pop(int(note_to_delete.split()[-1]) - 1)
        save_notes(notes)
        st.success(f"{note_to_delete} deleted successfully!")
    else:
        st.warning("No note selected to delete.")
