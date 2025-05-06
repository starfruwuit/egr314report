---
title: Block Diagram
---
![Block Diagram](BiDirectionalInternetComm314.drawio.png)
This block diagram for Team STEMteresting's Bidirectional Internet Communication is up-to-date as of May 05, 2025. 

## Decision-Making Process
I decided to use the ESP32-S3-WROOM module because it has wi-fi capabilities, which the PIC chips do not, and was familiar to me from previous in-class labs. Via the MQTT Server, my subsystem is able to both publish and receive messages over wi-fi. In addition to this, my subsystem may receive messages from my teammates' boards via UART module 2, which is connected to pins RX2 and TX2. 