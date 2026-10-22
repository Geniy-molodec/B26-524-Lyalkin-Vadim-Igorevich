import re
with open("contacts.txt", mode="r", encoding="utf-8") as f:
    text=f.read()
    emails=re.findall(r".+@.+\..+", text)
    emails=list(set(emails))
    for email in emails:
        print(email)
