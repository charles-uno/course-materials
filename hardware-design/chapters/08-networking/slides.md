beamer: true
---

# Networking

### What is a Computer Network?

A network is a group of interconnected devices exchanging data. We refer to the devices connected by a network as nodes.
Examples:
- Home network, connecting laptops, smartphones, printer. Devices share internet connection, can all access the printer. This is a **LAN** (Local Area Network). 
- If it uses WiFi to connect devices, this is a **WLAN** (Wireless Local Area Network).
- Personal network, connecting smartphone to smartwatch, headphones using Bluetooth. This is a **PAN** (Personal Area Network).
- St. Olaf campus network, connecting laptops, phones, servers (csgit). This is a **CAN** (Campus Area Network), made up of many LANs.
- Internet, connects networks across huge distances. This is a **WAN** (Wide Area Network).

### Physical Media

- Ethernet: voltage in metal wires
- Wifi: radio waves (invisible, incorporeal)
- Fiber: Lasers through glass

### Getting Plugged In

Each computer talks to the network using a **NIC** (Network Interface Card):

- Not a literal card these days
- Keeps track of connections over wifi, ethernet
- Incoming and outgoing traffic
- Translates between CPU (64+ lanes) and network (maybe just 1 lane)

### TCP/IP Model

When talking about networking, we have a few different layers of abstraction:

- Application Layer
- Transport Layer
- Internet Layer
- Link Layer

### Data Encapsulation

![frame, packet, and segment](images/network-layers)

## Application Layer

### Client-Server Model

Data doesn't move on its own:

- Clients issue **requests**
- Servers listen and send **responses**

![client server model](images/client-server-model)

% server is ready to respond at all times

### Client-Server Model

Clients initiate network connections:
- Your phone
- Your laptop
- ATMs
- Your smart TV

Servers listen and respond:
- Websites
- App backends
- Databases
- Minecraft server

### Client And Server

Can one device be both a client and a server?

If so, can it perform both roles at the same time?

### Client-Server Model

Yes!

- When you type `ping google.com` on your Raspberry Pi to check the internet connection, the Pi is acting as a client
- When you type `ssh kiwi@raspberrypi.local` on your laptop, your Pi is acting as a server

### Domain Name System (DNS)

- Computers use numbers, not words
- Huamns can't remember `142.250.190.46`
- We use DNS to bridge the gap
- When you ask for `google.com`, your computer uses DNS to look up the corresponding IP address
- We'll talk more about IP addresses later (internet layer)

### DNS Can Fail!

- Your computer and local router do not know the layout of the whole internet
- DNS lookups are distributed across the internet
- If the DNS server is down, you won't get a response
- Websites may be "up" but inaccessible by name
- This happens every few years!

% The Dyn Attack (2016): DDoS attack hit Dyn, a major DNS provider. Twitter, Spotify, Reddit, and Netflix went dark
% The Facebook/Meta Outage (2021): configuration error removed FB from DNS. Internal systems worked, but no external access
% Akamai Bug (2021): infra bug caused a global DNS disruption affecting airlines, banks
% AWS "Cascading" DNS Failure (2021): AWS bug broke their internal DNS. Disrupted sites hosted on AWS (snapshat, disnet+, venmo)

### HTTP and HTTPS

Hyper Text Transfer Protocol (HTTP) is the set of rules for how a browser asks for a webpage.
- Request types: `GET`, `PUT`, `POST`, `DELETE`
- Status code: 200 (normal), 30x (redirect), 40x (client error), 50x (server error)
- HTTPS: same rules but the data is encrypted (more on this later)

### HTTP and HTTPS

- You can also attach data to an HTTP/HTTPS request!
- A `GET` request often does not include any data. Just asking for website contents
- A `POST` request could be sending an email. Includes email contents, metadata, auth, etc

### Summary

- Human types in a URL
- Computer uses DNS to look up the corresponding IP address
- Send a request: IP address, type (eg `PUT`), data
- Get a response: IP address, status (eg `404`), data

### Exercise

TODO: this

## Transport Layer

### Segmentation and Reassembly

- TCP chops data into **segments** before sending
- Each segment has a header including a sequence ID
- Recipient NIC/OS uses the header to reassemble the data
- Why do you suppose we do this?

% may be multiple apps using the NIC at the same time. port

### Why Segmentize?

- The internet can't handle one giant 5GB file at once
- Resiliency. Eggs in multiple baskets
- Easier for your NIC (network card) to take turns

% don't want all our eggs in one basket

### Multiple Applications

