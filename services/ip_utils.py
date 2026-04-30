import ipaddress

def is_cidr(value):
    try:
        ipaddress.ip_network(value, strict=False)
        return True
    except ValueError:
        return False

def is_single_ip(value):
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False

def is_range(value):
    if not isinstance(value, str) or "-" not in value:
        return False

    start, end = value.split("-", 1)

    try:
        ip_start = ipaddress.ip_address(start)
        ip_end = ipaddress.ip_address(end)

        return type(ip_start) is type(ip_end)
    except ValueError:
        return False

def is_ip(value):
    if not isinstance(value, str):
        return False

    return is_single_ip(value) or is_cidr(value) or is_range(value)

def normalize_range(value):
    start, end = value.split("-", 1)
    return f"{start.strip()}-{end.strip()}"

def extract_ips(value):
    ips = set()

    if isinstance(value, dict):
        for v in value.values():
            ips.update(extract_ips(v))

    elif isinstance(value, list):
        for item in value:
            ips.update(extract_ips(item))

    elif is_ip(value):
        ips.add(normalize_range(value) if is_range(value) else value)

    return ips

def resolve_path(data, path):
    for key in path:
        data = data[key]
    return data

def collect_all_ips(data):
    return extract_ips(data)

def collect_ips(data, selected_paths):
    ips = set()

    for path in selected_paths:
        value = resolve_path(data, path)
        ips.update(extract_ips(value))

    return ips