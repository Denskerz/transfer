#values.yaml
global:
  namespace: bzi
  nexus:
    cred: nexus-cred 
    host: nexus3-ift.sigma-belpsb.by
    port: 5048

deployment:
  profile: ift
  replicas: 1
  port: 8040
  pullPolicy: Always
  image:
    tag: latest
    path: /excel-service
  resources:
    limits:
      cpu: '2'
      memory: '2Gi'
    requests:
      cpu: '2'
      memory: '2Gi'
  volumes:
    crz:
      mountPath: /excel-service/CRZ-Test
      server: 172.30.56.144
      path: /CRZ-Test
  initialDelay: 20
  period: 5        
  timeout: 3       

ingress:
  host: excel-service.apps.k8s-ift.sigma-belpsb.by
  rootPath: /*

#deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{.Chart.Name}}
  namespace: {{.Values.global.namespace}}
  labels:
    app: {{.Chart.Name}}
spec:
  replicas: {{.Values.deployment.replicas}}
  selector:
    matchLabels:
      app: {{.Chart.Name}}
  template:
    metadata:
      labels:
        app: {{.Chart.Name}}
    spec:
      containers:
        - name: {{.Chart.Name}}
          image: "{{ .Values.global.nexus.host }}:{{ .Values.global.nexus.port }}{{ .Values.deployment.image.path }}:{{ .Values.deployment.image.tag }}"
          imagePullPolicy: {{.Values.deployment.pullPolicy}}
          envFrom:
            - configMapRef:
                name: {{.Chart.Name}}-config
          resources:
            limits:
              cpu: {{.Values.deployment.resources.limits.cpu | quote}}
              memory: {{.Values.deployment.resources.limits.memory | quote}}
            requests:
              cpu: {{.Values.deployment.resources.requests.cpu | quote }}
              memory: {{.Values.deployment.resources.requests.memory | quote}}
          ports:
            - name: main-port
              containerPort: {{.Values.deployment.port}}
          volumeMounts:
            - name: crzdir
              mountPath: {{.Values.deployment.volumes.crz.mountPath}}

      imagePullSecrets:
        - name: {{.Values.global.nexus.cred}}
      volumes:
        - name: crzdir
          nfs:
            server: {{.Values.deployment.volumes.crz.server}}
            path: {{.Values.deployment.volumes.crz.path}}

А если я таким образом попробую прикрутить volume?
