/values.yaml:

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
  initialDelay: 20
  period: 5        
  timeout: 3       

ingress:
  host: excel-service.apps.k8s-ift.sigma-belpsb.by
  rootPath: /*


/templates/ingress.yaml:

apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{ .Chart.Name }}-ingress
  namespace: {{ .Values.global.namespace }}
  annotations:
    nginx.ingress.kubernetes.io/use-regex: "true"
  labels:
    app: {{ .Chart.Name }}
spec:
  rules:
    - host: {{ .Values.ingress.host }}
      http:
        paths:
          - path: {{ .Values.ingress.rootPath }}
            pathType: Prefix
            backend:
              service:
                name: {{ .Chart.Name }}-service
                port:
                  number: {{ .Values.deployment.port }}



