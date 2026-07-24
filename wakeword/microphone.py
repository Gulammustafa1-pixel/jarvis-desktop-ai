import pyaudio


RATE = 16000
CHUNK = 1280


class Microphone:

    def __init__(self):

        self.audio = pyaudio.PyAudio()

        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK
        )


    def read(self):

        return self.stream.read(
            CHUNK,
            exception_on_overflow=False
        )


    def close(self):

        self.stream.stop_stream()

        self.stream.close()

        self.audio.terminate()