- Your computer might be running Spotify, Zoom, and Chrome at the same time
- Data for each app is getting chopped up into segments
- How do we keep track of what goes where?

### Ports

- Each application "listens" on a certain port
- Ports are assigned by the OS
- SSH server always listens on port 22, HTTPS server always listens on port 443, etc
- Client and server ports do not need to match
- Ports are included in the segment header

### What happens if a segment gets lost along the way?

- We can ask the other machine to re-send the missing data
- Should we do so? Or just move on without it?

### TCP vs UDP

We choose the protocol based on the use case.

- TCP (Transmission Control Protocol). Delivery is guaranteed. Lost packets are re-sent. Web browsing, email, file transfers
- UDP (User Datagram Protocol). Faster but not guaranteed. Lost packets are gone. Gaming, video calls, streaming

### The Three-Way Handshake

How does TCP ensure a reliable connection?

1. Client: Hey my name is Charles (sync), can you synchronize with me?
2. Server: Hi Charles (ack), my name is Telemachus (sync)
3. Client: Hi Telemachus (ack)

### Summary

- Requests get broken down into segments for transmission
- Segments can be reassembled using header data: port, sequence ID
- TCP: slower, guaranteed delivery
- UDP: faster, best effort

### Exercise

TODO: this

## Internet Layer

### Routing Segments

- We have segments: data, port, seq ID
- We want to send those segments to an IP address (from DNS)
- What does that process look like?
- Wrap the segment in a **packet**

### Remember: Layers of Encapsulation!

![network layers but frames are partially hidden by a SPOILERS banner](images/network-layers-spoiler.png)

### Routing Packets

- Your laptop sends each packet to a **router**, which looks at the destination IP address
- If the address is in the local neighborhood, deliver it
- Otherwise, use a routing table to figure out which direction to send it
- Different packets may take different paths, then get reassembled later

### Routing Packets

Packets may take different paths. What happens if they get stuck in a loop?

% header also includes a "timer". Drops by 1 every time the packet hits a router. If the timer runs out, the packet is deleted

![packet switching](images/packet-switching)

### IP Addresses

- What does my IP address actually look like?
- Ostensibly it's just four numbers separated by periods
- IP address is 32 bits long. What's $2^{32}$? How many devices are there on the planet?

% IPv4 exhaustion

![ipv4 breakdown](images/ipv4-address)

### IPv4 Exhaustion

- There are about 4 billion possible IPv4 addresses
- There are more than 4 billion network devices
- Eventually we'll switch to IPv6 (128 bits)
- In the meantime we use **public** and **private** IP addresses

![ipv6 breakdown](images/ipv6-address)

### Public and Private IP Addresses

- *Public* IP is the address of your network (eg St Olaf College)
- Public IP address is (mostly) constant to play nice with DNS
- *Private* IP if the address within that network (eg your laptop)
- Private IP addresses can change all the time
- A few IP address patterns are reserved for private (eg `192.168.x.x`, `172.16.x.x`) 

### Public and Private IP Addresses

Network Address Translation (NAT):
- When you send a request to Google, the packet includes your private IP address
- The router at the edge of the network switches the request to use the public IP address instead

Port Address Translation (PAT):
- Multiple machines on the same public IP address
- Some may be using the same ports!
- The router switches your private port to a unique public port

In both cases, the router keeps a table to swap back

### Layer Violation!

- Most routers just look at IP address (packet header)
- The router at the edge of the network also looks at port (segment header)
- This seems weird, but does it really matter?

% digging deeper is more CPU intensive

### Layer Violation!

- In principle, a router is just moving packets around
- NAT/PAT means it is reading and manipulating packet content
- You can't trust intermediate machines not to read your data
- If you want privacy, you have to encrypt (more on this later)

### Summary

- Data segments are wrapped in packets which contain the destination IP address
- Routers pass packets along until they get to that address
- IPv4 has limited addresses, so we use public + private addresses
- Public/private swap is handled at the edge of the network
- IPv6 replaces public + private, isn't widely used yet

### Exercises

TODO: this

## Link Layer

### MAC Addresses

- Every NIC (network card) has a unique ID burned into it at the factory
- This is how data is ultimately delivered
- Important because local IP addresses are transient

### Frames

- Remember: a packet contains the destination IP address
- But how do we specify one step in that journey?
- Wrap the packet in a **frame**
- Frame contains the MAC address of the next device

### Frames

![frame, packet, and segment](images/frame-encapsulation)

### Wrap Unwrap Wrap Unwrap

