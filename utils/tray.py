import threading


def start_tray():

    print("TRAY STARTED")

    import pystray
    from PIL import Image, ImageDraw


    image = Image.new(
        "RGB",
        (64, 64),
        "black"
    )


    draw = ImageDraw.Draw(image)


    draw.text(
        (20, 20),
        "J",
        fill="white"
    )


    icon = pystray.Icon(
        "Jarvis",
        image,
        "Jarvis AI"
    )


    print("ICON RUNNING")


    icon.run()



def run_tray():

    thread = threading.Thread(
        target=start_tray,
        daemon=True
    )

    thread.start()