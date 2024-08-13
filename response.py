apiVersion: v1
kind: Secret
metadata:
  name: {{ .Values.persistentVolume.secretName }}
type: Opaque
data:
  username: ZXJvc2hldmljaF9k
  password: MjAwMl9EZW5za2Vyenp6
  domain: c2lnbWEtYmVscHNiLmJ5
