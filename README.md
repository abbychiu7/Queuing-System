# Queuing-System
APPDAET Final Project
Python console application: a single FIFO queue with persistent logs in `ticket_logs.txt`.

---

## Run
- Python 3.9+
- `python main.py`

---

## Features
- Issue ticket
- Serve ticket
- View queue
- View logs
- Summary report

---

## Design
- Queue: `collections.deque.`
- Log format: `timestamp | EVENT | key=value ...`

---

## File Ownership
| File               | Owner  |
|--------------------|--------|
| main.py            | Justin |
| menu.py            | Justin |
| queue_manager.py   | Trina  |
| logger.py          | Abby   |
| reports.py         | Abby   |
| ticket_logs.txt    | Abby   |
| README.md          | All    |

---

## Branch Workflow
- `main` – stable/final code 
- `develop` – integration branch (for merging only)
- `feature/<name-task>` – individual work branch

---

### Clone Repository
1. Clone repo:
```bash
git clone https://github.com/abbychiu7/Queuing-System.git
cd Queuing-System

