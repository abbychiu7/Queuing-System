import logger


def generate_summary():
    """Parse logs and produce a simple activity summary."""
    lines = logger.read_logs()
    issued = 0
    served = 0
    for line in lines:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 3:
            event = parts[1]
            if event == "ISSUE":
                issued += 1
            elif event == "SERVE":
                served += 1
    return {
        "issued": issued,
        "served": served,
        "in_queue": max(issued - served, 0),
    }
