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


def process_message(message):

    command = message.lower().strip()

    print("Command:", command)

    # ---------- Apps ----------

    if "open chrome" in command:
        print("Opening Chrome")
        return open_chrome()

    elif "open vscode" in command or "open vs code" in command:
        print("Opening VS Code")
        return open_vscode()

    elif "open notepad" in command:
        print("Opening Notepad")
        return open_notepad()

    elif "open calculator" in command or "open calc" in command:
        print("Opening Calculator")
        return open_calculator()

    # ---------- Browser ----------

    elif command.startswith("search "):
        query = message[7:]
        print("Searching:", query)
        return google_search(query)

    elif "open youtube" in command:
        print("Opening YouTube")
        return open_youtube()

    elif "open github" in command:
        print("Opening GitHub")
        return open_github()

    elif "open linkedin" in command:
        print("Opening LinkedIn")
        return open_linkedin()

    # ---------- AI ----------

    print("Sending to Ollama...")
    return ask_ai(message)