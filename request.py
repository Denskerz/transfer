
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}' | xargs -I {} ssh {} "apt-get list --installed | grep cifs-utils"