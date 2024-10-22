sudo  /usr/local/bin/podman-compose up -d
06557fd6cbcd08c6c216130cb2633da58ab0281c2bbe9a799edcb457a1930f28
Traceback (most recent call last):
  File "/usr/local/bin/podman-compose", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.8/site-packages/podman_compose.py", line 3504, in main
    asyncio.run(async_main())
  File "/usr/lib64/python3.8/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib64/python3.8/asyncio/base_events.py", line 616, in run_until_complete
    return future.result()
  File "/usr/local/lib/python3.8/site-packages/podman_compose.py", line 3500, in async_main
    await podman_compose.run()
  File "/usr/local/lib/python3.8/site-packages/podman_compose.py", line 1743, in run
    retcode = await cmd(self, args)
  File "/usr/local/lib/python3.8/site-packages/podman_compose.py", line 2500, in compose_up
    podman_args = await container_to_args(compose, cnt, detached=args.detach)
  File "/usr/local/lib/python3.8/site-packages/podman_compose.py", line 1095, in container_to_args
    podman_args.extend(get_net_args(compose, cnt))
  File "/usr/local/lib/python3.8/site-packages/podman_compose.py", line 955, in get_net_args
    multiple_nets = {net: net_config or {} for net, net_config in multiple_nets.items()}
AttributeError: 'str' object has no attribute 'items'
