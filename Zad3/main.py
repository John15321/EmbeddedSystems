"""
Opracuj program, korzystający z wyrażeń regularnych zmień przykładowy nagłówek wiadomości

From: author@example.com

User-Agent: Thunderbird 1.5.0.9 (X11/20061227)

MIME-Version: 1.0

To: editor@example.com



w słownik.
"""

import re

# .+:
# [^:]*$
def zad3(msg):
    for each in re.finditer(r".+:", msg):
        print(each)

if __name__ == "__main__":
    msg = """From: author@example.com

User-Agent: Thunderbird 1.5.0.9 (X11/20061227)

MIME-Version: 1.0

To: editor@example.com"""
zad3(msg)