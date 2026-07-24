from agent.ollama_client import ask_ai

from tools.apps import (
    open_chrome,
    open_vscode,
    open_notepad,
    open_calculator,
)

from tools.browser import (
    google_search,
    open_youtube,
    open_github,
    open_linkedin,
)

from tools.files import (
    create_folder,
    open_desktop,
    open_downloads,
    open_documents,
    open_pictures,
    open_music,
    open_videos,
    open_this_pc,
)

from tools.system import (
    shutdown_pc,
    restart_pc,
    sleep_pc,
    lock_pc,
    sign_out,
    volume_up,
    volume_down,
    mute_volume,
)


def process_message(message):

    command = message.lower().strip()

    # ---------------- OPEN COMMANDS ----------------

    if "open" in command:

        # Apps
        if "chrome" in command:
            return open_chrome()

        elif "github" in command:
            return open_github()

        elif "youtube" in command:
            return open_youtube()

        elif "linkedin" in command:
            return open_linkedin()

        elif "vs code" in command or "vscode" in command:
            return open_vscode()

        elif "notepad" in command:
            return open_notepad()

        elif "calculator" in command or "calc" in command:
            return open_calculator()

        # Folders
        elif "desktop" in command:
            return open_desktop()

        elif "downloads" in command:
            return open_downloads()

        elif "documents" in command:
            return open_documents()

        elif "pictures" in command:
            return open_pictures()

        elif "music" in command:
            return open_music()

        elif "videos" in command:
            return open_videos()

        elif "this pc" in command or "file explorer" in command:
            return open_this_pc()

    # ---------------- SYSTEM COMMANDS ----------------

    elif "shutdown" in command:
        return shutdown_pc()

    elif "restart" in command:
        return restart_pc()

    elif "sleep" in command:
        return sleep_pc()

    elif "lock" in command:
        return lock_pc()

    elif "sign out" in command or "logout" in command:
        return sign_out()

    elif "volume up" in command:
        return volume_up()

    elif "volume down" in command:
        return volume_down()

    elif "mute" in command:
        return mute_volume()

    # ---------------- GOOGLE SEARCH ----------------

    elif command.startswith("search "):

        query = message[7:].strip()

        if not query:
            return "Please enter something to search."

        return google_search(query)

    # ---------------- CREATE FOLDER ----------------

    elif command.startswith("create folder"):

        folder_name = message[len("create folder"):].strip()

        if not folder_name:
            return "Please enter a folder name."

        return create_folder(folder_name)

    # ---------------- AI CHAT ----------------

    return ask_ai(message)