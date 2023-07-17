# 0x13. Firewall

A firewall is a network security device or software that acts as a barrier between an internal network (such as a private or corporate network) and external networks (such as the internet). Its primary purpose is to control and monitor incoming and outgoing network traffic based on predetermined security rules.

## 0-block_all_incoming_traffic_but

Install ufw firewall and configure it to block all incoming traffic, except TCP ports:
22 (SSH)
443 (HTTPS SSL)
80 (HTTP)

## 100-port_forwarding

Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.

