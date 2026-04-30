
---

# Networking

## Network Hardware

1. Find a network device on campus. Take a photo of it.
2. What type of device is it? (Hint: find the model number and look it up)
3. What does it do?
4. Are there any wires plugged into it? If is, what type of wires are they and what are they carrying?
5. Repeat for at least four other devices. Make sure each device is a different type.

## Application Layer

$$$
\begin{enumerate}

  \item Open the developer tools tab in your browser (F12). Go to the `Network` tab and make sure the `Method` column is visible (see screenshot). Visit some websites. 

\includegraphics[width=0.9\columnwidth, height=0.9\textheight, keepaspectratio]{images/chrome-developer-panel.png}

Make a note of five different \verb|GET| requests. Explain in words what each of those requests is doing. Don't explain the whole page -- just explain \textit{that} request specifically.

\item Do the same for five different \verb|POST| requests. 

\item HTTP also supports several other types of request, such as \verb|PUT| and \verb|DELETE|. Can you find a case where the browser sends any of these? Please explain either way. You can look this up, but make sure what you turn in reflects your own understanding!

\item Perform a DNS lookup with \verb|dig|. For example:
\begin{minted}{bash}
dig <URL>
dig -x <IP ADDRESS>
\end{minted}
What does it mean for a URL to have more than one IP address? Can you find a case where more than one URL points to the same IP address? In each case, explain what's happening.

\item Use \verb|curl| to request an entire website, then just the headers. For example:
\begin{minted}{bash}
curl https://www.google.com
curl -I https://www.google.com
\end{minted}
Print it out and mark it up. What do you recognize? What information does the header contain? What information does the body contain? How does your browser take this information and create something that looks nice?

\item This part uses port scanning. You will be scanning only your own ports. \textbf{Do not scan ports without permission!}

What does it mean for a port to be open? What are the security implications of an open port?

Use \verb|nmap| to scan the ports on your Raspberry Pi:
\begin{minted}{bash}
nmap localhost
\end{minted}
Which ports are open? Explain each open port (you may need to look some things up)

Now scan your laptop. What's the same? What's different? Why?

\end{enumerate}
$$$

## Transport Layer

$$$
\begin{enumerate}
\item Use \verb|nc| to create a basic chat between two terminal windows on different machines on the same network. The easiest setup is to use a Mac and a Pi plugged into that Mac.

Choose one machine to be the server. Make note of its IP address:
\begin{minted}{bash}
hostname -I
\end{minted}
Tell the server to listen on port 5555 (or whatever port you like):
\begin{minted}{bash}
nc -l 5555
\end{minted}
Now tell the client (the other machine) to connect to that port on the server:
\begin{minted}{bash}
nc <SERVER IP ADDRESS> 5555
\end{minted}

Type some text on the server side and hit enter. What happens? Do the same on the client side. 

Use Ctrl+C to kill the process on the server side. What happens on the client side? Why? Do you suppose this connection was TCP or UDP?

\item Create another \verb|nc| connection, but this time use the \verb|-u| flag. On the server:
\begin{minted}{bash}
nc -u -l 5555
\end{minted}
On the client:
\begin{minted}{bash}
nc <SERVER IP ADDRESS> 5555
\end{minted}
Confirm that your connection is established and the "chat" functionality works both ways. Then use Ctrl+C to kill the process on the server side. What happens on the client side? How is this different from before?






\end{itemize}




\end{enumerate}

$$$





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


$$$
\begin{enumerate}
\item Explain the difference between public IP address and private IP address. What are the public and private IP addresses of your Pi? What are the public and private IP addresses of your laptop? Compare these with a classmate.

\item Run \verb|traceroute| for a website. Explain the output. Can you get it to produce rows of asterisks? What's happening?

\end{enumerate}

$$$


- run `traceroute google.com`. route from the current machine to google HQ. do you see rows of asterisks? what do you suppose it means?
- run `ip route`. find your own IP, verify that it's private
- run `ip route`. find the default via IP. default gateway (router... probably the laptop)
- `traceroute 8.8.8.8`

Hands-on Pi Exercise: ip and traceroute
This makes the abstract "path" visible to the students.
Command 1: ip addr
Goal: Find their own IP and identify if it's Private (usually starts with 192.168 or 10.).
Command 2: ip route
Goal: Find the default via IP. This is their "Default Gateway" (the Router).
Command 3: traceroute 8.8.8.8
Goal: Watch the packet "hop" through different routers across the world. They will see the latency (ms) increase as the packet physically travels further away.


## Link Layer


Hands-on Pi Exercise: ip link and arp
Let the students see their hardware's "fingerprint."
Command 1: ip link show
Goal: Find the link/ether line. That 12-digit hex code (e.g., b8:27:eb...) is their Pi's unique MAC address.
Command 2: arp -a
Goal: See the "Address Resolution" table. This shows every other device the Pi has talked to recently and their corresponding MAC addresses.
Activity: Have two students compare their MAC addresses. They'll notice the first 6 digits are often identical—that's the "OUI" (Organizationally Unique Identifier) that identifies the manufacturer as Raspberry Pi Trading Ltd.

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