- The frame contains the MAC address of the *next* device
- Data may pass through dozens of routers along the way
- Each router must unwrap the frame, look at the IP address, figure out the next step, and rewrap it
- Your computer attaches your MAC address to each outbound frame, but that MAC address doesn't leave your local network

### Delivering to a MAC Address

How does a router know the MAC addresses of its neighbors?

% it listens to outgoing traffic and builds a table (ARP)

% local traffic uses a SWITCH

### Address Resolution Protocol (ARP)

This is the "glue" between the Internet Layer and Network Access Layer.
The Problem: Your Pi knows the IP of the Router, but the Switch only understands MACs. How do we find the MAC?
The Solution: ARP (Address Resolution Protocol). Your Pi shouts: "Who has IP 192.168.1.1? Tell me your MAC!" The router replies, and now the Pi can build the Frame.

### Frames Trailer

- In addition to the MAC address, a frame also contains a checksum
- This allows the NIC to identify incomplete or corrupted data

### Every Router Except the Last One

- Receive a frame addressed to itself
- Remove the outer wrapper (leaving the packet)
- Read the destination IP address
- Figure out the next hop along the path


- Use a routing table to identify the next router
- Wrap the packet in a new frame with that address
- Send it along

### The Last Router

- Receive a frame addressed to itself
- IP address is for this network
- Look up the corresponding MAC address
- Send it to the switch
- Port lookup shenanigans (NAT) to get the appropriate private IP address MAC address


### The Switch

- We have a bunch of computers
- Each computer is plugged into the switch (via ethernet or wifi)
- Switch keeps track of the MAC address for each
- Delivers packets based on MAC address
- A **gateway** is just a router and a switch in the same box

### Routers and Switches

To be technically precise for your Raspberry Pi lab, the "nesting" order looks like this:
The Segment (Transport Layer): This is your data (like a piece of a webpage) plus the TCP/UDP header (Source/Destination Ports). [1, 2]
The Packet (Internet Layer): The entire Segment is stuffed inside an IP header (Source/Destination IP Addresses). [1, 3]
The Frame (Network Access Layer): The entire Packet is stuffed inside an Ethernet header (Source/Destination MAC Addresses). [1, 4]

- router gets a packet addressed to its own MAC address
- uses a **routing table** to figure out the next hop to get to the destination IP address

### Exercises

We can use the `traceroute` command on our Raspberry Pi to track the path that packets take from your computer to a destination. For example, try:
```bash
traceroute google.com
```
This sends packets through the internet, and shows every server or router passed through along the way.

On your Raspberry Pi, view the status of your active network interfaces:
```bash
ifconfig
```
- Can you find the connection to your laptop?
- Find the IP address(es) of your computer for your internet connection.
- Find the MAC address(es) of your computer.

You may need to Google how to read the output of `ifconfig` in order to answer these questions.


## Performance \& Security


### Metrics of Network Performance

**Bandwidth** is the maximum rate at which data can be transmitted over a network.
**Throughput** is the actual amount of data successfully transmitted over the network in a given time period.
- Low throughput is perceived as buffering or slow downloads.
- Limit on volume of data transmitted.
**Latency** is the time between a packet being sent, and a response being received.
- High latency is perceived as slow or delayed actions (e.g. lag in video games).
- Limit on speed of data transmitted.
**Packet Loss** is the percent of packets that fail to reach their destination.
- High packet loss is perceived as choppy audio/video, generally slower performance due to retransmission.
- Inconsistency in timing of data received.

### Network Security

- Eavesdropping is intercepting network traffic to steal sensitive information.
- While packets traverse a network, they can be captured by unauthorized parties. This is called packet sniffing.
- In a Man-in-the-Middle (MitM) attack, an attacker positions themselves between communicating parties. This allows them to intercept, and potentially alter, messages.

### Network Security

![man in the middle](images/man-in-the-middle)

### Encryption

Encryption is a powerful tool against eavesdropping. Encryption scrambles data being sent, so that (in theory) only the intended recipient can unscramble it to read the message. For example, HTTPS encrypts communications.
Really cool cryptography: public-key encryption, RSA

![encryption](images/encryption)




switch only sends data to the right MAC address. but you can tell your NIC to pretend to be many MAC addresses
- MAC Flooding
- ARP Spoofing



### Exercise

You can use the `ping` command to measure latency and packet loss to a specific host. For example,
```bash
ping www.google.com
```
This should work on Raspberry Pi or Mac.

You can test your throughput using `www.speedtest.net` (will be affected if other pages/applications are using the internet). There is also a command line version of this, but it requires installation.


