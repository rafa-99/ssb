import subprocess

def chunk_list(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]

def generate_firewall_rules(exe_path, ips, label="", chunk_size=50):
    rules = []
    ip_list = sorted(ips)

    use_program = bool(exe_path)

    for i, chunk in enumerate(chunk_list(ip_list, chunk_size), start=1):
        ip_string = ",".join(chunk)

        rule = (
            f'New-NetFirewallRule '
            f'-DisplayName "ssb Block{label} {i}" '
            f'-Direction Outbound '
            f'-Action Block '
            f'-RemoteAddress {ip_string}'
        )

        if use_program:
            rule += f' -Program "{exe_path}"'

        rules.append(rule)

    return rules

def apply_rules(rules):
    for rule in rules:
        subprocess.run(
            ["powershell", "-Command", rule],
            shell=True
        )

def remove_rules():
    command = (
        'Get-NetFirewallRule | '
        'Where-Object {$_.DisplayName -like "ssb Block*"} | '
        'Remove-NetFirewallRule'
    )

    subprocess.run(
        ["powershell", "-Command", command],
        shell=True
    )

def count_rules():
    command = (
        'Get-NetFirewallRule | '
        'Where-Object {$_.DisplayName -like "ssb Block*"} | '
        'Measure-Object | '
        'Select-Object -ExpandProperty Count'
    )

    result = subprocess.run(
        ["powershell", "-Command", command],
        capture_output=True,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW
    )

    try:
        return int(result.stdout.strip())
    except:
        return 0