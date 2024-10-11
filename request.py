10:34:14  + podman build -f docker/Dockerfile --format=docker --no-cache --pull-always -t nexus3-ift.sigma-belpsb.by:5001/images/gigachat_rag_service:202410111022 .
10:34:14  STEP 1/10: FROM nexus3-ift.sigma-belpsb.by:5001/images/ubi8-python38:latest
10:34:15  Trying to pull nexus3-ift.sigma-belpsb.by:5001/images/ubi8-python38:latest...
10:34:15  Getting image source signatures
10:34:15  Copying blob sha256:68be66ceca368ebe4a844b1821250d8d8c95fcdaa10e7699e9b378fedb47f798
10:34:15  Copying blob sha256:55e827cc6c85bbf96b303b2a1d283a64a0749752b2ffbce233c3578036ebfeb6
10:34:15  Copying blob sha256:0dbe531b0d7b1c6b3a4e24bad4cecdf2edc9ba16351a58879559723e453e63d9
10:34:15  Copying config sha256:ce7f5461dc494d9fa52e0ef2aa951a567fb7323f6be16405e5cba2fece67eb59
10:34:15  Writing manifest to image destination
10:34:15  Error: creating build container: creating container: creating read-write layer with ID "da1f45f1c12f0a6ca38e08608bc42b52956aee391022e7897448c05989715697": Stat /var/lib/jenkins/.local/share/containers/storage/overlay/b8c12644dfea82fa64fc5a3c3e926302d7bf7399fd237d17ae72ff28f6f8f380/diff: no such file or directory
