import os

class NoteApp:
    def __init__(self, filename="notes.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                pass  # Create the file if it doesn't exist

    def add_note(self, note):
        with open(self.filename, "a") as f:
            f.write(note + "\n")
        print("Note added!")

    def view_notes(self):
        with open(self.filename, "r") as f:
            notes = f.readlines()
        if notes:
            print("Your Notes:")
            for idx, note in enumerate(notes, 1):
                print(f"{idx}. {note.strip()}")
        else:
            print("No notes found.")

    def delete_note(self, note_number):
        with open(self.filename, "r") as f:
            notes = f.readlines()
        if 1 <= note_number <= len(notes):
            notes.pop(note_number - 1)
            with open(self.filename, "w") as f:
                f.writelines(notes)
            print("Note deleted!")
        else:
            print("Invalid note number.")

    def menu(self):
        while True:
            print("\n--- Note Taking App ---")
import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
