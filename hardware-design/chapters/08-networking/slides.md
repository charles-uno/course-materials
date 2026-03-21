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
- Servers send **responses**

![client server model](images/client-server-model)

% server is ready to respond at all times

### Client-Server Model

Clients initiate network connections:
- Your phone
- Your laptop
- ATMs

Servers listen and respond:
- Google
- Amazon
- Spotify

### Client And Server

Can one device be both a client and a server?

If so, can it perform both roles at the same time?

### Client-Server Model

Yes!

- When you type `ping google.com` on your Raspberry Pi to check the internet connection, the Pi is acting as a client
- When you type `ssh kiwi@raspberrypi.local` on your laptop, your Pi is acting as a server

### HTTP and HTTPS

HyperText Transfer Protocol is the set of rules for how a browser asks for a webpage.
- HTTP: Sending a postcard. Anyone (hackers, ISPs) can read it as it passes by.
- HTTPS: Sending a locked box. The 'S' stands for Secure (via TLS/SSL encryption). It ensures that even if someone "sees" the data, they can't read your password or credit card info.

### DNS

- Computers use numbers, not words
- Huamns can't remember `142.250.190.46`
- We use DNS to bridge the gap
- When you ask for `google.com`, your computer uses DNS to look up the corresponding IP address

### DNS Can Fail!

- Your computer and local router do not know the layout of the whole internet
- DNS lookup requires a request over the internet
- If your DNS server is down, you won't get a response
- Websites may be "up" but inaccessible by name
- This happens every few years!

% The Dyn Attack (2016): DDoS attack hit Dyn, a major DNS provider. Twitter, Spotify, Reddit, and Netflix went dark
% The Facebook/Meta Outage (2021): configuration error removed FB from DNS. Internal systems worked, but no external access
% Akamai Bug (2021): infra bug caused a global DNS disruption affecting airlines, banks
% AWS "Cascading" DNS Failure (2021): AWS bug broke their internal DNS. Disrupted sites hosted on AWS (snapshat, disnet+, venmo)

### Ports

- Your computer might be running Spotify, Zoom, and Chrome at the same time. 
- How does it know which incoming data goes to which app?
- Each application "listens" on a specific Port.
- Firewalls may look at port number when deciding to let traffic through
%    - Port 80/443: Web traffic (HTTP/HTTPS)
%    - Port 25: Email (SMTP)
%    - Port 53: DNS
%    - Port 22: SSH

### Exercise

TODO: this

## Transport Layer

### TCP vs UDP

We choose the protocol based on the use case.

- TCP (Transmission Control Protocol). Delivery is guaranteed. Lost packets are re-sent. Web browsing, email, file transfers
- UDP (User Datagram Protocol). Faster but not guaranteed. Lost packets are gone. Gaming, video calls, streaming

### The Three-Way Handshake

How does TCP ensure a reliable connection?

1. Client: Hey my name is Charles (sync), can you synchronize with me?
2. Server: Hi Charles (ack), my name is Telemachus (sync)
3. Client: Hi Telemachus (ack)

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

### Exercise

TODO: this

## Internet Layer

### IP and MAC Addresses

- Public IP address - How to get to your network
- Private IP address - Your address within the network (transient)
- MAC address - Unique to your computer (burned onto the NIC)

### IPv4

|||
- Introduced in 1982-1983
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

### Packets

- Segment gets wrapped in an IP header 
- Source IP address, destination IP address
- This layer does not touch the data inside the packet

### Packets

Packets may take different paths. What happens if they get stuck in a loop?

% header also includes a "timer". Drops by 1 every time the packet hits a router. If the timer runs out, the packet is deleted

![packet switching](images/packet-switching)

### Routing

A router looks at the destination IP address

- If the address is in the local neighborhood, pass it along to the switch (more on this in a minute)
- Otherwise, use its **routing table** to figure out which direction to send it

### Exercises

On your Raspberry Pi, view the status of your active network interfaces:
```bash
ifconfig
```
- Can you find the connection to your laptop?
- Find the IP address(es) of your computer for your internet connection.
- Find the MAC address(es) of your computer.

You may need to Google how to read the output of `ifconfig` in order to answer these questions.

## Network Access Layer (AKA Link Layer)

### Physical Media

This is the literal physical stuff. On a Raspberry Pi, students usually deal with two types:
Ethernet (Copper): Electricity pulsing through wires.
Wi-Fi (Radio): Invisible waves in the air.
Fiber (Light): Lasers through glass (usually for the "backbone" of the internet).

### MAC Addresses

This is the most important concept for this layer.
Physical vs. Logical: An IP address (Internet Layer) is assigned by the network. A MAC address is burned into the NIC at the factory.
The Scope: MAC addresses only matter locally. Your router uses your Pi's MAC address to find it in the room, but a server in Japan has no idea what your MAC address is—it only sees your IP.

