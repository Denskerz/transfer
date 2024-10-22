sudo /usr/local/bin/podman-compose up -d
Traceback (most recent call last):
  File "/usr/local/bin/podman-compose", line 11, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.6/site-packages/podman_compose.py", line 3504, in main
    asyncio.run(async_main())
AttributeError: module 'asyncio' has no attribute 'run'
