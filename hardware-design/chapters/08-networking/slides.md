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





### TCP/IP Model

- Application Layer
- Transport Layer
- Internet Layer
- Network Access Layer



## Application Layer

### Client-Server Model

### HTTP and HTTPS

### DNS

### Ports






## Transport Layer



## Internet Layer



## Network Access Layer



## Network Security





### TCP/IP Model

The TCP/IP Model provides rules for computer systems to communicate over a network. By dividing the tasks into layers, it makes it easier for different technologies to communicate. 

TCP/IP Basics:
- Ensures that data arrives safely and correctly.
- Data is broken into small pieces, called packets, to be sent.
- Packets are sent separately.
- Packets are reassembled into the correct order when they are received.

### TCP/IP Model

Application Layer (closest to user): where applications (e.g. web browsers, email clients) connect to the network.

- Manages data formatting
- Manages encryption
- Manages connection sessions
- Protocols: HTTP, FTP, SMTP, DNS

Transport Layer: ensures that data is sent reliably and completely.

- Checks for errors
- Resends packets if needed
- Keeps track of order
- Protocols: TCP, UDP

Internet Layer: finds path across different networks for data to reach its destination.

- Routing
- Finding the best way to travel
- Protocols: IP

Network Access Layer (physical connection): ensures data can travel over the hardware within a local network.

- Data travels over wires, switches, wireless signals.
- MAC addresses identify devices

### Network Devices

- A router directs data between different networks (e.g., home network and internet).
- A network switch connects devices on the same local network (LAN).
- A modem connects your local network to your internet service provider (ISP); gateway to the internet.
- A firewall monitors network traffic to protect against unauthorized access.
- A Wireless Access Point allows wireless devices to connect to a wired network.
- A Network Interface Card is a hardware component in a computer, allowing it to connect to a network.


### Network Diagram

![network diagram](images/network-diagram)

### Packet Switching

When data is transmitted over a network, it’s divided into small pieces called packets. These packets are sent independently through the network (possibly through different paths), and reassembled at the destination.

![packet switching](images/packet-switching)

### Packet Switching

- Efficiently uses available bandwidth
- Reliable (can detect missing packets, request retransmission)
- Packets may arrive out of order
- Use sequence number to reassembly packets in correct order

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

### MAC and IP Addressing

A MAC address is a permanent address for local communication, tied to hardware. It is hard-coded into a device’s network interface card.
An IP address is a software-based address for broader network communication. It identifies a device on a network, and can change if the device connects to a different network.
To deliver data, the router uses the IP address to find the correct network, and it uses the MAC address to find the specific device.

### Internet Protocol

The Internet Protocol (IP) establishes rules for how data is sent across the internet (or other networks). Data is divided into packets, and unique IP addresses are used to route packets to the correct destination.
- Every device on the network is assigned a unique IP address
- Another protocol (e.g. TCP) is used to ensure that the data arrives reliably, without errors.
- Two major versions: IPv4 and IPv6

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

### Exercise

Connect your Raspberry Pi to St. Olaf Wi-Fi (St. Olaf Guest is fine)
On your Raspberry Pi, view the status of your active network interfaces:
```bash
ifconfig
```
Can you find the connection to your laptop?
Find the IP address(es) of your computer for your internet connection.
Find the MAC address(es) of your computer.

You may need to Google how to read the output of `ifconfig` in order to answer these questions.

### TCP vs UDP

TCP and UDP are transport layer protocols for sending data, ensuring that data arrives quickly, reliably, and in order.
TCP (Transmission Control Protocol) requires a connection to be established before sending data. It guarantees that all packets are delivered correctly and in the proper order.
- Used for web browsing, email, file transfers
- Slower than UDP
UDP (User Datagram Protocol) does not require a connection to send packets. It does not guarantee that packets will be received, or received in order.
- Used for video streaming, online gaming
- Faster than TCP

### Client-Server Model

In the client-server model, clients (e.g. web browsers, email applications) request services and servers provide them.

