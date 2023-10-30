echo "Starting up captive portal"
# Allow DNS
iptables -A FORWARD -i wlan0 -p udp --dport 53 -j ACCEPT
iptables -A FORWARD -i wlan0 -p tcp --dport 53 -j ACCEPT
# Allow captive portal and port-forwarding
iptables -A FORWARD -i wlan0 -p tcp --dport 80 -d $PORTAL_IP -j ACCEPT
# Block all incoming traffic
iptables -A FORWARD -j DROP -i wlan0
# Redirecting all traffic to captive portal
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 80 -j DNAT --to-destination $PORTAL_IP