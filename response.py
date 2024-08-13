values

persistentVolume:
  name: cifs-pv
  server: //SBERORM-WIN-IFT
  shareName: CRZ-Test
  secretName: cifs-secret
  storageSize: 5Gi

persistentVolumeClaim:
  name: cifs-pvc
  storageSize: 5Gi



apiVersion: v1
kind: PersistentVolume
metadata:
  name: {{ .Values.persistentVolume.name }}
spec:
  capacity:
    storage: {{ .Values.persistentVolume.storageSize }}
  accessModes:
  - ReadWriteOnce
  cifs:
    secretRef:
      name: {{ .Values.persistentVolume.secretName }}
    server: {{ .Values.persistentVolume.server }}
    shareName: {{ .Values.persistentVolume.shareName }}
    readOnly: false
    
    
    
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: {{ .Values.persistentVolumeClaim.name }}
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: {{ .Values.persistentVolumeClaim.storageSize }}
    
    
    
    apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      containers:
      - name: my-container
        volumeMounts:
        - name: cifs-volume
          mountPath: /data
      volumes:
      - name: cifs-volume
        persistentVolumeClaim:
          claimName: {{ .Values.persistentVolumeClaim.name }}
        
        
        
        apiVersion: v1
kind: Secret
metadata:
  name: {{ .Values.persistentVolume.secretName }}
type: Opaque
stringData:
  username: {{ .Values.persistentVolume.username }}
  password: {{ .Values.persistentVolume.password }}
  domain: {{ .Values.persistentVolume.domain }}