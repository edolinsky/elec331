# ELEC 331 Wireshark Lab: TCP

1. What is the IP address and TCP port number used by the client computer
(source) that is transferring the file to gaia.cs.umass.edu?

The IP address used bt the client computer is 192.168.1.102, and the port used
is 1161.

2. What is the IP address of gaia.cs.umass.edu? On what port number is it
sending and receiving TCP segments for this connection?

The IP address of gaia.cs.umass.edu is 128.119.245.12, and the port number used
here is 80, which means that it is an http web server.

3. What is the IP address and TCP port number used by your client computer
(source) to transfer the file to gaia.cs.umass.edu?

The IP address and TCP port number used by my computer are 10.0.0.11 and 40932,
respectively.

4. What is the sequence number of the TCP SYN segment that is used to initiate
the TCP connection between the client computer and gaia.cs.umass.edu? What is it
in the segment that identifies the segment as a SYN segment?

The sequence number of the TCP SYN segment used to initiate the TCP connection
between the client computer and gaia.cs.umass.edu is 0 (trace No. 1). The second
least significant bit in Flags is set to identify this segment as a SYN segment.

5. What is the sequence number of the SYNACK segment sent by gaia.cs.umass.edu
to the client computer in reply to the SYN? What is the value of the
Acknowledgement field in the SYNACK segment? How did gaia.cs.umass.edu
determine that value? What is it in the segment that identifies the segment as a
SYNACK segment?

The sequence number of the SYNACK segment in response to the SYN is also 0, and
the value of the acknowledgement field is 1. This is determined by incrementing
the initial sequence number provided by the client (i.e. 0+1=1). Both the
Acknowledgement and Syn flags are set, identifying this as a SYNACK segment.
(trace No. 2)

6. What is the sequence number of the TCP segment containing the HTTP POST
command?

The sequence number of the TCP segment containing the HTTP POST command is 1
(trace No. 4).

7. Consider the TCP segment containing the HTTP POST as the first segment in the
TCP connection. What are the sequence numbers of the first six segments in the
TCP connection (including the segment containing the HTTP POST)? At what
time was each segment sent? When was the ACK for each segment received?
Given the difference between when each TCP segment was sent, and when its
acknowledgement was received, what is the RTT value for each of the six
segments? What is the EstimatedRTT value (see Section 3.5.3, page 242 in
text) after the receipt of each ACK? Assume that the value of the
EstimatedRTT is equal to the measured RTT for the first segment, and then is
computed using the EstimatedRTT equation on page 242 for all subsequent
segments.

The sequence numbers of the first six segments in the TCP connection are as
follows:

| Trace No. | Sequence No. | Time Sent | ACK Rec. Time |   RTT    | EstimatedRTT |
| :-------- | :----------- | :-------- | :------------ | :------- | :----------- |
|     4     |        1     |  0.026477 |    0.053937   | 0.02746  |    0.02746   |
|     5     |      565     |  0.041737 |    0.077294   | 0.035557 |    0.028472  |
|     7     |     2026     |  0.054026 |    0.124085   | 0.070059 |    0.03367   |
|     8     |     3486     |  0.054690 |    0.169118   | 0.114428 |    0.043765  |
|    10     |     4946     |  0.077405 |    0.217299   | 0.139894 |    0.055781  |
|    11     |     6406     |  0.078157 |    0.267802   | 0.189645 |    0.072514  |

-- add calculations --

8. What is the length of each of the first six TCP segments?

| Trace No. | Length (bytes) |
| :-------- | :------------- |
|     4     |       565      |
|     5     |      1460      |
|     7     |      1460      |
|     8     |      1460      |
|    10     |      1460      |
|    11     |      1460      |

9. What is the minimum amount of available buffer space advertised at the received
for the entire trace? Does the lack of receiver buffer space ever throttle the
sender?

The minimum amount of buffer space advertised by gaia.cs.umass.edu over the
course of the trace is 5840 bytes, as displayed in the first SYNACK. The lack of
receiver buffer space seems to not throttle the sender whatsoever.


10. Are there any retransmitted segments in the trace file? What did you check for
(in the trace) in order to answer this question?

There are no retransmitted segments in the trace file. I checked for a second
entry for the any particular segment, with an identical sequence number.

11. How much data does the receiver typically acknowledge in an ACK? Can you
identify cases where the receiver is ACKing every other received segment (see
Table 3.2 on page 250 in the text).

Early on, the receiver sends an ACK for every single segment (565, 1460 bytes).
Later in the trace (roughly frame 60 onwards), the receiver starts sending an
ACK for every two segments received (2920 bytes).

12. What is the throughput (bytes transferred per unit time) for the TCP
connection? Explain how you calculated this value.

The total time from the start of transmission (frame 4) to the final TCP ACK
(frame 206) is (5.651141 - 0.026477) = 5.624664 seconds. The size of the data
file is 152138 bytes, so the average throughput is
(152138 * 8 / 1000) / 5.624664 = 216.386969959 Kbits/sec.

13. Use the Time-Sequence-Graph(Stevens) plotting tool to view the sequence
number versus time plot of segments being sent from the client to the
gaia.cs.umass.edu server. Can you identify where TCP’s slowstart phase begins
and ends, and where congestion avoidance takes over? Comment on ways in
which the measured data differs from the idealized behavior of TCP that we’ve
studied in the text.

The graph shows that the slowstart phase ends within the first 0.2 seconds. Thus,
congestion control is almost always on. The theoretical linear increase seems
not to apply; instead it is transmitting in bursts of 5. This bursting effect
cannot be the result of flow control, as the advertised threshold is much larger
than 5 packets.

14. Answer each of two questions above for the trace that you have gathered when
you transferred a file from your computer to gaia.cs.umass.edu

(2.060510379 - 1.683368957) = 0.377141422 seconds
((152138/1000) * 8) / 0.377141422 = 3227.18197738 Kbits/sec = 3.23 Mbits/sec

The graph shows almost no sign of slow start, but similar bursts. However, the
bursts increase in size with each successive burst. Congestion control is also
on here, and flow control does not take over.
