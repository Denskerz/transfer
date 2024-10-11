09:40:20  + podman build -f docker/Dockerfile --format=docker --no-cache --pull-always -t nexus3-ift.sigma-belpsb.by:5001/images/gigachat_rag_service:202410110929 .
09:40:20  STEP 1/10: FROM nexus3-ift.sigma-belpsb.by:5001/images/ubi9-python311:latest
09:40:20  Trying to pull nexus3-ift.sigma-belpsb.by:5001/images/ubi9-python311:latest...
09:40:21  Getting image source signatures
09:40:21  Copying blob sha256:b7af5bed306dcea702d787c2b9c02d07d773742500c0213475289f7837cc0fcd
09:40:21  Copying blob sha256:c20470d0be35939741977f0ca184f1072d55e7d5cff1e9c4d7cb9baa9de9c9fb
09:40:21  Copying blob sha256:fcb3b197a73b700abaa9ba089b6e96d570365ce9ff0e4b355ba04c4b5fd8a590
09:40:21  Copying blob sha256:edab65b863aead24e3ed77cea194b6562143049a9307cd48f86b542db9eecb6e
09:40:21  Copying config sha256:6bd2491384b098e2d175f9452aab07b9ffa23ca05ca937e1f02d6959cb11fc7e
09:40:21  Writing manifest to image destination
09:40:21  Error: creating build container: creating container: creating read-write layer with ID "97bfd7831bb37a6c18aee7afa414ae8e32479788546d41119bbc57222644e300": Stat /var/lib/jenkins/.local/share/containers/storage/overlay/5669cc385d32c72282366710f375edf0559086f8f0474c52715b9fabe2036503/diff: no such file or directory
