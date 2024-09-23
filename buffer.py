persistentVolume и persistentVolumeClaim уже прописаны в кубере
persistentVolume:
apiVersion: v1
kind: PersistentVolume
metadata:
  finalizers:
  - kubernetes.io/pv-protection
  name: pv-smb-bzi-crz-dispatcher
spec:
  accessModes:
  - ReadWriteMany
  capacity:
    storage: 200Gi
  claimRef:
    apiVersion: v1
    kind: PersistentVolumeClaim
    name: pvc-smb-bzi-crz-dispatcher
    namespace: bzi
  csi:
    driver: smb.csi.k8s.io
    nodeStageSecretRef:
      name: pv-creds-cifs-bzi
      namespace: kube-system
    volumeAttributes:
      source: //pdc-psi.belpsb.by/crz-dispatcher
    volumeHandle: cifs-csi-bzi-crz-dispatcher
  mountOptions:
  - dir_mode=0755
  - file_mode=0644
  - uid=1001
  - gid=1001
  - noperm
  - mfsymlinks
  - cache=strict
  - noserverino
  - vers=3.0
  persistentVolumeReclaimPolicy: Retain
  storageClassName: smb
  volumeMode: Filesystem

persistentVolumeClaim:
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  finalizers:
  - kubernetes.io/pvc-protection
  name: pvc-smb-bzi-crz-dispatcher
  namespace: bzi
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 200Gi
  storageClassName: smb
  volumeMode: Filesystem
  volumeName: pv-smb-bzi-crz-dispatcher

как теперь в моих хелмчартах прописать secret с user: BZI_Tech и password: 12345678, чтобы использовать pvc?

