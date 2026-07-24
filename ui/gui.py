import sys
import threading

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QLabel,
)

from PySide6.QtCore import Qt, Signal, QObject


from agent.brain import process_message
from voice.speech import listen
from voice.speaker import speak



# Thread se GUI update karne ke liye
class WorkerSignals(QObject):
    message = Signal(str)



class JarvisGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("🤖 Jarvis AI Assistant")
        self.resize(900, 650)


        self.setStyleSheet("""
        
        QWidget{
            background:#202123;
            color:white;
            font-family:Segoe UI;
        }

        QTextEdit{
            background:#343541;
            border-radius:10px;
            padding:10px;
            font-size:14px;
        }


        QLineEdit{
            background:#40414F;
            border-radius:10px;
            padding:12px;
            color:white;
            font-size:14px;
        }


        QPushButton{

            background:#10A37F;
            color:white;
            border-radius:10px;
            padding:10px 18px;
            font-size:14px;
        }


        QPushButton:hover{
            background:#0d8f6f;
        }


        QLabel{
            font-size:24px;
            font-weight:bold;
        }

        """)


        main_layout = QVBoxLayout()



        # Title

        title = QLabel("🤖 Jarvis AI")

        title.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(title)



        # Chat Area

        self.chat = QTextEdit()

        self.chat.setReadOnly(True)

        main_layout.addWidget(self.chat)



        # Bottom section

        bottom = QHBoxLayout()


        self.input = QLineEdit()

        self.input.setPlaceholderText(
            "Type your message..."
        )


        self.send_btn = QPushButton("Send")


        self.mic_btn = QPushButton("🎤")


        bottom.addWidget(self.input)

        bottom.addWidget(self.mic_btn)

        bottom.addWidget(self.send_btn)



        main_layout.addLayout(bottom)



        self.setLayout(main_layout)



        # Buttons

        self.send_btn.clicked.connect(
            self.send_message
        )


        self.input.returnPressed.connect(
            self.send_message
        )


        self.mic_btn.clicked.connect(
            self.voice_command
        )



        self.signals = WorkerSignals()

        self.signals.message.connect(
            self.add_message
        )



    # ---------------- TEXT MESSAGE ----------------


    def send_message(self):

        message = self.input.text().strip()


        if message == "":
            return


        self.add_message(
            f"<b>You:</b> {message}"
        )


        self.input.clear()


        thread = threading.Thread(
            target=self.process_ai,
            args=(message,)
        )

        thread.start()



    # ---------------- AI PROCESS ----------------


    def process_ai(self,message):

        response = process_message(message)


        self.signals.message.emit(
            f"<font color='#10A37F'><b>Jarvis:</b></font> {response}"
        )


        speak(str(response))



    # ---------------- VOICE COMMAND ----------------


    def voice_command(self):

        self.add_message(
            "<font color='yellow'>Listening...</font>"
        )


        thread = threading.Thread(
            target=self.voice_process
        )

        thread.start()



    def voice_process(self):

        command = listen()


        if command:

            self.signals.message.emit(
                f"<b>You:</b> {command}"
            )


            response = process_message(command)


            self.signals.message.emit(
                f"<font color='#10A37F'><b>Jarvis:</b></font> {response}"
            )


            speak(str(response))



    # ---------------- CHAT UPDATE ----------------


    def add_message(self,message):

        self.chat.append(message)





if __name__ == "__main__":


    app = QApplication(sys.argv)


    window = JarvisGUI()

    window.show()


    sys.exit(app.exec())