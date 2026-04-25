def chunk_list(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]


def generate_firewall_rules(exe_path, ips, chunk_size=50):
    rules = []
    ip_list = sorted(ips)

    use_program = bool(exe_path)

    for i, chunk in enumerate(chunk_list(ip_list, chunk_size), start=1):
        ip_string = ",".join(chunk)

        if use_program:
            rule = (
                f'New-NetFirewallRule '
                f'-DisplayName "FirewallTool Block {i}" '
                f'-Direction Outbound '
                f'-Action Block '
                f'-RemoteAddress {ip_string} '
                f'-Program "{exe_path}"'
            )
        else:
            rule = (
                f'New-NetFirewallRule '
                f'-DisplayName "FirewallTool Block {i}" '
                f'-Direction Outbound '
                f'-Action Block '
                f'-RemoteAddress {ip_string}'
            )

        rules.append(rule)

    return rules