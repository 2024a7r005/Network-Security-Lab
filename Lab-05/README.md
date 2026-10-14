# Experiment 5: Capture and Analyze a TLS Handshake Using Wireshark

## Aim
To capture and analyze a TLS handshake using Wireshark and understand how HTTPS communication is secured through TLS negotiation, certificate verification, and encryption.

## Objectives
- Capture HTTPS traffic using Wireshark.
- Analyze ClientHello and ServerHello messages.
- Identify the negotiated TLS version and cipher suite.
- Configure TLS key logging to inspect encrypted handshake messages.
- Examine server certificate details.

## Tools Required
- Wireshark
- Web browser
- Internet connection
- TLS key log file

## Theory
TLS (Transport Layer Security) protects communication between a client and a server. During the handshake, the client and server negotiate security parameters and establish encryption keys. Wireshark helps capture and analyze the handshake messages and certificate information.

## Methodology
1. Select the active network interface in Wireshark.
2. Apply the capture filter `tcp port 443` and start capturing packets.
3. Open a fresh browser window and visit `https://www.wireshark.org/`.
4. Stop the capture and save it as `exp5_tls_handshake.pcapng`.
5. Apply the display filter `tls` and inspect ClientHello.
6. Analyze ServerHello and record the negotiated TLS version and cipher suite.
7. Configure browser TLS key logging and load the key log in Wireshark.
8. Capture a fresh HTTPS session, verify decryption, and inspect the certificate and handshake messages.

## Important Wireshark Filters

```text
tls
```

```text
tls.handshake.type == 1
```

```text
tls.handshake.type == 2
```

## Results
The TLS handshake was captured and analyzed using Wireshark. The ClientHello and ServerHello messages were examined to understand TLS negotiation. TLS decryption and certificate inspection were performed to study the protected handshake.

*Update this section according to the results actually observed during the experiment.*

## Discussion
The experiment demonstrates how TLS negotiates security parameters and protects HTTPS communication. It also explains how TLS key logging can help analyze encrypted handshake messages in Wireshark.

## Improvements
- Compare TLS handshakes from two different websites.
- Enable TLS decryption and compare packet details before and after.
- Inspect certificate hostname, issuer, and expiry date.
- Use display filters to isolate handshake messages for easier analysis.

## Conclusion
This experiment provides practical experience in capturing HTTPS traffic, analyzing TLS handshake messages, and understanding the role of certificates and encryption in secure communication.

## Safety Note
Capture only authorized traffic. Protect TLS key log files because they contain sensitive session secrets.
