apiVersion: v1
kind: PersistentVolume
metadata:
  name: {{ .Values.persistentVolume.name }}
spec:
  capacity:
    storage: {{ .Values.persistentVolume.storageSize }}
  accessModes:
  - ReadWriteOnce
  nfs:
    server: {{ .Values.persistentVolume.server }}
    path: {{ .Values.persistentVolume.shareName }}
    
    persistentVolume:
  name: cifs-pv
  server: nfs-server.default.svc.cluster.local
  shareName: /shared
  secretName: nfs-secret
  storageSize: 100Gi

persistentVolumeClaim:
  name: cifs-pvc
  storageSize: 100Gi
  
  
  apiVersion: v1
kind: Secret
metadata:
  name: {{ .Values.persistentVolume.secretName }}
type: Opaque
stringData:
  username: {{ .Values.persistentVolume.username }}
  password: {{ .Values.persistentVolume.password }}