from voice.speech import listen
from voice.speaker import speak
from agent.brain import process_message

print("===== Jarvis Voice Assistant =====")

speak("Jarvis is now online.")

while True:

    command = listen()

    if not command:
        continue

    print(f"\nYou: {command}")

    response = process_message(command)

    print(f"Response = {repr(response)}")

    if response:
        speak(str(response))
    else:
        speak("Done.")