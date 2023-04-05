# N-W_Simulator_assignmet_project_1




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
