import subprocess


def open_chrome():
    try:
        subprocess.Popen("start chrome", shell=True)
        return "Opening Google Chrome..."
    except Exception as e:
        return f"Error: {e}"


def open_vscode():
    try:
        subprocess.Popen("code", shell=True)
        return "Opening VS Code..."
    except Exception as e:
        return f"Error: {e}"


def open_notepad():
    try:
        subprocess.Popen("notepad")
        return "Opening Notepad..."
    except Exception as e:
        return f"Error: {e}"


def open_calculator():
    try:
        subprocess.Popen("calc")
        return "Opening Calculator..."
    except Exception as e:
        return f"Error: {e}"