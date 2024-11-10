import os
import json
from file_utils import read_file
from openai_client import get_contents
from docx_utils import save_as_docx
from prompts import SYSTEM_PROMPT_ACTION_ITEMS, SYSTEM_PROMPT_SUMMARY_NOTES, SYSTEM_PROMPT_IDENTITY_PARTICIPANTS, SYSTEM_PROMPT_DECISIONS, SYSTEM_PROMPT_IMPORTANT_NOTE, SYSTEM_PROMPT_FOLLOW_UPS, SYSTEM_PROMPT_EXTRACT_QUESTIONS, SYSTEM_PROMPT_CAPTURE_AGENDA, SYSTEM_PROMPT_HIGHLIGHT_CONCERNS, SYSTEM_PROMPT_MEETING_SUMMARY, SYSTEM_PROMPT_MOM


def meeting_minutes(transcription):
    ACTION_ITEMS = get_contents(transcription, SYSTEM_PROMPT_ACTION_ITEMS)
    SUMMARY_NOTES = get_contents(transcription, SYSTEM_PROMPT_SUMMARY_NOTES)
    IDENTITY_PARTICIPANTS = get_contents(transcription, SYSTEM_PROMPT_IDENTITY_PARTICIPANTS)
    DECISIONS = get_contents(transcription, SYSTEM_PROMPT_DECISIONS)

    IMPORTANT_NOTE = get_contents(transcription, SYSTEM_PROMPT_IMPORTANT_NOTE)
    FOLLOW_UPS = get_contents(transcription, SYSTEM_PROMPT_FOLLOW_UPS)
    EXTRACT_QUESTIONS = get_contents(transcription, SYSTEM_PROMPT_EXTRACT_QUESTIONS)

    CAPTURE_AGENDA = get_contents(transcription, SYSTEM_PROMPT_CAPTURE_AGENDA)
    HIGHLIGHT_CONCERNS = get_contents(transcription, SYSTEM_PROMPT_HIGHLIGHT_CONCERNS)
    MEETING_SUMMARY = get_contents(transcription, SYSTEM_PROMPT_MEETING_SUMMARY)
    MOM = get_contents(transcription, SYSTEM_PROMPT_MOM)

    return {
        'Action Items': ACTION_ITEMS,
        'Summary Notes': SUMMARY_NOTES,
        'Participants': IDENTITY_PARTICIPANTS,
        'Decisions': DECISIONS,

        'Important Note': IMPORTANT_NOTE,
        'Follow Ups': FOLLOW_UPS,
        'Questions': EXTRACT_QUESTIONS,

        'Agenda': CAPTURE_AGENDA,
        'Concerns': HIGHLIGHT_CONCERNS,
        'Meeting Summary': MEETING_SUMMARY,
        'MOM': MOM
    }

if __name__ == "__main__":
    file_path = "../data/transcription.txt"
    content = read_file(file_path)
    file_name = file_path.split("/")[-1].split(".")[0].replace(" ", "")
    minutes = meeting_minutes(content)
    base_file_op_path = "../output"
    save_as_docx(minutes, f'{base_file_op_path}{file_name}_detailed_meeting_minutes.docx')
    with open(f'{base_file_op_path}{file_name}_minutes.json', 'w') as file:
        json.dump(minutes, file, indent=4)

    # file_path = "../data/transcription.txt"
    # content = read_file(file_path)
    # file_name = os.path.basename(file_path).split(".")[0].replace((" ", ""))
    # minutes = meeting_minutes(content)
    # base_file_op_path = "../output"
    # save_as_docx(minutes, f'{base_file_op_path}{file_name}_detailed_meeting_minutes.docx')
    # with open(f'{base_file_op_path}{file_name}_minutes.json', 'w') as file:
    #     json.dump(minutes, file, indent=4)