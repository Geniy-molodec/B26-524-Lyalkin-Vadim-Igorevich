import re

logs = [
    "2026-09-24 10:15:32 INFO User 123 logged in",
    "2026-09-24 10:16:04 ERROR User 456 authentication failed",
    "2026-09-24 10:17:21 INFO User 123 opened page",
    "2026-09-24 10:18:45 WARNING User 789 too many requests",
    "2026-09-24 10:19:02 ERROR User 123 database connection failed",
]

logs_2 = [
    # --- корректные строки ---
    "2026-09-24 10:20:00 INFO User 1 logged out",
    "2026-09-24 10:21:15 WARNING User 42 password expires soon",
    "2026-09-24 10:22:33 ERROR User 99999 payment failed: card declined",
    "2026-09-24 10:23:00 INFO User 007 opened settings",          # ведущие нули
    "2026-12-31 23:59:59 INFO User 3 session ended",              # граничные дата и время
    "2026-09-24 10:27:00 INFO User 12 message with 2026-09-24 date and User 77 inside",
    "2026-09-24 10:28:00 INFO User 5 a",                          # сообщение из одного символа

    # --- некорректные строки (должны дать None) ---
    "",
    "просто текст без структуры",
    "2026-09-24 10:30:00 DEBUG User 1 debug info",                # уровень не из списка
    "2026-09-24 10:31:00 info User 1 lower case level",           # нижний регистр
    "2026-09-24 10:32:00 INFO Server started",                    # нет пользователя
    "2026-09-24 10:33:00 INFO User abc logged in",                # id не число
    "2026-09-24 10:34:00 INFO User  logged in",                   # id отсутствует
    "2026-09-24 10:35:00 INFO User 5",                            # нет сообщения
    "2026-09-24 10:35:30 INFO User 5 ",                           # сообщение из одного пробела
    "2026-09-24 10:36 INFO User 5 no seconds",                    # нет секунд
    "24-09-2026 10:37:00 INFO User 5 wrong date format",          # другой формат даты
    "2026-09-24T10:38:00 INFO User 5 iso format",                 # T вместо пробела
    "INFO User 5 no datetime",                                    # нет даты
    "2026-09-24 10:39:00 User 5 no level",                        # нет уровня
]

log_re = re.compile(
    r"(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"(?P<level>INFO|WARNING|ERROR) "
    r"User (?P<user_id>\d+) "
    r"(?P<message>.+)"
)


def parse_log(line):
    m = log_re.fullmatch(line.strip())
    return m.groupdict() if m else None

for log in logs:
    print(parse_log(log))

for log in logs_2:
    print(parse_log(log))