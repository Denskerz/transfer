apiVersion: v1  
kind: ConfigMap
metadata:
  name: cifs-mount
data:
  mount-options: 'username=eroshevich_d,password=12345678,workgroup=sigma-belpsb.by'

  volumeMounts:
  - name: cifs-mount  
    mountPath: /mount/path
  env:
  - name: MOUNT_OPTIONS
    valueFrom:
      configMapKeyRef:
        name: cifs-mount 
        key: mount-options
        
volumes:
- name: cifs-mount
  cifs:
    server: //SBERORM-WIN-IFT/CRZ-Test
    path: /mount/path
    securityStyle: unix
    volumeOptions:
      opect: {{.data.MOUNT_OPTIONS}}  