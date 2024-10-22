python3.8 -m pip install podman-compose
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: http://nexus3-prod.belpsb.by:8081/repository/pypi-proxy/simple
Collecting podman-compose
  Downloading http://nexus3-prod.belpsb.by:8081/repository/pypi-proxy/packages/podman-compose/1.2.0/podman_compose-1.2.0-py2.py3-none-any.whl (39 kB)
Requirement already satisfied: python-dotenv in /home/gpadmin/.local/lib/python3.8/site-packages (from podman-compose) (1.0.1)
Requirement already satisfied: pyyaml in /home/gpadmin/.local/lib/python3.8/site-packages (from podman-compose) (6.0.2)
Installing collected packages: podman-compose
Successfully installed podman-compose-1.2.0
[gpadmin@dbsnode22-p server]$ which podman-compose
~/.local/bin/podman-compose
[gpadmin@dbsnode22-p server]$ sudo ~/.local/bin/podman-compose up -d
Traceback (most recent call last):
  File "/home/gpadmin/.local/bin/podman-compose", line 5, in <module>
    from podman_compose import main
ModuleNotFoundError: No module named 'podman_compose'
