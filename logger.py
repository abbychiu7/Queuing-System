from datetime import datetime

LOG_FILE = "ticket_logs.txt"


def write_log(event_type: str, data: dict):
    """Append a structured log line to the text file."""
    ts = datetime.now().isoformat(timespec="seconds")
    kv = " ".join([f"{k}={v}" for k, v in data.items()])
    line = f"{ts} | {event_type} | {kv}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)


def read_logs():
    """Return all log lines; empty list if file not found."""
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []
