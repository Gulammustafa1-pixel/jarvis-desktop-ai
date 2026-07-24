import numpy as np
from openwakeword.model import Model

from wakeword.microphone import Microphone

from voice.speaker import speak
from voice.speech import listen
from agent.brain import process_message


THRESHOLD = 0.5


def start_wake_word():

    print("🤖 Jarvis is waiting for wake word...")

    model = Model(
        wakeword_models=["hey_jarvis"],
        inference_framework="onnx"
    )

    mic = Microphone()

    activated = False

    try:

        while True:

            audio = mic.read()

            audio = np.frombuffer(audio, dtype=np.int16)

            prediction = model.predict(audio)

            score = prediction.get("hey_jarvis", 0)

            if score > THRESHOLD and not activated:

                activated = True

                print("🔥 Jarvis Activated!")

                speak("Yes, how can I help?")

                command = listen()

                if command:

                    print("You:", command)

                    response = process_message(command)

                    print("Jarvis:", response)

                    if response:
                        speak(response)

                activated = False

    except KeyboardInterrupt:

        print("Stopping Jarvis...")

    finally:

        mic.close()


if __name__ == "__main__":

    start_wake_word()