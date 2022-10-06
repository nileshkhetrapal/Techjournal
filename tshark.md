Tshark- Wireshark on terminal

Use cases:

Capturing network packets and exporting them to a PCAP file

Analyzing PCAP files

First Use case:

List the interfaces available to tshark:

```bash
tshark -d
```

Use the -i flag to determine the interface to use:

```bash
tshark -i eth0
```

Use the -w flag to write to a pcap file. Enter this command to start and ctrl+c to stop the capture.

```bash
tshark -i eth0 -w capture1.pcap
```

Protocol filtering can be done by appending the command with the protocol. This is done for icmp:

```bash
tshark -i eth0 icmp
tshark -i eth0 -w capture1.pcap icmp
```

You can combine protocol and port filters together. This is done for telnet:

```bash
tshark -i eth0 -w capture1.pcap tcp port 23 #telnet works on tcp port 23
```

Setup:

cat /etc/network/interfaces

Second use case:

Read pcap files:

```bash
tshark -r capture1.pcap
```

Follow tcp stream (telnet): The 0 here represents the first stream.

```bash
tshark -nr capture1.pcap -q -z follow,tcp,ascii,0
```

-n : disable network object name resolution (hostname, tcp, udp port names)

-z : enable statistics. It has a wide variety of possible configs so use -z help to learn more about them

-z follow,*prot*,*mode*,*filter*[,*range*] : This is follow command config for -z .

-q : suppress default TShark output

TShark statistics:

Protocol Hierarchy Statistics:

```bash
tshark -r capture1.pcap -z io,phs,tcp -q
```

**-z** io,phs[,*filter*] : Create protocol hierarchy statistics listing through a filter.

Endpoint statistics:

Tshark can get individual statistics on the endpoints (computers) through the -z flag.

```bash
tshark -r capture1.pcap -z endpoints,tcp -q
```

**-z** endpoints,*type*[,*filter*] : creates a table with all the endpoints on the network based on type

"bluetooth" Bluetooth addresses
"dccp" DCCP/IP socket pairs Both IPv4 and IPv6 are supported
"eth" Ethernet addresses
"fc" Fibre Channel addresses
"fddi" FDDI addresses
"ip" IPv4 addresses
"ipv6" IPv6 addresses
"ipx" IPX addresses
"jxta" JXTA message addresses
"mptcp" Multipath TCP connections
"ncp" NCP connections
"rsvp" RSVP connections
"sctp" SCTP/IP socket pairs Both IPv4 and IPv6 are supported
"sll" Linux "cooked mode" capture addresses
"tcp" TCP/IP socket pairs Both IPv4 and IPv6 are supported
"tr" Token Ring addresses
"udp" UDP/IP socket pairs Both IPv4 and IPv6 are supported
"usb" USB addresses
"wlan" IEEE 802.11 addresses
"wpan" IEEE 802.15.4 addresses
"zbee_nwk" ZigBee Network Layer addresses

Conversation statistics:

Tshark can extract statistics based on conversations as well:

```bash
tshark -r capture1.pcap -z conv,tcp -q
```

**-z** conv,*type*[,*filter*] : create a table to list all conversations in the capture.

Protocol Satistics:

You can use TShark to get statistics on which different protocols have been used in the capture:

```bash
tshark -r capture1.pcap -z ptype,tree -q
```

**-z** ptype,tree[,*filter*] : Calculate statistics on port types that occur on IPv4 packets.
![My project-1](https://user-images.githubusercontent.com/71113185/194425729-692f47b4-3f3f-47d4-a5df-bd3ad14285da.png)
