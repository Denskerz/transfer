podman-compose up -d
WARNING:podman_compose:WARNING: unused networks: server-networks
Traceback (most recent call last):
  File "/home/gpadmin/.local/bin/podman-compose", line 8, in <module>
    sys.exit(main())
  File "/home/gpadmin/.local/lib/python3.8/site-packages/podman_compose.py", line 3504, in main
    asyncio.run(async_main())
  File "/usr/local/lib/python3.8/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/local/lib/python3.8/asyncio/base_events.py", line 616, in run_until_complete
    return future.result()
  File "/home/gpadmin/.local/lib/python3.8/site-packages/podman_compose.py", line 3500, in async_main
    await podman_compose.run()
  File "/home/gpadmin/.local/lib/python3.8/site-packages/podman_compose.py", line 1741, in run
    self._parse_compose_file()
  File "/home/gpadmin/.local/lib/python3.8/site-packages/podman_compose.py", line 1927, in _parse_compose_file
    raise RuntimeError(f"missing networks: {missing_nets_str}")
RuntimeError: missing networks: server-network
