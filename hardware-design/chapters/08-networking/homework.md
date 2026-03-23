---
---

Classroom Pro-Tip: Have your students open their browser's "Developer Tools" (F12) and look at the Network tab. When they refresh a page, they can see the actual HTTP Requests and Responses happening in real-time.

# Networking


## Application Layer

1. DNS: The "Phonebook" Investigation
Students use dig (Domain Information Groper) or nslookup to see how names become numbers. 
Command: dig google.com
What to look for: Have them find the "ANSWER SECTION" to see the IP address.
Challenge: Run dig -x [IP_ADDRESS] (a reverse lookup) to see if the number points back to the same name. This demonstrates that DNS is a two-way directory. 
2. HTTP: Talking to a Web Server Manually
Students use curl to see the "hidden" conversation between a browser and a server. 
Command: curl -I https://www.google.com (The -I flag shows only the headers).
What to look for: Point out the HTTP Status Codes (like 200 OK or 404 Not Found).
Concept: This proves that "the web" is just text-based requests and responses, not magic. 
3. Ports: Seeing the "Open Doors"
Students use netstat or ss to see what their own Raspberry Pi is "listening" to right now. 
Command: netstat -tuln (or ss -tuln on newer OS versions).
What to look for: They will likely see Port 22 (SSH).
Concept: Explain that because Port 22 is "LISTEN," their Pi is waiting for them to log in. If they were running a web server, they’d see Port 80 or 443. 
4. Port Scanning: The Hacker’s First Step
Using nmap, students can scan another student's Pi (or their own) to see what services are exposed. 
Command: nmap [STUDENT_PI_IP]
What to look for: A list of open ports and the services running on them (e.g., 22/tcp open ssh).
Security Angle: This is a great transition into your Network Security topic—if a port is open, a hacker has a way in. 

Pro-Tip: If you have time, have them run traceroute google.com. It visually shows the "hops" (Routers) their packet takes to leave the classroom and reach the destination. 

## Transport Layer

Hands-on Pi Exercise: ss and tcpdump
Have your students see the difference between "Established" connections and "Listening" ports.
Command: ss -t (Show only TCP connections).
What to look for: They will see their SSH connection to the Pi as "ESTABLISHED."
Advanced: Run sudo tcpdump -i eth0 port 22 to see the actual TCP "Flags" (like [S] for SYN or [.] for ACK) flying across the screen in real-time.
Summary for Students:
IP (Layer 3) gets it to the right house.
TCP/UDP (Layer 4) gets it to the right person (Port) and makes sure they got the whole message.


Teaching Tip: Use the command sudo tcpdump -i eth0 'tcp[tcpflags] & (tcp-syn|tcp-ack) != 0' on the Pi. It will filter out the boring data and show the students the actual [S] (SYN) and [.] (ACK) flags as they browse the web.

## Internet Layer

Hands-on Pi Exercise: ip and traceroute
This makes the abstract "path" visible to the students.
Command 1: ip addr
Goal: Find their own IP and identify if it’s Private (usually starts with 192.168 or 10.).
Command 2: ip route
Goal: Find the default via IP. This is their "Default Gateway" (the Router).
Command 3: traceroute 8.8.8.8
Goal: Watch the packet "hop" through different routers across the world. They will see the latency (ms) increase as the packet physically travels further away.


## Link Layer

Hands-on Pi Exercise: ip link and arp
Let the students see their hardware's "fingerprint."
Command 1: ip link show
Goal: Find the link/ether line. That 12-digit hex code (e.g., b8:27:eb...) is their Pi’s unique MAC address.
Command 2: arp -a
Goal: See the "Address Resolution" table. This shows every other device the Pi has talked to recently and their corresponding MAC addresses.
Activity: Have two students compare their MAC addresses. They’ll notice the first 6 digits are often identical—that’s the "OUI" (Organizationally Unique Identifier) that identifies the manufacturer as Raspberry Pi Trading Ltd.

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



You can use the `ping` command to measure latency and packet loss to a specific host. For example,
```bash
ping www.google.com
```
This should work on Raspberry Pi or Mac.

You can test your throughput using `www.speedtest.net` (will be affected if other pages/applications are using the internet). There is also a command line version of this, but it requires installation.

