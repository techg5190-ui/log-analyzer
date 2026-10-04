# 🛡️ SentinelLog

> **Lightweight Server Log Threat Detector: spot noisy IPs, HTTP errors, and brute-force attempts in seconds.**

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

---

## 📖 About

**SentinelLog** is a lightweight Python security tool that analyzes server logs, identifies high-traffic IP addresses, summarizes HTTP errors, and detects repeated failed-login attempts that may indicate brute-force attacks.

It is built for developers, students, and small teams who need quick answers from a raw log file without setting up a full SIEM or log-aggregation stack. Point it at a log, get a readable security summary.

---

## 📸 Screenshot

<!-- Replace this with a real screenshot of your terminal output -->
![SentinelLog sample output](docs/screenshot.png)

*Add a screenshot at `docs/screenshot.png` to make this section appear.*

---

## ✨ Key Features

- **Top-talker detection:** ranks the IP addresses generating the most requests, so traffic spikes and scrapers stand out immediately.
- **HTTP error summary:** counts and groups 4xx and 5xx responses so you can see what is failing and how often.
- **Brute-force detection:** flags IPs with repeated failed-login attempts that exceed a configurable threshold.
- **Lightweight and fast:** pure Python, no heavy dependencies, and it reads the log file line by line.
- **Readable reports:** clean terminal output that you can understand at a glance.

---

## 🚀 Quick Start (under 5 minutes)

### Prerequisites

- **Python 3.8 or newer** (check with `python --version`)
- **Git**

### 1. Clone the repository

```bash
git clone https://github.com/techg5190-ui/log-analyzer.git
cd log-analyzer
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If the project has no `requirements.txt`, it uses only the Python standard library and you can skip this step.

### 4. Run the analyzer

```bash
python log_analyzer.py path/to/your/access.log
```

That is it. SentinelLog will print a summary of top IPs, HTTP errors, and suspected brute-force activity.

---

## 🧪 Usage

### Basic run

```bash
python log_analyzer.py access.log
```

### Expected log format

SentinelLog expects standard web-server access logs (Apache or Nginx *combined* format), for example:

```text
203.0.113.7 - - [04/Oct/2026:10:15:32 +0000] "POST /login HTTP/1.1" 401 512
203.0.113.7 - - [04/Oct/2026:10:15:34 +0000] "POST /login HTTP/1.1" 401 512
198.51.100.22 - - [04/Oct/2026:10:16:01 +0000] "GET /index.html HTTP/1.1" 200 2048
```

### Example output

> *Illustrative sample. Your numbers will differ.*

```text
=== SentinelLog Report ===

[Top IP Addresses]
  203.0.113.7      482 requests
  198.51.100.22    131 requests

[HTTP Error Summary]
  401 Unauthorized     96
  404 Not Found        41
  500 Server Error      3

[⚠ Possible Brute-Force Activity]
  203.0.113.7  ->  27 failed login attempts
```

---

## 🧠 How It Works

1. **Parse:** each log line is read and the IP address, timestamp, request, and status code are extracted.
2. **Aggregate:** requests are counted per IP, and responses are grouped by HTTP status code.
3. **Detect:** failed-login responses are tallied per IP, and any IP above the threshold is flagged as a suspected brute-force source.

---

## 🗂️ Project Structure

```text
log-analyzer/
├── log_analyzer.py      # Main script
├── requirements.txt     # Dependencies (if any)
├── sample_logs/         # Example logs for testing
├── docs/                # Screenshots
└── README.md
```

---

## 🛣️ Roadmap

- [ ] Configurable brute-force threshold via command-line flag
- [ ] Export reports to JSON and CSV
- [ ] Time-window analysis (attempts per minute)
- [ ] GeoIP lookup for flagged addresses

---

## 🤝 Contributing

Contributions are welcome. Fork the repo, create a feature branch, commit your changes, and open a pull request.

---

## ⚠️ Disclaimer

SentinelLog is a lightweight analysis aid, not a replacement for a full intrusion-detection system. Use it only on logs you own or are authorized to analyze.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## 🏷️ Tags

`python` `security` `log-analysis` `log-analyzer` `threat-detection` `brute-force-detection` `cybersecurity` `blue-team` `server-logs` `http-errors` `intrusion-detection` `command-line-tool`
