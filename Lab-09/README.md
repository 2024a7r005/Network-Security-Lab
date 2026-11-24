# Configure and Analyze IPsec VPN in Tunnel Mode

## Aim
To configure an IPsec VPN in Tunnel Mode and analyze encrypted packet flow to understand secure VPN communication.

## Introduction
IPsec (Internet Protocol Security) is a network security protocol suite used to secure communication over IP networks. It provides authentication, data integrity, and encryption to protect transmitted data.

Tunnel Mode encrypts the entire original IP packet and encapsulates it inside a new IP packet. It is commonly used in site-to-site VPN connections.

## Objectives
- Understand IPsec VPN and Tunnel Mode.
- Configure a secure VPN connection.
- Analyze encrypted packet transmission.
- Understand the role of ESP (Encapsulating Security Payload).
- Observe secure communication using Wireshark.

## Technologies and Tools
- IPsec VPN
- Wireshark
- Operating System: Kali Linux / Linux
- IKE (Internet Key Exchange)
- ESP (Encapsulating Security Payload)

## Working of IPsec Tunnel Mode
1. Two VPN gateways establish a secure connection.
2. IKE negotiates security parameters and establishes Security Associations (SAs).
3. The original IP packet is encrypted and encapsulated.
4. ESP provides encryption and data integrity.
5. The encrypted packet travels through the public network.
6. The receiving VPN gateway decrypts and decapsulates the packet.
7. The original packet is forwarded to its destination.

## Packet Analysis
Wireshark is used to capture and analyze network traffic.

The following details can be observed:
- ESP protocol packets.
- Source and destination IP addresses.
- Encrypted payload data.
- IPsec packet encapsulation.
- IKE negotiation traffic.

The original application data is not directly readable in the encrypted ESP payload.

## Security Features
- **Confidentiality:** Encrypts data to prevent unauthorized access.
- **Integrity:** Detects unauthorized modification of packets.
- **Authentication:** Verifies communicating VPN peers.
- **Anti-replay protection:** Helps prevent attackers from retransmitting captured packets.

## Result
Successfully studied the configuration and working of IPsec VPN in Tunnel Mode and analyzed encrypted packet flow to understand secure VPN communication.

## Conclusion
IPsec Tunnel Mode provides secure communication by encrypting and encapsulating complete IP packets. Packet analysis using Wireshark helps understand how VPN communication protects data during transmission.
