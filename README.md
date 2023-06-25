# N-W_Simulator_assignmet_project_1 (Network_Simulator_complete is final file where as Nw_sim_upto_data_link_layer.py is upto data link layer )




# Physical and Data Link Layers

This repository contains implementations of the Physical and Data Link layers .

## Physical Layer

The Physical layer is the first layer of the OSI model and is responsible for the transmission and reception of unstructured raw data between devices. This layer deals with the mechanical, electrical, and timing aspects of transmitting bits over the medium, and is responsible for the physical addressing of devices on the network through the use of MAC addresses.

### Functions

- Transmits and receives raw bit streams over the medium.
- Defines the physical characteristics of the transmission medium, such as voltage levels, signal timing, and data rate.
- Handles the synchronization between sender and receiver devices.
- Defines the MAC addressing scheme for identifying devices on the network.
- Provides the foundation for all other layers of the OSI model.

## Data Link Layer

The Data Link layer is the second layer of the OSI model and is responsible for the transmission and reception of structured data frames over the physical medium. This layer provides a means for error detection, error correction, and flow control to ensure that the data is transmitted without errors and congestion is prevented.

### Functions

- Transmits and receives structured data frames over the physical medium.
- Provides error detection, error correction, and flow control to ensure reliable transmission.
- Defines the format and structure of the data frames and rules for accessing the medium.
- Handles the MAC sublayer for addressing devices on the network and identifying unique devices through their MAC addresses.
- Operates in two sublayers: the Logical Link Control (LLC) sublayer and the MAC sublayer.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `urllib3`.

```bash
pip install urllib3
```







3.Network layer: Handles the routing and sending of data between different networks. The most important protocols at this layer are IP and ICMP. We have implemented the Routing Information Protocol-(RIP) in the project for shortest path.

4.Transport layer: Provides the means for transmitting data between the two connected parties, as well as controlling the quality of service. The main protocols used here are TCP and UDP. We have set a probability for packet drop in UDP to show that this protocol is unreliable. TCP is a reliable protocol where no packet drop is shown. A server class is made to enable the 3 services we have included HTTP, SSH, SMTP.

5.Application Layer: The application layer is the highest abstraction layer of the TCP/IP model that provides the interfaces and protocols needed by the users. It combines the functionalities of the session layer, the presentation layer and the application layer of the OSI model. We have included two application layer services DHCP and HTTP .
 
