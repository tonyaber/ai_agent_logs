import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) - - \[(?P<dt>.*?)\] "(?P<method>\S+) (?P<path>\S+)'
    r' HTTP/\d\.\d" (?P<status>\d{3}) (?P<bytes>\d+)'
)

def parse_logs(logs):
    parsed = []

    for line in logs:
        match = LOG_PATTERN.search(line)
        if match:
            data = match.groupdict()
            data["status"] = int(data["status"])
            data["bytes"] = int(data["bytes"])
            parsed.append(data)

    return parsed