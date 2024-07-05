import webbrowser


def fetchUrl():
    url_array = [
        "https://mail.google.com/chat/u/0/#chat/home",
        "https://mail.google.com/mail/u/0/#inbox",
        "https://calendar.google.com/calendar/u/0/r"
    ]

    for url in url_array:
        print(url)
        webbrowser.open(url, new=1, autoraise=True)


def main():
    fetchUrl()


if __name__ == "__main__":
    main()