- The client initiates communication by requesting data or services from a server.
- The server waits for client requests, and then responds by sending data or performing requested tasks.

![client server model](images/client-server-model)

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





### Cache!

- Communicating over a network is way slower than loading a value from memory
- Software often caches data locally (eg by writing it to a file) to avoid duplicate calls later
- images on a website, for example



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


## Day 1: The Local Network (The "Mailroom")

Goal: How does a computer talk to the device next to it?

- The Hardware (5 mins): Ditch hubs/bridges; focus on the Network Interface Card (NIC) and the Switch.
- Switching & MAC Addresses (10 mins): Explain that every device has a permanent "Social Security Number" (MAC Address). A switch is a smart mailroom that sends data only to the specific port where that MAC lives.
- The Client-Server Model (10 mins): Most internet interaction is just a "Client" (student's laptop) asking a "Server" (Google/Discord) for a file.
- Packets (5 mins): Data isn't sent in one big chunk; it’s chopped into tiny envelopes called packets.

Day 2: The Global Internet (The "Postal Service")

Goal: How does that packet find a server 3,000 miles away?

- IP Addresses & Routing (10 mins): If a MAC is a name, an IP address is a "Mailing Address." Explain that Routers are the GPS of the internet—they look at the IP and decide which city/country to send the packet to next.
- DNS & HTTP/HTTPS (10 mins): Students don't type IPs; they type google.com. Explain DNS as the "Contacts App" of the internet. Then, briefly explain HTTP as the language used to ask for the website once you arrive.
TCP/UDP & Security (10 mins):
- TCP: "Did you get that?" (Guaranteed delivery for websites/email).
- UDP: "Hope you get this!" (Fast, but messy—for gaming/video calls).
- Encryption: Mention that HTTPS (the 'S') is just a locked envelope so the routers in the middle can't read your password.





switch cares about MAC address. does not know anything about IP address. delivers messages within a network/neighborhood

switch watches traffic to see which MAC address is where. stores entries in a table. when data wants to go to a known address, it can send it directly. if data wants to go to an unknown address, it yells to everyone and waits for a response.

router knows about IP address. it sends the data to the appropriate network/neighborhood

if you ping google. your computer knows that it's not a nearby IP address. it sends it to the MAC address of the router

MAC address is hard-coded into the NIC when manufactured. NIC is supposed to ignore any traffic addressed to a different MAC




signals on the computer run in parallel. eg 64-bit system ostensibly means your logic path is 64 bits wide. the NIC takes that and turns it into one channel for the network





switch only sends data to the right MAC address. but you can tell your NIC to pretend to be many MAC addresses
- MAC Flooding
- ARP Spoofing






## The Physical Layer

### outline placeholder

- Basic networking hardware (Hubs, bridges, NICs, cables)
- Switching vs. Routing (Focusing on Layer 2 switching)
- The OSI Model (Introduction to the 7-layer framework) 

## Network Protocols

### outline placeholder

- The TCP/IP Model (Comparing it to OSI)
- IP Addresses (IPv4, IPv6, and subnets)
- Packets (Encapsulation and structure)
- TCP vs. UDP (Connection-oriented vs. connectionless)
- Switching vs. Routing (Focusing on Layer 3 routing) 

## Internet Infrastructure \& Navigation

### outline placeholder

- How the internet works (The "network of networks" concept)
- DNS (Domain Name System and the resolution process)
- The client-server model (Request/response architecture)

## The Application Layer

### outline placeholder

- HTTP/HTTPS (Web traffic and state)
- The client-server model (As it relates specifically to web apps)

## Security \& Privacy

### outline placeholder

- Encryption (Symmetric, asymmetric, and hashing)
- HTTPS (The role of SSL/TLS certificates)
- Network security and attacks (DDoS, Man-in-the-Middle, packet sniffing)



### summary

DNS finds the address.
TCP chops the data into Packets.
Routers move them across the world.
Switches deliver them to the right desk.

