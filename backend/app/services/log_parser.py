import re

LOG_PATTERN = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
    r'(?P<level>INFO|WARNING|ERROR) '
    r'(?P<message>.+)'
)

def parse_logs(lines):
    parsed = []

    for line in lines:
        match = LOG_PATTERN.match(line)
        if match:
            data = match.groupdict()

            # normalize to "status-like" semantics
            if data["level"] == "ERROR":
                data["status"] = 500
            elif data["level"] == "WARNING":
                data["status"] = 400
            else:
                data["status"] = 200

            parsed.append(data)

    return parsed
