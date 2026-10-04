import re
from collections import Counter
from datetime import datetime

LOG_FILE = "server.log"

FAILED_LOGIN_LIMIT = 3


def read_logs(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []


def extract_ip(line):
    match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)
    return match.group() if match else None


def extract_status_code(line):
    match = re.search(r"\s(\d{3})\s", line)
    return match.group(1) if match else None


def analyze_logs(logs):
    ip_counter = Counter()
    status_counter = Counter()
    failed_logins = Counter()

    for line in logs:
        ip = extract_ip(line)
        status = extract_status_code(line)

        if ip:
            ip_counter[ip] += 1

        if status:
            status_counter[status] += 1

        if "FAILED_LOGIN" in line and ip:
            failed_logins[ip] += 1

    return ip_counter, status_counter, failed_logins


def detect_suspicious_ips(failed_logins):
    suspicious_ips = []

    for ip, attempts in failed_logins.items():
        if attempts >= FAILED_LOGIN_LIMIT:
            suspicious_ips.append((ip, attempts))

    return suspicious_ips


def print_report(ip_counter, status_counter, suspicious_ips):
    print("\n" + "=" * 50)
    print("SERVER LOG ANALYSIS REPORT")
    print("=" * 50)

    print(f"\nGenerated at: {datetime.now()}")

    print("\nTop IP addresses:")

    for ip, count in ip_counter.most_common(5):
        print(f"{ip:<20} {count} requests")

    print("\nHTTP Status Codes:")

    for status, count in status_counter.items():
        print(f"{status}: {count}")

    print("\nSuspicious IP Addresses:")

    if suspicious_ips:
        for ip, attempts in suspicious_ips:
            print(f"[WARNING] {ip} -> {attempts} failed login attempts")
    else:
        print("No suspicious activity detected.")

    print("\n" + "=" * 50)


def main():
    logs = read_logs(LOG_FILE)

    if not logs:
        return

    ip_counter, status_counter, failed_logins = analyze_logs(logs)

    suspicious_ips = detect_suspicious_ips(failed_logins)

    print_report(ip_counter, status_counter, suspicious_ips)


if __name__ == "__main__":
    main()