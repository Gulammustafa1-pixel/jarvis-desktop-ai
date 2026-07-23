from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton,
)

from agent.brain import process_message


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Desktop AI Agent")
        self.resize(900, 650)

        layout = QVBoxLayout()

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Ask me anything...")

        self.send_button = QPushButton("Send")

        layout.addWidget(self.chat_area)
        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

        # Events
        self.send_button.clicked.connect(self.send_message)
        self.input_box.returnPressed.connect(self.send_message)

    def send_message(self):
        user_message = self.input_box.text().strip()

        if not user_message:
            return

        self.chat_area.append(f"<b>You:</b> {user_message}")

        reply = process_message(user_message)

        self.chat_area.append(f"<b>Agent:</b> {reply}")
        self.chat_area.append("")

        self.input_box.clear()