from tools.apps import *


def execute(plan):

    tool = plan.get("tool")

    if tool == "chat":
        return plan["message"]

    if tool == "apps":

        action = plan.get("action")

        if action == "open_chrome":
            return open_chrome()

        elif action == "open_vscode":
            return open_vscode()

        elif action == "open_notepad":
            return open_notepad()

        elif action == "open_calculator":
            return open_calculator()

    return "I don't know how to do that yet."