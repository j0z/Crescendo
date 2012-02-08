Crescendo v0.1
==============
Crescendo is a unique peer-to-peer file sharing program written in Python. It was developed by me, [flags,](http://jetstarforever.com/site/) in about two weeks. First as a proof-of-concept, things quickly got out of hand and it ended up as a serious project. Several revisions later, it's now ready to be tested.

Warning
-------
Crescendo is, at this point in time, not entirely secure. There are a few things that could potentially be exploited if you pushed in the right places, but not much damage can be done (*probably* none.)

In addition, not all variables have been implemented yet. Therefore, the below examples for `config.conf` and `node.conf` should be used. Custom configs will not work completely. Why?

The next "big thing" I have to do is implement network profiles. This will allow you to connect to a variety of nodes via the UI. It's a long process, though, and I've logged many, many hours into this project and just want to get a version out to the public to see the reaction (if any.)

Installation
------------
By default, Crescendo contains no configuration files and will NOT run out-of-box. You'll need to do two things:

#Create config.conf
This is read by the client, and sets up a few things:

`node_name`: This isn't used at the moment. You'll still need it, though.
`host`: Your local IP:port. Port should be 9001.
`save_dir`: Where Crescendo will store downloaded items.

##Example: 
    {"node_name":"flagship",
    "host":["10.234.16.131",9001],
    "save_dir":"downloads"}

#Create node.conf
This is read by the server (node.)

`name`: The name of your node. Other clients will see this.
`searchable`: `true` if you want to be broadcasted by broadcast nodes.
`broadcast`: `true` if you want to help distribute clients on the network.
`broadcast_every`: Frequency at which broadcast packets are sent (in seconds.) Only if `broadcast` is set to `true`.
`security`: `auth` or `pass`. Explained below.
`authdb`: If `security` is set to `auth`, this value is read. Should point to a file that looks like this:

`{"users":[{"usr":"test","pas":"test"}]}`

`passwd`: If `security` is set to `pass`, this value is read. Should be a sha224 hash.
`share_dir`: The directory you want to share.
`ignore_filename`: Files with names similar to the ones in this list are ignored.
`ignore_filetypes`: Files with this extension are ignored.

##Example
    {"name":"flagship",
    "searchable":true,
    "broadcast":true,
    "broadcast_every":"5",
    "security":"auth",
    "authdb":"auth.db",
    "passwd":"22c7d75bd36e271adc1ef873aee4f95db6bc54a9c2f9f4bcf0cd18a8",
    "share_dir":"files",
    "ignore_filename":["-sample"],
    "ignore_filetypes":["sfv","srr","nfo","nzb"]}

Running
-------
`crescendo_qt.py`: Runs both the client and the server in a nice GUI. Arguments are: `-noserver`, which runs the UI without the server, and `-metro` which is a great alternative GUI designed by `j0z`. By default, my boring UI is used.

`crescendo_server.py`: Runs the server by itself.

Helping
-------
I need testers to deploy Crescendo and see how it works in other networks. I've only been able to test with four nodes, and would like to see how it fares in a larger environment.

Credits
-------
`flags`: Coding, UI, design.

`j0z`: Metro UI, design, tester.

Quote from the author
---------------------
David Letterman is on.

Special Thanks
--------------
The members of #xenn.org
Whoever makes [twisted](http://twistedmatrix.com/trac/)
Various [Stack Overflow](http://stackoverflow.com/) threads