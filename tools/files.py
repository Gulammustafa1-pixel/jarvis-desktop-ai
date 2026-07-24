import os
import subprocess


def create_folder(folder_name):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_path = os.path.join(desktop, folder_name)

    try:
        os.makedirs(folder_path, exist_ok=True)
        return f"Folder '{folder_name}' created successfully."
    except Exception as e:
        return str(e)


def open_desktop():
    path = os.path.join(os.path.expanduser("~"), "Desktop")
    subprocess.Popen(f'explorer "{path}"')
    return "Opening Desktop..."


def open_downloads():
    path = os.path.join(os.path.expanduser("~"), "Downloads")
    subprocess.Popen(f'explorer "{path}"')
    return "Opening Downloads..."


def open_documents():
    path = os.path.join(os.path.expanduser("~"), "Documents")
    subprocess.Popen(f'explorer "{path}"')
    return "Opening Documents..."


def open_pictures():
    path = os.path.join(os.path.expanduser("~"), "Pictures")
    subprocess.Popen(f'explorer "{path}"')
    return "Opening Pictures..."


def open_music():
    path = os.path.join(os.path.expanduser("~"), "Music")
    subprocess.Popen(f'explorer "{path}"')
    return "Opening Music..."


def open_videos():
    path = os.path.join(os.path.expanduser("~"), "Videos")
    subprocess.Popen(f'explorer "{path}"')
    return "Opening Videos..."


def open_this_pc():
    subprocess.Popen("explorer")
    return "Opening File Explorer..."