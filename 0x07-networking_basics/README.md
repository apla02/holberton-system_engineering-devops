# 0x07-networking_basics
# link to the project:  https://intranet.hbtn.io/projects/259

# General objectives

## OSI Model

>### What it is
>OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

>It is organized from the lowest level to the highest level and it has 7 layers:

>The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc



|  Layer |  Function |
|---|---|
| Layer 7: Application  |Interacts with software applications that implement a communicating component.   |
|  Layer 6: Presentation |  Converts incoming and outgoing data from one presentation format to another (Data encryption, text compression). |
| Layer 5: Session  |   Controls the connections between computers. Establishes, manages and terminates the connection.|
| Layer 4: Transport  |  Ensures data transfer from a source to a destination host across one or more networks. |
|  Layer 3: Network |  Routes data packets between two nodes on a network using an IP address |
|   Layer 2: Data Link|   Provides a reliable connection between two connected nodes by detecting errors at the physical layer.|
| Layer 1: Physical  |  Transmits a bit stream over physical media such as coax or fiber cable. |


## What is a LAN
>- A local area network (LAN) is a collection of devices connected together in one physical location, such as a building, office, or home. A LAN can be small or large, ranging from a home network with one user to an enterprise network with thousands of users and devices in an office or school.


## What is a WAN
>- In its simplest form, a wide-area network (WAN) is a collection of local-area networks (LANs) or other networks that communicate with one another.  A WAN is essentially a network of networks, with the Internet the world's largest WAN.


## What is the Internet
>- It is a global network of computers that works much like the postal system, only at sub-second speeds. Just as the postal service enables people to send one another envelopes containing messages, the internet enables computers to send one another small packets of digital data.

>### What is an IP address
>- An Internet Protocol address is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication. An IP address serves two main functions: host or network interface identification and location addressing.

>### What is a mac adress
>- A media access control address (MAC address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment.

>### What are the 2 types of IP address
>- There are two types of IP addresses – public and private. Public IPs are used by routers and by computers connected directly to DSL modems without a router. Private IP addresses are special IP addresses that are known only to a router and its home network.

>### What is localhost
>- localhost is a hostname that refers to the current computer used to access it. It is used to access the network services that are running on the host via the loopback network interface.

>### What is a subnet
>- A subnetwork or subnet is a logical subdivision of an IP network. The practice of dividing a network into two or more networks is called subnetting. Computers that belong to a subnet are addressed with an identical most-significant bit-group in their IP addresses.

>### Why IPv6 was created
>- Pv6 (Internet Protocol version 6) is a new version of IP protocol designed to solve problems that the previous version (IPv4) encountered by using an address length of 128 bits rather than 32. The protocol was developed by IETF. IPv6 was specifically designed to solve address space exhaustion.

## TCP/UDP

>### What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
>- The two most important protocols in the Transport Layer are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP). 

>### What is the main difference between TCP and UDP
>- TCP provides reliable data delivery service with end-to-end error detection and correction. UDP provides low-overhead, connectionless datagram delivery service. Both protocols deliver data between the Application Layer and the Internet Layer. Applications programmers can choose whichever service is more appropriate for their specific applications.

>### what is a datagram
>- A datagram is a basic transfer unit associated with a packet-switched network. Datagrams are typically structured in header and payload sections. Datagrams provide a connectionless communication service across a packet-switched network. The delivery, arrival time, and order of arrival of datagrams need not be guaranteed by the network.

>### What is a port
>- A port is a virtual point where network connections start and end. Ports are software-based and managed by a computer's operating system. Each port is associated with a specific process or service. Ports allow computers to easily differentiate between different kinds of traffic: emails go to a different port than webpages, for instance, even though both reach a computer over the same Internet connection.

>### What is a port number?

>- Ports are standardized across all network-connected devices, with each port assigned a number. Most ports are reserved for certain protocols — for example, all Hypertext Transfer Protocol (HTTP) messages go to port 80. While IP addresses enable messages to go to and from specific devices, port numbers allow targeting of specific services or applications within those devices.

>### Memorize SSH, HTTP and HTTPS port numbers
>- SSH: 22
HTTP/HTTPS: 80/443

>### What tool/protocol is often used to check if a device is connected to a network
>- Ping is a computer network administration software utility used to test the reachability of a host on an Internet Protocol (IP) network. It is available for virtually all operating systems that have networking capability, including most embedded network administration software. 

>to use ping in linux
>ping -c 5
>### What is ICMP

>- The Internet Control Message Protocol (ICMP) is a supporting protocol in the Internet protocol suite. It is used by network devices, including routers, to send error messages and operational information indicating success or failure when communicating with another IP address, for example, an error is indicated when a requested service is not available or that a host or router could not be reached.[2] ICMP differs from transport protocols such as TCP and UDP in that it is not typically used to exchange data between systems, nor is it regularly employed by end-user network applications (with the exception of some diagnostic tools like ping and traceroute). 



Sources:
>- https://www.cisco.com/c/en/us/products/switches/ 

>- what-is-a-lan-local-area-network.html
>- https://www.cisco.com/c/en/us/products/switches/

>- what-is-a-wan-wide-area-network.html
>- https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/
>- https://nfware.com/blog-what-is-ipv6
>- https://www.cyberciti.biz/faq/
>- https://www.oreilly.com/library/view/windows-nt-tcpip/1565923774/ch01s06.html
>- https://geekflare.com/default-port-numbers/
>- how-do-i-find-out-what-ports-are-listeningopen-on-my-linuxfreebsd-server/
>- https://linux.die.net/man/8/netstat
>- https://linux.die.net/man/8/ping
>- https://www.reiser.cl/bash-validar-archivos-pasados-como-parametros/
