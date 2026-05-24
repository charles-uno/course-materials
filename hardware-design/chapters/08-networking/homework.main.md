template: assignment.tex
---

# Networking

TODO: make sure we are using Linux syntax that everyone can do on the Pi. Avoid Mac-specific commands unless necessary (and if so, call them out as such)

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

\begin{enumerate}
\item Make a note of five different \verb|GET| requests. Explain in words what each of those requests is doing. Don't explain the whole page -- just explain \textit{that} request specifically.
\item Do the same for five different \verb|POST| requests. 
\item HTTP also supports several other types of request, such as \verb|PUT| and \verb|DELETE|. Can you find a case where the browser sends any of these? Please explain either way. You can look this up, but make sure what you turn in reflects your own understanding!
\end{enumerate}

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
\begin{enumerate}
\item What does it mean for a port to be open? What are the security implications of an open port?
\item Use \verb|nmap| to scan the ports on your Raspberry Pi:
\begin{minted}{bash}
nmap localhost
\end{minted}
Which ports are open? Explain each open port (you may need to look some things up)
\item Now scan your laptop. What's the same? What's different? Why?
\end{enumerate}
\end{enumerate}
$$$

% NOTE: maybe play with Wireshark in the future? this requires an additional download

## Transport Layer

$$$
\begin{enumerate}
\item For this part you will use \verb|nc| to create a basic TCP chat between two terminals on different machines. The easiest setup is to use a Mac and a Pi plugged into that Mac.

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

\begin{enumerate}
\item Type some text on the server side and hit enter. What happens? Do the same on the client side. 
\item Use Ctrl+C to kill the process on the server side. What happens on the client side? Why? 
\end{enumerate}

\item Create another \verb|nc| connection, but this time use UDP instead of TCP. On the server:
\begin{minted}{bash}
nc -u -l 5555
\end{minted}
On the client:
\begin{minted}{bash}
nc -u <SERVER IP ADDRESS> 5555
\end{minted}
\begin{enumerate}
\item Confirm that your connection is established and the "chat" functionality works both ways. 
\item Use Ctrl+C to kill the process on the server side. What happens on the client side? How is this different from the TCP connection? Why?
\end{enumerate}

\item Create another \verb|nc| chat using UDP. This time, be sure to choose your Raspberry Pi as the server (and your laptop as the client).
\begin{enumerate}
\item Send some messages to confirm the connection.
\item Use Ctrl+C to kill the connection. Unplug the server (Pi) completely. Now try sending a message from the client side. What happens? How is this different from before? Why?
\end{enumerate}

\end{enumerate}

$$$

% note for next time: tcdump? looks like this will let us see SYN and ACK flags in real time

## Internet Layer

$$$
\begin{enumerate}
\item Explain the difference between public IP address and private IP address. What are the public and private IP addresses of your Pi? What are the public and private IP addresses of your laptop? Compare these with a classmate. Explain what you see.

\item Run \verb|traceroute| for a website. Explain the output. Can you get it to produce rows of asterisks? What's happening?

\item Use \verb|ping| to find the largest IP packet that can be sent without breaking it into pieces. How many bytes can you send at once?
\begin{minted}{bash}
ping -s <SIZE> <URL>
\end{minted}
Note: if you can't get it to fail, you may need to add the \verb|-D| flag. This explicitly tells \verb|ping| not to divide the data into multiple packets.

\item Use the \verb|-t| flag to explicitly set the TTL on a \verb|ping| packet:
\begin{minted}{bash}
ping -t <TTL> <URL>
\end{minted}
How many hops does it take to get to Google? Try a few other well-known websites. Which are closer? Which are further away?

\end{enumerate}

$$$


## Link Layer

$$$
\begin{enumerate}
\item We use IP addresses to navigate online, but IP addresses are transient. Let's look at some MAC addresses.

\begin{enumerate}
\item What is a MAC address?
\item Use \verb|ifconfig| to look up the MAC addresses for your machine. You may need to look up how to read the output. How many MAC addresses are there? Why?
\item Ask a classmate for their IP address. Ping their machine. If you went to a different part of campus, would this IP address change?
\item Look up your machine's ARP table:
\begin{minted}{bash}
arp -a
\end{minted}
What do you see? If you went to a different part of campus, would the MAC addresses here change?
\item Compare the MAC addresses of several Raspberry Pis. What do you notice? Why might this be?
\end{enumerate}

\end{enumerate}
$$$

% sudo ip link set eth0 down && sleep 10 && sudo ip link set eth0 up
% set the link down without locking yourself out permanently