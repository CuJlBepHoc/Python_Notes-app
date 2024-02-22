from note_operations import read_notes


def filter_notes_by_date(date):
    notes = read_notes()
    filter_notes = [
        note for note in notes if note['timestamp'].startswith(date)]
    return filter_notes
