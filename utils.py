import subprocess


IPTABLES_CMD = ["iptables"]


def accept_ip(ip: str) -> None:
    subprocess.run(IPTABLES_CMD + ["-I", "INPUT", "-s", ip, "-j", "ACCEPT"])
    # prerouting is needed for local traffic
    subprocess.run(IPTABLES_CMD + ["-I", "PREROUTING", "-s", ip, "-j", "ACCEPT"])