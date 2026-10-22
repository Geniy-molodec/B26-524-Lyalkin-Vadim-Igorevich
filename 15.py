from io import StringIO
def count_lines(stream):
    return len(stream.readlines())
with open("data.txt", mode="w", encoding="utf-8") as f:
    f.write("first\nsecond\nthird\nfourth")
with open("data.txt", mode="r", encoding="utf-8") as f:
    print(count_lines(f))
print(count_lines(StringIO("first\nsecond\nthird")))
