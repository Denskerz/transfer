podman-compose up -d
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
  File "/home/gpadmin/.local/lib/python3.8/site-packages/podman_compose.py", line 1743, in run
    retcode = await cmd(self, args)
  File "/home/gpadmin/.local/lib/python3.8/site-packages/podman_compose.py", line 2470, in compose_up
    await compose.podman.output(
  File "/home/gpadmin/.local/lib/python3.8/site-packages/podman_compose.py", line 1362, in output
    raise subprocess.CalledProcessError(p.returncode, " ".join(cmd_ls), stderr_data)
subprocess.CalledProcessError: Command 'podman ps --filter label=io.podman.compose.project=server -a --format {{ index .Labels "io.podman.compose.config-hash"}}' returned non-zero exit status 125.
