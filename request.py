  Warning  FailedMount  8m56s (x2 over 36m)   kubelet            Unable to attach or mount volumes: unmounted volumes=[data], unattached volumes=[kube-api-access-k5bvh data]: timed out waiting for the condition
  Warning  FailedMount  3m30s (x14 over 42m)  kubelet            MountVolume.SetUp failed for volume "data" : mount failed: exit status 32
Mounting command: mount
Mounting arguments: -t nfs 172.30.56.144:/C:/CRZ-Test /var/lib/kubelet/pods/6bf07a7f-a2d3-4890-91c0-a654bfb939a3/volumes/kubernetes.io~nfs/data
Output: mount.nfs: Connection refused
  Warning  FailedMount  2m12s (x17 over 42m)  kubelet  Unable to attach or mount volumes: unmounted volumes=[data], unattached volumes=[data kube-api-access-k5bvh]: timed out waiting for the condition
