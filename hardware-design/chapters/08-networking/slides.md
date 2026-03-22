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

- Application Layer
- Transport Layer
- Internet Layer
- Network Access Layer

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

### What happens when you visit a website?

1. You enter a web address (a URL, Uniform Resource Locator) into a browser.
2. The browser queries a DNS server, converting the domain to an IP address.
3. If the website uses HTTPS, a secure and encrypted connection is established between the browser and the website server.
4. The browser sends an HTTP request to the website server, requesting the content of the website.
5. The server processes this request, sending back the requested files (probably HTML, CSS, JavaScript).
6. The browser processes the received files and renders the website.

### DNS Can Fail!

- Your computer and local router do not know the layout of the whole internet
- DNS lookups are distributed across the internet
- If your DNS server is down, you won't get a response
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
- A `POST` request could be sending an email. Includes email data, metadata, auth, etc

### Ports

- Your computer might be running Spotify, Zoom, and Chrome at the same time. 
- How does it know which incoming data goes to which app?
- Each application "listens" on a specific Port.
- Firewalls may look at port number when deciding to let traffic through
%    - Port 80/443: Web traffic (HTTP/HTTPS)
%    - Port 25: Email (SMTP)
%    - Port 53: DNS
%    - Port 22: SSH

### Summary

- Human types in a URL
- Computer uses DNS to look up the corresponding IP address
- Send a request: IP address, port (eg 443), type (eg `PUT`), data
- Get a response: IP address, port, status (eg `404`), data

### Exercise

TODO: this

## Transport Layer

### Segmentation and Reassembly

- TCP chops data into **segments** before sending
- Each segment has a header including port and sequence ID
- Recipient NIC/OS uses the header to reassemble the data
- Why do you suppose we do this?

### Why Segmentize?

- The internet can't handle one giant 5GB file at once
- Resiliency. Eggs in multiple baskets
- Easier for your NIC (network card) to take turns

% don't want all our eggs in one basket

### Multiplexing and De-Multiplexing

- HTTPS is on port 443, SSH is on port 22, etc
- Different apps may be running at the same time
- Data is getting chopped up into segments
- How do we make sure the data doesn't get mixed up?

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
- TCP: slower, guaranteed delivery
- UDP: faster, best effort
- Multiple apps can take turns sending segments

### Exercise

TODO: this

## Internet Layer

### Routing Segments

- App uses a certain port, and attaches that data to each segment of data
- Computer knows the destination IP address from DNS
- How do we keep track of both?
- Wrap each segment into a **packet**

### Remember: Layers of Encapsulation!

![network layers but frames are partially hidden by a SPOILERS banner](images/network-layers-spoiler.png)

### IP Addresses

- Public IP address: How to get to your network
- Private IP address: Your address within the network (transient)
- This is important because there are more devices than addresses

### IPv4

|||
- Introduced in 1982
- Still used to route most internet traffic
- Uses 32-bit addresses (about 4 billion unique addresses)
- Not enough unique addresses for the global internet; IPv4 address exhaustion issue
|||
![ipv4 breakdown](images/ipv4-address)
|||

### IPv6

|||
- Most recent version of the Internet Protocol
- Developed to handle IPv4 address exhaustion, replacing IPv4
- Uses 128-bit addresses
- Other improvements over IPv4
|||
![ipv6 breakdown](images/ipv6-address)
|||

### Routing Packets

- Your laptop sends each packet to a **router**, which looks at the destination IP address
- If the address is in the local neighborhood, deliver it
- Otherwise, use a **routing table** to figure out which direction to send it
- Different segments may take different paths, then get reassembled later


TODO: probably talk about NAT here? switching between local IP and global IP


### Routing Packets

Packets may take different paths. What happens if they get stuck in a loop?

% header also includes a "timer". Drops by 1 every time the packet hits a router. If the timer runs out, the packet is deleted

![packet switching](images/packet-switching)

### Summary

- Data segments are wrapped in packets which contain the destination IP address
- Routers pass packets along until they get to that address
- IPv4: limited address space, so we network address + private address
- IPv6: plenty of addresses, not yet widely used

### Exercises

TODO: this

## Network Access Layer

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

### NAT and PAT

Network Address Translation

Port Address Translation


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


### Layer Violation!

Most routers just look at IP address to figure out where to send data next

Your home router breaks the rule. It also looks at port

Laptop, port 443... let's call that port 100001

Raspberry Pi, port 22... let's call that port 100002



### Exercise

You can use the `ping` command to measure latency and packet loss to a specific host. For example,
```bash
ping www.google.com
```
This should work on Raspberry Pi or Mac.

You can test your throughput using `www.speedtest.net` (will be affected if other pages/applications are using the internet). There is also a command line version of this, but it requires installation.


