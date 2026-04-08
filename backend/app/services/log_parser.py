import re

LOG_PATTERN = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} '
    r'\d{2}:\d{2}:\d{2},\d{3}) '
    r'(?P<level>INFO|WARNING|ERROR) '
    r'(?P<message>.+)'
)

def parse_logs(lines):
    return lines
    # code for parsing logs
    # parsed = []

    # for line in lines:
    #     print(line)
    #     match = LOG_PATTERN.match(line)
    #     print(match)
    #     if not match:
    #         continue

    #     data = match.groupdict()

    #     # Map log level to status-like severity
    #     if data["level"] == "ERROR":
    #         data["status"] = 500
    #     elif data["level"] == "WARNING":
    #         data["status"] = 400
    #     else:
    #         data["status"] = 200

    #     parsed.append(data)

    # return parsed

