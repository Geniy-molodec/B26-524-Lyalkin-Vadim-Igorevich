import json
import logging
import re
import sys
from collections import Counter
from pathlib import Path

LOG_FILE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("access.log")
OUTPUT_FILE = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("stats.json")
PROGRESS_EVERY = 100_000

# 2026-09-23 10:00:01 192.168.1.10 GET /index.html 200
LINE_RE = re.compile(
    r"(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) "
    r"(?P<method>[A-Z]+) "
    r"(?P<url>\S+) "
    r"(?P<status>\d{3})"
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("processing.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger("access_stats")


def process(path: Path) -> dict:
    methods = Counter()
    urls = Counter()
    total = 0
    errors_4xx = 0
    skipped = 0

    with open(path, encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            line = line.rstrip("\r\n")
            if not line:
                continue

            m = LINE_RE.fullmatch(line)
            if not m:
                skipped += 1
                logger.warning("Строка %d пропущена (неверный формат): %r", lineno, line)
                continue

            total += 1
            methods[m["method"]] += 1
            urls[m["url"]] += 1
            if m["status"].startswith("4"):
                errors_4xx += 1

            if total % PROGRESS_EVERY == 0:
                logger.info("Обработано запросов: %d", total)

    top_url = None
    if urls:
        url, count = urls.most_common(1)[0]
        top_url = {"url": url, "count": count}

    return {
        "total_requests": total,
        "requests_by_method": dict(methods),
        "errors_4xx": errors_4xx,
        "most_common_url": top_url,
        "skipped_lines": skipped,
    }


def save_json(stats: dict, path: Path) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)


def main() -> int:
    logger.info("Начало обработки файла %s", LOG_FILE)

    try:
        stats = process(LOG_FILE)
    except FileNotFoundError:
        logger.error("Файл не найден: %s", LOG_FILE)
        return 1
    except PermissionError:
        logger.error("Нет прав на чтение файла: %s", LOG_FILE)
        return 1
    except UnicodeDecodeError as e:
        logger.error("Ошибка кодировки в %s: %s", LOG_FILE, e)
        return 1
    except OSError as e:
        logger.error("Ошибка чтения файла %s: %s", LOG_FILE, e)
        return 1

    logger.info("Обработка завершена: запросов %d, пропущено строк %d",
                stats["total_requests"], stats["skipped_lines"])

    try:
        save_json(stats, OUTPUT_FILE)
    except OSError as e:
        logger.error("Не удалось записать %s: %s", OUTPUT_FILE, e)
        return 1

    logger.info("Статистика сохранена в %s", OUTPUT_FILE)
    return 0


if __name__ == "__main__":
    sys.exit(main())