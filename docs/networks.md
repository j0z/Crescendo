How it works
============
The distribution of nodes is a direct result of connecting users (clients) who build the network by connecting to broadcast nodes manually and request to be added to the list of broadcasted nodes. After a while, broadcast nodes will learn the list of nodes on the network, and can distribute entire lists of running nodes (broadcast or non) to connecting clients who don't have a view of the network. Thus, each client has a unique view of the network which is based on the network model distributed by any broadcast nodes the client is connected to.

Protected networks
==================
Networks by default are joinable by any client. However, a number of security measures are available.

Authenticated
-------------
An "auth" node is created on the network that stores valid username/password logins. The client must first connect and authenticate themselves before joining any other nodes on the network.

Dist-Auth (Multi-Auth)
---------
Distributed Authentication/Multiple Authentication. The network passes around an agreed-upon username/password database. The user must identify themselves with each auth node before the node is added to the network. This is a bit more secure, since a rogue auth node could not corrupt the entire network.

Password
--------
Each node can set a specific password that is required by joining clients. Thus, the password must be handed out to those who wish to connect. Not recommended for normal use, but included anyway.

Other security methods
======================

WARN
----
I've thought about a few possible attack scenarios. Most involve disgruntled users who want to break down a network via modified clients. I've developed WARN (*W*hy *AR*e you attacking this *N*ode) to combat a few forms of brute-force attacks. After a client fails to connect to a node a certain number of times, the IP of the attacking client is spread across the network in a `blk` packet. That specific client is then ignored by every node on the network for a certain amount of time.
