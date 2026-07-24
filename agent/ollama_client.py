import ollama


SYSTEM_PROMPT = """
You are Jarvis, a desktop AI assistant.

If the user wants to perform one of these actions, reply ONLY with the keyword.

Commands:

OPEN_CHROME
OPEN_VSCODE
OPEN_NOTEPAD
OPEN_CALCULATOR
OPEN_GITHUB
OPEN_YOUTUBE
OPEN_LINKEDIN
SEARCH_GOOGLE:

If the user wants Google Search, reply:

SEARCH_GOOGLE: user query

Examples:

User: Search Python tutorials
Assistant:
SEARCH_GOOGLE: Python tutorials

User: Open GitHub
Assistant:
OPEN_GITHUB

If it is a normal question, answer normally.
"""


def ask_ai(prompt):

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]