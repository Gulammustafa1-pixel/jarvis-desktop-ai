import os
import subprocess


def open_chrome():
    try:
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    except:
        subprocess.Popen("start chrome", shell=True)

    return "Opening Chrome."


def open_vscode():
    try:
        subprocess.Popen("code", shell=True)
    except:
        return "VS Code is not installed or not added to PATH."

    return "Opening VS Code."


def open_notepad():
    subprocess.Popen("notepad")
    return "Opening Notepad."


def open_calculator():
    subprocess.Popen("calc")
    return "Opening Calculator."