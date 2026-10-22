import re

text = """Полезные сайты: https://python.org, http://example.com/page,
https://example.com/docs/index.html и ftp://files.example.com/data."""

# --- дополнительные тесты ---
TEXT_2 = """\
Точка в конце: смотрите https://python.org.
Вопрос и восклицание: http://example.com/a? или https://example.com/b!
В скобках (https://example.com/c) и в кавычках «http://example.com/d».
Через точку с запятой: http://a.com/x;https://b.com/y; конец.
С параметрами: https://example.com/search?q=python&page=2
С якорем: http://example.com/docs#section-1
С портом: http://localhost:8080/api/v1
IP-адрес: http://192.168.1.10/admin
Поддомены: https://sub.domain.example.co.uk/path/to/page.html
Разные протоколы: ftp://files.example.com/data, mailto:user@example.com, file:///etc/passwd
Без протокола: www.example.com и example.com/page
Прилипло к слову: xhttp://bad.com и abchttps://bad.org
Регистр: HTTP://UPPER.COM и Https://Mixed.com
Только протокол: http:// и https://
Конец строки: https://last.example.com/end"""

url_re = re.compile(r"\bhttps?://[^\s,]+(?<![.,;:!?)}\]»])")

for url in url_re.findall(text):
    print(url)
for url in url_re.findall(TEXT_2):
    print(url)