### Frames

Frame wraps around the packet (which wraps around the segment)

As we discussed, this is the final "envelope."
The Header: It adds the Source MAC and Destination MAC.
The Trailer (FCS): This layer adds a "checksum" at the end of the data. If the electricity flickers and a bit gets flipped, the NIC detects the error and throws the frame away before it even reaches the CPU.

### ARP

This is the "glue" between the Internet Layer and Network Access Layer.
The Problem: Your Pi knows the IP of the Router, but the Switch only understands MACs. How do we find the MAC?
The Solution: ARP (Address Resolution Protocol). Your Pi shouts: "Who has IP 192.168.1.1? Tell me your MAC!" The router replies, and now the Pi can build the Frame.

### Routers and Switches

To be technically precise for your Raspberry Pi lab, the "nesting" order looks like this:
The Segment (Transport Layer): This is your data (like a piece of a webpage) plus the TCP/UDP header (Source/Destination Ports). [1, 2]
The Packet (Internet Layer): The entire Segment is stuffed inside an IP header (Source/Destination IP Addresses). [1, 3]
The Frame (Network Access Layer): The entire Packet is stuffed inside an Ethernet header (Source/Destination MAC Addresses). [1, 4]

- router gets a packet addressed to its own MAC address
- uses a **routing table** to figure out the next hop to get to the destination IP address


### Layer Violation!

Most routers just look at IP address to figure out where to send data next

Your home router breaks the rule. It also looks at port

Laptop, port 443... let's call that port 100001

Raspberry Pi, port 22... let's call that port 100002

### Exercises

TODO: this


## Network Security











### Exercise

We can use the `traceroute` command on our Raspberry Pi to track the path that packets take from your computer to a destination. For example, try:
```bash
traceroute google.com
```
This sends packets through the internet, and shows every server or router passed through along the way.

If you’ve seen Dr. Horrible’s Sing-Along Blog, try:
```bash
traceroute bad.horse
```


### Application Protocols

HTTP (HyperText Transfer Protocol) defines how clients (such as web browsers) and servers exchange information.
- The browser sends an HTTP request to the server hosting the website.
- The server processes the request, and sends an HTTP response containing the requested data.
- HTTP request methods:
    - GET: retrieve a resource (e.g., content of a webpage)
    - POST: submit data to the server (e.g., submit a form)
    - PUT: update or create a resource at a specific location (e.g., upload profile picture)
    - DELETE: remove a resource
HTTPS is HyperText Transfer Protocol Secure, adding security by encrypting the data being exchanged.

### Application Layer Protocols

DNS (Domain Name System) translates domain names (like www.google.com) into IP addresses (like 173.194.39.78).
- When you type a web address (URL) into your browser, the browser sends a DNS query to a DNS server.
- The DNS server looks up the domain name, and returns the corresponding IP address.
- Purpose: Users can remember domain names, instead of IP addresses.

% when facebook.com goes down, DNS goes down for a decent chunk of the internet

### What happens when you visit a website?

1. You enter a web address (a URL, Uniform Resource Locator) into a browser.
2. The browser queries a DNS server, converting the domain to an IP address.
3. If the website uses HTTPS, a secure and encrypted connection is established between the browser and the website server.
4. The browser sends an HTTP request to the website server, requesting the content of the website.
5. The server processes this request, sending back the requested files (probably HTML, CSS, JavaScript).
6. The browser processes the received files and renders the website.





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

### Exercise

You can use the `ping` command to measure latency and packet loss to a specific host. For example,
```bash
ping www.google.com
```
This should work on Raspberry Pi or Mac.

You can test your throughput using `www.speedtest.net` (will be affected if other pages/applications are using the internet). There is also a command line version of this, but it requires installation.

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




You will be asked a series of conceptual questions, and you will be evaluated on how well your answers demonstrate understanding of the following networking concepts:
- Basic definitions
- How the internet works
- Basic networking hardware
- The client-server model
- The OSI Model
- THE TCP/IP Model
- IP Addresses
- TCP vs. UDP
- HTTP/HTTPS
- DNS
- Switching vs. Routing
- Packets


switch cares about MAC address. does not know anything about IP address. delivers messages within a network/neighborhood

switch watches traffic to see which MAC address is where. stores entries in a table. when data wants to go to a known address, it can send it directly. if data wants to go to an unknown address, it yells to everyone and waits for a response.

router knows about IP address. it sends the data to the appropriate network/neighborhood

if you ping google. your computer knows that it's not a nearby IP address. it sends it to the MAC address of the router

MAC address is hard-coded into the NIC when manufactured. NIC is supposed to ignore any traffic addressed to a different MAC






