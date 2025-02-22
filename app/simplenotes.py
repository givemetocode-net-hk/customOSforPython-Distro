import sqlite3

class NoteApp:
    def __init__(self, db_name='simplenotes.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY,
                    note TEXT NOT NULL
                )
            ''')

    def add_note(self, note):
        with self.connection:
            self.connection.execute('INSERT INTO notes (note) VALUES (?)', (note,))
        print("Note added.")

    def view_notes(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT id, note FROM notes')
        notes = cursor.fetchall()
        if not notes:
            print("No notes available.")
        else:
            print("\nList of Notes:")
            for id, note in notes:
                print(f"{id}: {note}")

    def delete_note(self, note_id):
        with self.connection:
            cursor = self.connection.execute('DELETE FROM notes WHERE id = ?', (note_id,))
            if cursor.rowcount == 0:
                print("Invalid note number.")
            else:
                print(f"Deleted note with ID: {note_id}")

    def run(self):
        print("simplenotes v1.0")
        while True:
            command = input("\nEnter a command (add/view/delete/exit): ").strip().lower()
            if command == 'add':
                note = input("Enter your note: ")
                self.add_note(note)
            elif command == 'view':
                self.view_notes()
            elif command == 'delete':
                try:
                    note_id = int(input("Enter the note ID to delete: "))
                    self.delete_note(note_id)
                except ValueError:
                    print("Please enter a valid number.")
            elif command == 'exit':
                break
            else:
                print("Invalid command.")

if __name__ == "__main__":
    app = NoteApp()
    app.run()