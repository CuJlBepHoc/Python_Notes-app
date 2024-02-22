import datetime
from note_operations import read_notes


def filter_notes_by_date(date):
    notes = read_notes()
    filter_notes = [
        note for note in notes if datetime.datetime.strptime(note['timestamp'], '%Y-%m-%d %H:%M:%S').date() == datetime.datetime.strptime(date, '%Y-%m-%d').date()]
    return filter_notes
