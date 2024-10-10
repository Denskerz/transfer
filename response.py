# Убедитесь, что iptables установлен
sudo iptables -t nat -A POSTROUTING -p tcp --dport 80 -j SNAT --to-source <IP-хоста>:7110