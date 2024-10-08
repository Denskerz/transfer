15:53:58  task path: /var/lib/jenkins/workspace/DataScience/rbl_model_service/rbl_model_service_deploy-host/rbl_model_service/ansible/roles/rbl_model_service/tasks/main.yaml:85
15:53:59  fatal: [dev]: FAILED! => {"changed": true, "cmd": "/bin/podman run  -ti -d  --restart always  --name \"rbl_model_service\" -e FLASK_APP=\"/opt/rbl_model_service/main.py\"  -e PYAPP=main.py  -e PYAPP_HOME=\"/opt/rbl_model_service\" -v \"/opt/deploy/rbl_model_service\":\"/opt/rbl_model_service/external_dir\"  -p 7001:7001  \"172.30.71.8:5001/images/rbl_model_service:202401301725\"  bash -l -c \"/bin/bash\" #bash -l -c \"python3 -m uvicorn --host 0.0.0.0 --port 7010 main:app\"\n", "delta": "0:00:00.592211", "end": "2024-02-26 15:53:59.803752", "msg": "non-zero return code", "rc": 126, "start": "2024-02-26 15:53:59.211541", "stderr": "Error: cannot listen on the TCP port: listen tcp4 :7001: bind: address already in use", "stderr_lines": ["Error: cannot listen on the TCP port: listen tcp4 :7001: bind: address already in use"], "stdout": "", "stdout_lines": []}

17:26:59  ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'docker/requirements.txt'
17:27:21  Error: building at STEP "RUN pip3 install -r docker/requirements.txt": while running runtime: exit status 1

ssh: connect to host 10.244.226.121 port 22: Connection timed out
