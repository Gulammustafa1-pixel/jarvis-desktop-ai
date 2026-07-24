import sys
import threading

from PySide6.QtWidgets import QApplication

from ui.gui import JarvisGUI
from wakeword.detector import start_wake_word



def start_jarvis():

    thread = threading.Thread(
        target=start_wake_word,
        daemon=True
    )

    thread.start()



if __name__ == "__main__":

    print("===== Jarvis Desktop AI =====")


    # Start Wake Word Listener
    start_jarvis()


    # Start GUI
    app = QApplication(sys.argv)


    window = JarvisGUI()

    window.show()


    sys.exit(
        app.exec()
    )