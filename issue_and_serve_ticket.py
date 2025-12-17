from collections import deque

_queue = deque()
_next_id = 1


def issue_ticket(name: str) -> int:
    """Add a ticket to the queue and return its ID."""
    global _next_id
    tid = _next_id
    _next_id += 1
    _queue.append({"id": tid, "name": name})
    return tid


def serve_ticket():
    """Remove and return the next ticket, or None if empty."""
    return _queue.popleft() if _queue else None


def get_queue():
    """Return a snapshot list of the queue."""
    return list(_queue)


def reset_state():
    """Utility for tests: reset queue and IDs."""
    global _queue, _next_id
    _queue.clear()
    _next_id = 1
