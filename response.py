Chain CNI-DN-ced8a516105815b5bdb6a (1 references)
 pkts bytes target     prot opt in     out     source               destination
    0     0 CNI-HOSTPORT-SETMARK  tcp  --  *      *       10.88.0.0/16         0.0.0.0/0            tcp dpt:7110
   16   960 CNI-HOSTPORT-SETMARK  tcp  --  *      *       127.0.0.1            0.0.0.0/0            tcp dpt:7110
   18  1080 DNAT       tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:7110 to:10.88.0.153:7110
