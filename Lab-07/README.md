# WPA2 Wireless Security Analysis Using Wireshark

## Overview
This experiment focuses on capturing and analyzing the WPA2 Four-Way Handshake using Wireshark to understand how secure wireless communication is established between a client and a wireless access point.

## Aim
To capture and analyze the WPA2 Four-Way Handshake process using Wireshark and understand secure wireless authentication and key establishment.

## Tools Used
- Wireshark
- WPA2-enabled Wi-Fi network
- Wireless network adapter

## Theory
WPA2 (Wi-Fi Protected Access 2) is a wireless security protocol that protects Wi-Fi communication using encryption. It commonly uses AES-CCMP.

The Four-Way Handshake consists of four messages exchanged between the client and access point:

1. **Message 1:** Access Point sends ANonce.
2. **Message 2:** Client sends SNonce and MIC.
3. **Message 3:** Access Point sends key installation information.
4. **Message 4:** Client acknowledges the exchange.

## Methodology
1. Open Wireshark and select the wireless network interface.
2. Start packet capture.
3. Connect an authorized client to the WPA2 Wi-Fi network.
4. Apply the `eapol` display filter.
5. Identify and inspect the handshake packets.
6. Analyze nonce, MIC, replay counter and key-information fields.
7. Save the packet capture for further analysis.

## Practical Improvements
- Analyzed timestamps to compare the time intervals between handshake messages.
- Examined key-information flags across the four messages.
- Inspected EAPOL packet details for better understanding of key establishment.
- Saved the capture for future reference and comparison.

## Result
Successfully captured and analyzed WPA2 handshake traffic using Wireshark. The EAPOL packets provided insight into the four-way handshake and the process of establishing secure wireless communication.

## Learning Outcomes
- Understood WPA2 wireless security.
- Learned the four-way handshake mechanism.
- Identified EAPOL packets using Wireshark filters.
- Examined key-exchange fields and authentication information.

## Conclusion
The experiment provided practical understanding of WPA2 authentication and key establishment. Wireshark helped visualize and analyze the packet exchange involved in securing wireless communication.

## Safety Note
Perform packet capture and analysis only on networks for which you have authorization.
