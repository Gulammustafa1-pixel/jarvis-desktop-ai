import threading
from wakeword.detector import start_wake_word


print("🤖 Jarvis Background Service Started")


thread = threading.Thread(
    target=start_wake_word,
    daemon=True
)

thread.start()


while True:
    pass