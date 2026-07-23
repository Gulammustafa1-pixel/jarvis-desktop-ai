import json
from agent.ollama_client import ask_ai


SYSTEM_PROMPT = """
You are an AI planner.

Your job is to convert the user's request into JSON.

Available tools:

1. apps
Actions:
- open_chrome
- open_vscode
- open_notepad
- open_calculator

If no tool is needed, return:

{
    "tool":"chat",
    "message":"..."
}

If a tool is needed return:

{
    "tool":"apps",
    "action":"open_chrome"
}

Return ONLY JSON.
"""


def create_plan(user_message):

    response = ask_ai(
        SYSTEM_PROMPT + "\n\nUser: " + user_message
    )

    try:
        return json.loads(response)

    except:
        return {
            "tool": "chat",
            "message": response
        }