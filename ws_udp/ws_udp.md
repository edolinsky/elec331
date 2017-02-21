# ELEC 331 Wireshark Lab: UDP

1. Select one UDP packet from your trace. From this packet, determine how many
fields there are in the UDP header. (You shouldn’t look in the textbook! Answer
these questions directly from what you observe in the packet trace.) Name these
fields.

In this packet, there are 4 fields in the UDP header. These fields are:
  * Source port
  * Destination port
  * Length
  * Checksum

2. By consulting the displayed information in Wireshark’s packet content field
for this packet, determine the length (in bytes) of each of the UDP header
fields.

|      Feild       | Length (bytes) |
| :--------------- | :------------- |
| Source Port      |        2       |
| Destination Port |        2       |
| Length           |        2       |
| Checksum         |        2       |

3. The value in the Length field is the length of what? (You can consult the
text for this answer). Verify your claim with your captured UDP packet.

The value of the length field (58 Bytes) is the total length of the UDP segment,
including both the payload and header. Each of the header fields is 2 bytes, and
the payload is 50 bytes. (50 + 4 * 2) = 58 bytes.

4. What is the maximum number of bytes that can be included in a UDP payload?
(Hint: the answer to this question can be determined by your answer to 2. above)

As the length field is 2 bytes long, the maximum total segment size is
(2^16) - 1 = 65535 bytes. Subtracting the size of the header, we get 65527 for
the maximum number of bytes that can be included in a UDP payload.

5. What is the largest possible source port number? (Hint: see the hint in 4.)

The largest possible source port number is (2^16) - 1 = 65535.

6. What is the protocol number for UDP? Give your answer in both hexadecimal and
decimal notation. To answer this question, you’ll need to look into the Protocol
field of the IP datagram containing this UDP segment (see Figure 4.13 in the
text, and the discussion of IP header fields).

The UDP protocol number is 0x11, or decimal 17.

7. Examine a pair of UDP packets in which your host sends the first UDP packet
and the second UDP packet is a reply to this first UDP packet. Describe the
relationship between the port numbers in the two packets.

The source and destination port numbers for the packet sent by my host (4334 and
161, respectively) are the reverse of the source and destination (161 and 4334,
respectively) sent to my host. This means that the two packets are the two parts
of a query and response exchange. The first is the query, the second the response.
