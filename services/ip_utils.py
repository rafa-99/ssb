import re

IP_REGEX = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?$")


def is_ip(value):
    return isinstance(value, str) and IP_REGEX.match(value)


def extract_ips(value):
    ips = set()

    if isinstance(value, dict):
        for v in value.values():
            ips.update(extract_ips(v))

    elif isinstance(value, list):
        for item in value:
            ips.update(extract_ips(item))

    elif is_ip(value):
        ips.add(value)

    return ips


def resolve_path(data, path):
    for key in path:
        data = data[key]
    return data


def collect_ips(data, selected_paths):
    ips = set()

    for path in selected_paths:
        value = resolve_path(data, path)
        ips.update(extract_ips(value))

    return ips