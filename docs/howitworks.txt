The distribution of nodes is a direct result of connecting users (clients) who build the network by connecting to nodes manually. After a while, nodes will learn the list of nodes on the network, and can distribute entire lists of running nodes to connecting clients who don't have a view of the network. Thus, each client has a unique view of the network which is based on the network model distributed by any broadcast nodes the client is connected to.

Protected networks
==================
Networks by default are joinable by any client. However, a number of security measures are available:

Authenticated 
-------------
An "auth" node is created on the network that stores valid username/password logins.

Password
--------
Each node can set a specific password that is required by joining clients. Thus, the password must be handed out to those who wish to connect. Not recommended for normal use, but included anyway.
