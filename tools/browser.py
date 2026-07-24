import webbrowser
import urllib.parse


def google_search(query):
    url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
    webbrowser.open(url)
    return f"Searching Google for {query}."


def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube."


def open_github():
    webbrowser.open("https://github.com")
    return "Opening GitHub."


def open_linkedin():
    webbrowser.open("https://www.linkedin.com")
    return "Opening LinkedIn."