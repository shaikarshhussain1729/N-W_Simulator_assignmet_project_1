import random
import time

import urllib3


class EndDevice:

    def Generate_mac_address():
        mac_addresss = [str(random.randint(0x00, 0xFF)) for x in range(5)]
        return ("00:" + ":".join(mac_addresss))
    """GENERATES RANDOM MAC ADDRESS ANS ASSIGNS TO END-DEVICES"""

# This is a class constructor for EndDevice
    def __init__(self, i,p,d,s):
        self.ip = ""
        # Generate a random MAC address using the Generate_mac_address function
        self.mac = EndDevice.Generate_mac_address()
        # Set the port to the value passed in as an argument
        self.port = p
        # Set the data to the value passed in as an argument
        self.data = d
        # Set the sequence number to the value passed in as an argument
        self.seq_no = s
        # Set the subnet to an empty string
        self.subnet = ""
        # Set the gateway to an empty string
        self.gateway = ""
        # Set the dynamic flag to 0
        self.dynamic = 0
        # Set the message to an empty string
        self.message= ""


    def display(Gen):
        print("ip address is " + str(Gen.ip))
        print("mac address is " + EndDevice.Generate_mac_address() )
        print("port value = " + str(Gen.port))


e1 = EndDevice("192.168.0.10", 0, "No data", 1)
e2 = EndDevice("192.168.0.11", 0, "No data", 2)
e3 = EndDevice("192.168.0.12", 0, "No data", 3)
e4 = EndDevice("192.168.0.13", 0, "No data", 4)
e5 = EndDevice("192.168.0.14", 0, "No data", 5)
e6 = EndDevice("192.168.0.15", 0, "No data", 6)
e7 = EndDevice("192.168.0.16", 0, "No data", 7)
e8 = EndDevice("192.168.0.17", 0, "No data", 8)
e9 = EndDevice("192.168.0.18", 0, "No data", 9)
e10 = EndDevice("192.168.0.19", 0, "No data", 10)


endDevices = [-1, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
processes = [1, 2, 3]


def End_Device_Vacant():
    eport = [e1.port, e2.port, e3.port, e4.port, e5.port, e6.port, e7.port, e8.port, e9.port, e10.port]
    for i in range(0, 11):
        if eport[i] == 0:
            return 0
        else:
            return 1
    """CHECKS IF END-DEVICE IS VACANT OR NOT"""


class Hub:
    def __init__(self):
       self.port1 = 0
       self.port2 = 0
       self.port3 = 0
       self.port4 = 0
       self.port5 = 0
       self.port6 = 0
    def Hub_vacant(self):
        plist = [self.port1, self.port2, self.port3, self.port4, self.port5, self.port6]
        for i in range(0, 6):
            if plist[i] == 0:
                return 0
            else:
                return 1
    """CHECKS WHETHER HUB HAS ANY PORT VACANT OR NOT"""


Hub1 = Hub()
Hub2 = Hub()


class Switch:

    def __init__(self):
        self.port1 = 0
        self.port2 = 0
        self.port3 = 0
        self.port4 = 0
        self.port5 = 0
        self.port6 = 0
        self.port7 = 0

    def Switch_vacant(self):
        slist = [self.port1, self.port2, self.port3, self.port4, self.port5, self.port6, self.port7]
        for i in range(0,8):
            if slist[i] == 0:
                return 0
            else:
                return 1
    """CHECKS WHETHER SWITCH HAS ANY PORT VACANT OR NOT"""

    maclist1 = [0, 0, 0, 0, 0]
    maclist2 = [0, 0, 0, 0, 0]
    """MAC ADDRESS LIST FOR ADDRESS LEARNING"""


Switch1 = Switch()

Switch2 = Switch()



"""-----------------------------FLOW CONTROL PROTOCOL: STOP AND WAIT ARQ------------------------------------"""





def stop_and_wait_arq_HUb(a, b, c):

    sender = 0
    receiver = 0
    s = 0
    ack = 0
    for i in range(0, len(c)):
        if i % 2 == 0:
            s = 0
            ack = 1
        else:
            s = 1
            ack = 0
        c1 = Switch1.maclist1.count(endDevices[b].mac)
        c2 = Switch1.maclist2.count(endDevices[b].mac)
        if c1 == 0 and c2 == 0:
            print("Mac Address of End Device", b, "not found in the MAC table")
            print("Switch will broadcast the message\n")

            if i != 0 and i % 4 == 0:
                print("Time out occurred, Sending the", i, "th frame again. Sequence number :", s)
            print("Sending First packet  -----", c[0], "-----")
            for j in range(1, 11):
                if j != a:
                    endDevices[j].data = c[i]
                    print("Message sent to End Device", j)
                if j == b:
                    print("Ack received by End Device", b, "ACK NO :", ack)
            print("\n")
            if a < 6:
                Switch1.maclist1[a - 1] = endDevices[a].mac
            else:
                Switch1.maclist2[a - 6] = endDevices[a].mac
            if b < 6:
                Switch1.maclist1[b - 1] = endDevices[b].mac
            else:
                Switch1.maclist2[b - 6] = endDevices[b].mac
        else:
            if (a < 6 and b < 6):
               print("Mac Address found, Both Devices in Hub 1")
               print("Sending  packet -----", c[i], "-----")
               if i != 0 and i % 4 == 0:
                  print("Time out occurred, Sending the", i, "th frame again. Sequence number :", s)
               for j in range(1, 6):
                    if j != a:
                       endDevices[j].data = c[i]
                       print("Message sent to End Device", j)
                    if j == b:
                       print("Ack received by End Device", b, "ACK NO :", ack)
               print("\n")
            elif a > 6 and b > 6:
                print("Mac Address found, Both Devices in Hub 2")
                print("Sending  packet -----", c[i], "-----")
                if i != 0 and i % 4 == 0:
                    print("time out occurred, Sending the", i, "th frame again. Sequence number :", s)
                for j in range(6, 11):
                    if j != a:
                        endDevices[j].data = c[i]
                        print("Message sent to End Device", j)
                    if j == b:
                        print("Ack received by End Device", b, "ACK NO :", ack)
                print("\n")
            else:
                print("Mac Address of End Device", b, "  found in the MAC table")
                print("Sending  packet -----", c[i], "-----")
                print("Sending to other port")
                if i != 0 and i % 4 == 0:
                    print("time out occurred, Sending the", i, "th frame again. Sequence number :", s)
                for j in range(1, 11):
                    if j != a:
                        endDevices[j].data = c[i]
                        print("Message sent to End Device", j)
                    if j == b:
                        print("Ack received by End Device", b, "ACK NO :", ack)
                print("\n")
                if a < 6:
                    Switch1.maclist1[a - 1] = endDevices[a].mac
                else:
                    Switch1.maclist2[a - 6] = endDevices[a].mac
                if b < 6:
                    Switch1.maclist1[b - 1] = endDevices[b].mac
                else:
                    Switch1.maclist2[b - 6] = endDevices[b].mac



def stop_and_wait_arq(a, b, c):

    sender = 0
    receiver = 0
    s = 0
    ack = 0
    for i in range(0, len(c)):
        if i % 2 == 0:
            s = 0
            ack = 1
        else:
            s = 1
            ack = 0
        c1 = Switch1.maclist1.count(endDevices[b].mac)
        if c1 == 0:
            print("Mac Address of End Device", b, "not found in the MAC table")
            print("Switch will broadcast the message\n")
            print("Sending  packet -----", c[i], "-----")
            if i != 0 and i % 4 == 0:
                print("time out occurred, Sending the", i, "th frame again. Sequence number :", s)
            for j in range(1, 6):
                if j != a:
                    endDevices[j].data = c[i]
                    print("Message sent to End Device", j)
                if j == b:
                    print("Ack received by End Device", b, "ACK NO :", ack)
            print("\n")
            Switch1.maclist1[a - 1] = endDevices[a].mac
            Switch1.maclist1[b - 1] = endDevices[b].mac


        else:
                print("Mac Address of End Device", b, "found in the MAC table")
                print("Sending  packet -----", c[i], "-----")
                if i != 0 and i % 4 == 0:
                    print("time out occurred, Sending the", i, "th frame again. Sequence number :", s)
                print("Message sent to End Device", b)
                print("ACK received from End Device ", b)
                print("\n")
                Switch1.maclist1[a - 1] = endDevices[a].mac
                Switch1.maclist1[b - 1] = endDevices[b].mac






"""-----------------------------FLOW CONTROL PROTOCOL: SELECTIVE REPEAT------------------------------------"""






def Selective_Repeat_Hub(a,b,c):

    print("Enter the reserved bit size for Seq no")
    m = int(input())
    sf = 0
    sn = 0
    x = len(c)
    Window_Size = 2**(m-1)
    Seq_no = 2**m
    array = [0]*x
    visited = [0]*x
    while x != 0:
        marker = 0
        while sn < sf + Window_Size and sn < len(c):
          if array[sn] == 0:
            if sn % 3 == 0 and visited[sn] == 0:
                    print(sn, "-th packet lost, Sending next packet\n")
                    visited[sn] = 1
                    if marker == 0:
                      sf = sn
                      marker = marker + 1
            else:
                array[sn] = 1

                c1 = Switch1.maclist1.count(endDevices[b].mac)
                c2 = Switch1.maclist2.count(endDevices[b].mac)
                if c1 == 0 and c2 == 0:
                    print("Mac Address of End Device", b, "not found in the MAC table")
                    print("Switch will broadcast the message\n")
                    print("Sending  packet -----", c[sn], "-----")
                    for j in range(1, 11):
                        if j != a:
                            endDevices[j].data = c[sn]
                            print("Message sent to End Device", j)
                        if j == b:
                            print("Ack received by End Device", b, "ACK NO :", sn%Seq_no)
                    print("\n")
                    if a < 6:
                        Switch1.maclist1[a - 1] = endDevices[a].mac
                    else:
                        Switch1.maclist2[a - 6] = endDevices[a].mac
                    if b < 6:
                        Switch1.maclist1[b - 1] = endDevices[b].mac
                    else:
                        Switch1.maclist2[b - 6] = endDevices[b].mac
                else:
                    if (a < 6 and b < 6):
                        print("Mac Address found, Both Devices in Hub 1")
                        print("Sending  packet -----", c[sn], "-----")
                        for j in range(1, 6):
                            if j != a:
                                endDevices[j].data = c[sn]
                                print("Message sent to End Device", j)
                            if j == b:
                                print("Ack received by End Device", b, "ACK NO :", sn%Seq_no)
                        print("\n")
                    elif a > 6 and b > 6:
                        print("Mac Address found, Both Devices in Hub 2")
                        print("Sending  packet -----", c[sn], "-----")
                        for j in range(6, 11):
                            if j != a:
                                endDevices[j].data = c[sn]
                                print("Message sent to End Device", j)
                            if j == b:
                                print("Ack received by End Device", b, "ACK NO :", sn%Seq_no)
                        print("\n")
                    else:
                        print("Mac Address of End Device", b, "found in the MAC table")
                        if sn != 0 and sn % 4 == 0:
                            print("time out occurred, Sending the", i, "th frame again. Sequence number :", sn%Seq_no)
                        print("Sending  packet -----", c[sn], "-----")
                        for j in range(1, 11):
                            if j != a:
                                endDevices[j].data = c[sn]
                                print("Message sent to End Device", j)
                            if j == b:
                                print("Ack received by End Device", b, "ACK NO :", sn % Seq_no)
                        print("\n")
                        if a > 5:
                           Switch1.maclist1[a - 6] = endDevices[a].mac
                        else:
                            Switch1.maclist1[a - 1] = endDevices[a].mac
                        if b > 5:
                            Switch1.maclist2[b - 6] = endDevices[b].mac
                        else:
                            Switch1.maclist2[b - 1] = endDevices[b].mac


                x = x - 1
                if sf == sn:
                   for i in range(sf, len(c)):
                       if array[i] == 0:
                           sf = i
                           sn = sf - 1
                           break
          sn = sn + 1
        if sn < len(c):
              print("Restart the timer, sending the outstanding packets again")
        sn = sf




def Selective_Repeat(a,b,c):

    print("Enter the reserved bit size for Seq no")
    m = int(input())
    sf = 0
    sn = 0
    x = len(c)
    Window_Size = 2**(m-1)
    Seq_no = 2**m
    array = [0]*x
    visited = [0]*x
    while x != 0:
        marker = 0
        while sn < sf + Window_Size and sn<len(c):
          if array[sn] == 0:
            if sn % 2 == 0 and visited[sn] == 0:
                    print(sn, "th packet lost, Sending next packet\n")
                    visited[sn] = 1
                    if marker == 0:
                      sf = sn
                      marker = marker + 1
            else:
                array[sn] = 1

                c1 = Switch1.maclist1.count(endDevices[b].mac)
                if c1 == 0:
                    print("Mac Address of End Device", b, "  not found in the MAC table")
                    print("Switch will Broadcast the message")
                    print("Sending  packet -----", c[sn], "-----")

                    for j in range(1, 6):
                        if j != a:
                            endDevices[j].data = c[sn]
                            print("Message sent to End Device", j)
                        if j == b:
                            print("Ack received by End Device", b, "ACK NO :", sn%Seq_no)
                    Switch1.maclist1[a - 1] = endDevices[a].mac
                    Switch1.maclist1[b - 1] = endDevices[b].mac

                else:
                           print("Mac Address of End Device", b, "found in the MAC table")
                           print("Sending  packet -----", c[sn], "-----")
                           if sn != 0 and sn % 4 == 0:
                               print("time out occurred, Sending the", sn, "th frame again.")
                           print("Message sent to End Device", b)
                           print("ACK received from End Device ", b)
                           print("\n")
                           Switch1.maclist1[a - 1] = endDevices[a].mac
                           Switch1.maclist1[b - 1] = endDevices[b].mac


                x = x - 1
                if sf == sn:
                   for i in range(sf, len(c)):
                       if array[i] == 0:
                           sf = i
                           sn = sf - 1
                           break
          sn = sn + 1
        if sn < len(c):
              print("Restart the timer, sending the outstanding packets again")
        sn = sf







""""----------------------------------------------------ACCESS CONTROL-----------------------------------------"""




end_Devices = [e1.seq_no, e2.seq_no, e3.seq_no, e4.seq_no, e5.seq_no, e6.seq_no, e7.seq_no, e8.seq_no, e9.seq_no, e10.seq_no]


def token_passing(token, num1):

    t = token
    s = num1
    if t == s:
        print("Sender has the access already!")
    elif t < s:
        print("End Device", t, "Has access ")
        print("------Passing the Token ")
        for i in end_Devices:
            #endDevices[i] = t
            print("End Device ", i+t, "Has access now")

            if s == i+t:
                print("----------------------------Access granted-----------------------------------")
                break
            if i != s:
                print("------Passing the Token ")
    else:
        print("End Device", t, "Has access ")
        print("------Passing the Token ")
        for i in endDevices:
            endDevices[i] = t
            print("End Device ", t-i, "Has access now")

            if s == t-i:
                print("----------------------------Access granted-----------------------------------")
                break
            if i != s:
                print("------Passing the Token ")





def collision_broadcast():
    if 1 == num4 or 2 == num4:
        print("Collision Domain : 1")
        print("Broadcast Domain : 1")
    elif 3 == num4 or 4 == num4:
        print("Collision Domain : 2")
        print("Broadcast Domain : 1")
    elif 5 == num4:
        print("Collision domain : 5")
        print("Broadcast Domain : 1")
    elif 6 == num4 :
        print("Collision Domain : 5")
        print("Broadcast Domain : 1")
    elif 7 == num4:
        print("Collision domain : 6")
        print("Broadcast Domain : 1")


"""-------------------------------------------------MENU---------------------------------------------------------"""

print("Following Simulations can be carried out. Enter the respective number of the simulation:")
print("1. Dedicated Link")
print("2. Simulation through Hub--------STAR TOPOLOGY------")
print("3. Simulation through Switch-----ADDRESS LEARNING---")
print("4. Complete Simulation --Implementing Access and Flow Control Protocols--")
print("5. Switch and 5 End Devices ")

num4 = int(input())



def Connections():

    if 1 == num4:

        print("Enter Sender Device no")
        num1 = int(input())
        print("Enter Receiver Device no")
        num2 = int(input())
        print("you have selected these two End Devices:", num1, "and", num2)
        if e1.port == e2.port:
           print("Enter the message to be transmitted")
           num3 = str(input())
           print("Message : ", num3)
           e1.data = num3
           print("Connection Made between two End devices")
           e1.port = 1
           e2.port = 2
           e2.data = e1.data
           print("Message sent successfully : ", num3)
           if e2.data == e1.data:
             print("                                                     ----ACK RECEIVED FROM END DEVICE", num2, "---")
           else:
             print("---ACK LOST---")

        else:
           print("No connection possible, already occupied")




    elif 2 == num4:

        print("Enter Sender Device no:")
        num1 = int(input())
        print("Enter Receiver Device no:")
        num2 = int(input())
        print("you have selected these two End Devices within same HUB:", num1, "and", num2)
        if End_Device_Vacant() == 0 and Hub1.Hub_vacant() == 0:
           print("Connection made between Sender-End device and HUB")
           e1.port = 1
           Hub1.port1 = 9
           if Hub1.port2 == 0 and Hub1.port3 == 0:
             print("Connection made between Hub and other End Devices")
             print("Enter the message")
             num3 = str(input())
             print("Message : ", num3)
             e1.data = num3
             e2.data = e1.data
             print("Message sent to End Device 2 successfully : ", e2.data)
             e3.data = e1.data
             print("Message sent to End Device 3 successfully : ", e3.data)
             e4.data = e1.data
             print("Message sent to End Device 4 successfully : ", e4.data)
             e5.data = e1.data
             print("Message sent to End Device 5 successfully : ", e5.data)
             e2.port = 7
             e3.port = 2
             e4.port = 5
             e5.port = 62
             Hub1.port2 = 5
             Hub1.port3 = 8
             Hub1.port4 = 4
             Hub1.port5 = 1
             if num2 == 2:
                 print("                                                     ---ACK RECEIVED  from End Device 2---")
             elif num2 == 3:
                 print("                                                     ---ACK RECEIVED  from End Device 3---")
             elif num2 == 4:
                 print("                                                     ---ACK RECEIVED  from End Device 4---")
             elif num2 == 5:
                 print("                                                     ---ACK RECEIVED  from End Device 5---")
             else:
                 print("ACK lost, no connection")
           else:
                 print("No Port vacant in HUB")
        else:
            print("---No port available in HUB---")





    elif 3 == num4:

        if Hub1.Hub_vacant() == 0 and Switch1.Switch_vacant() ==0 and Hub2.Hub_vacant() == 0:
            print("Connection made between --Hub1------Switch------Hub2-- ")
            Switch1.port1 = 2
            Hub1.port6 = 6
            Hub2.port6 = 4
            if End_Device_Vacant() == 0 and Hub1.Hub_vacant() == 0:
                print("......................HUB 1  CONNECTING.......................")

                print("Connection made between Hub1 and  End Device 1")
                e1.port = 1
                Hub1.port1 = 9
                if  Hub1.port2 == 0 and Hub1.port3 == 0 and Hub1.port4 == 0 and Hub1.port5 == 0:
                    print("Connection made between Hub1 and  End Device 2")
                    print("Connection made between Hub1 and  End Device 3")
                    print("Connection made between Hub1 and  End Device 4")
                    print("Connection made between Hub1 and  End Device 5")
                    e2.port = 7
                    e3.port = 2
                    e4.port = 8
                    e5.port = 1
                    Hub1.port2 = 5
                    Hub1.port3 = 8
                    Hub1.port4 = 52
                    Hub1.port5 = 80
                else:
                    print("No Port vacant in HUB")
            else:
                print("---No end device vacant---")


            if End_Device_Vacant() == 0 or Hub2.Hub_vacant() == 0:
                    print("......................HUB 2  CONNECTING.......................")
                    print("Connection made between Hub2 and  End Device 6")
                    e6.port = 1
                    Hub2.port1 = 9
                    if Hub2.port2 == 0 and Hub2.port3 == 0 and Hub2.port4 == 0 and Hub2.port5 == 0:
                        print("Connection made between Hub2 and  End Device 7")
                        print("Connection made between Hub2 and  End Device 8")
                        print("Connection made between Hub2 and  End Device 9")
                        print("Connection made between Hub2 and  End Device 10")
                        e7.port = 71
                        e8.port = 22
                        e9.port = 71
                        e10.port = 22
                        Hub2.port2 = 50
                        Hub2.port3 = 801
                        Hub2.port4 = 501
                        Hub2.port5 = 800
                    else:
                        print("No Port vacant in HUB")

            else:
                    print("---No end Device vacant---")

            print("Enter the message")
            num3 = str(input())
            print("Message : ", num3)
            e1.data = num3
            print(" Sender Device is 1" )
            print(" Receiver Device is 2")
            print("Searching for MAC address of End Device : 2 ")
            print("Mac Address of End Device 2 is =", e2.mac)
            for i in range(0,5):
                if Switch1.maclist1[i] == e2.mac:
                    print("MAC address found in MAC table within same port")
                    e2.data = e1.data
                    print("Message sent to End Device 2")
                    e3.data = e1.data
                    print("Message sent to End Device 3")
                    e4.data = e1.data
                    print("Message sent to End Device 4")
                    e5.data = e1.data
                    print("Message sent to End Device 5")

                    print("                                        ---ACK RECEIVED  from End Device 2---")
                    break
                if i == 4:
                    print("Mac Address of End Device 2 not found in the MAC table")
                    e2.data = e1.data
                    print("Message sent to End Device 2")
                    e3.data = e1.data
                    print("Message sent to End Device 3")
                    e4.data = e1.data
                    print("Message sent to End Device 4")
                    e5.data = e1.data
                    print("Message sent to End Device 5")
                    e6.data = e1.data
                    print("Message sent to End Device 6")
                    e7.data = e1.data
                    print("Message sent to End Device 7")
                    e8.data = e1.data
                    print("Message sent to End Device 8")
                    e9.data = e1.data
                    print("Message sent to End Device 9")
                    e10.data = e1.data
                    print("Message sent to End Device 10")

                    print("                                        ---ACK RECEIVED  from End Device 2---")

            Switch1.maclist1[0] = e1.mac
            Switch1.maclist1[1] = e2.mac

            print("Enter the message")
            num3 = str(input())
            print("Message : ", num3)
            e3.data = num3
            print(" Sender Device is 3")
            print(" Receiver Device is 2")
            print("Searching for MAC address of End Device : 2 ")
            print("Mac Address of End Device 2 is =", e2.mac)
            for i in range(0, 5):
                if Switch1.maclist1[i] == e2.mac:
                    print("MAC address found in MAC table within same port")
                    e2.data = e3.data
                    print("Message sent to End Device 1")
                    e1.data = e3.data
                    print("Message sent to End Device 2")
                    e4.data = e3.data
                    print("Message sent to End Device 4")
                    e5.data = e3.data
                    print("Message sent to End Device 5")

                    print("                                        ---ACK RECIEVED  from End Device 2---")
                    break
                if i == 4:
                    print("Mac Address of End Device 2 not found in the MAC table")
                    e2.data = e3.data
                    print("Message sent to End Device 1")
                    e1.data = e3.data
                    print("Message sent to End Device 3")
                    e4.data = e3.data
                    print("Message sent to End Device 4")
                    e5.data = e3.data
                    print("Message sent to End Device 5")
                    e6.data = e3.data
                    print("Message sent to End Device 6")
                    e7.data = e3.data
                    print("Message sent to End Device 7")
                    e8.data = e3.data
                    print("Message sent to End Device 8")
                    e9.data = e3.data
                    print("Message sent to End Device 9")
                    e10.data = e3.data
                    print("Message sent tp End Device 10")
                    print("                                        ---ACK RECIEVED  from End Device 2---")
            Switch1.maclist1[2] = e3.mac

            print("Enter the message")
            num3 = str(input())
            print("Message : ", num3)
            e1.data = num3
            print(" Sender Device is 1")
            print(" Receiver Device is 5")
            print("Searching for MAC address of End Device : 5 ")
            print("Mac Address of End Device 2 is =", e5.mac)
            for i in range(0, 5):
                if Switch1.maclist1[i] == e5.mac:
                    print("MAC address found in MAC table within same port")
                    e2.data = e1.data
                    print("Message sent to End Device 2")
                    e3.data = e1.data
                    print("Message sent to End Device 3")
                    e4.data = e1.data
                    print("Message sent to End Device 4")
                    e5.data = e1.data
                    print("Message sent to End Device 5")

                    print("                                            ---ACK RECEIVED  from End Device 5---")
                    break
                if i == 4:
                    print("Mac Address of End Device 5 not found in the MAC table")
                    e2.data = e1.data
                    print("Message sent to End Device 2")
                    e3.data = e1.data
                    print("Message sent to End Device 3")
                    e4.data = e1.data
                    print("Message sent to End Device 4")
                    e5.data = e1.data
                    print("Message sent to End Device 5")
                    e6.data = e1.data
                    print("Message sent to End Device 6")
                    e7.data = e1.data
                    print("Message sent to End Device 7")
                    e8.data = e1.data
                    print("Message sent to End Device 8")
                    e9.data = e1.data
                    print("Message sent to End Device 9")
                    e10.data = e1.data
                    print("Message sent to End Device 10")
                    print("                                           ---ACK RECEIVED  from End Device 5---")
            Switch1.maclist1[4] = e5.mac


            print("Enter the message")
            num3 = str(input())
            print("Message : ", num3)
            e1.data = num3
            print(" Sender Device is 1")
            print(" Receiver Device is 6")
            print("Searching for MAC address of End Device : 6 ")
            print("Mac Address of End Device 2 is =", e6.mac)
            for i in range(0, 5):
                if Switch1.maclist1[i] == e6.mac or Switch1.maclist2[i] == e6.mac:
                    print("MAC address found in MAC table in Different port")
                    e2.data = e1.data
                    print("Message sent to End Device 2")
                    e3.data = e1.data
                    print("Message sent to End Device 3")
                    e4.data = e1.data
                    print("Message sent to End Device 4")
                    e5.data = e1.data
                    print("Message sent to End Device 5")
                    e6.data = e1.data
                    print("Message sent to End Device 6")
                    e7.data = e1.data
                    print("Message sent to End Device 7")
                    e8.data = e1.data
                    print("Message sent to End Device 8")
                    e9.data = e1.data
                    print("Message sent to End Device 9")
                    e10.data = e1.data
                    print("Message sent to End Device 10")

                    print("                                       ---ACK RECEIVED  from End Device 6---")
                    break
                if i == 4:
                    print("Mac Address of End Device 6 not found in the MAC table")
                    e2.data = e1.data
                    print("Message sent to End Device 2")
                    e3.data = e1.data
                    print("Message sent to End Device 3")
                    e4.data = e1.data
                    print("Message sent to End Device 4")
                    e5.data = e1.data
                    print("Message sent to End Device 5")
                    e6.data = e1.data
                    print("Message sent to End Device 6")
                    e7.data = e1.data
                    print("Message sent to End Device 7")
                    e8.data = e1.data
                    print("Message sent to End Device 8")
                    e9.data = e1.data
                    print("Message sent to End Device 9")
                    e10.data = e1.data
                    print("Message sent to End Device 10")
                    print("                                          ---ACK RECEIVED  from End Device 6---")

            Switch1.maclist2[0] = e6.mac


            print("Enter the message")
            num3 = str(input())
            print("Message : ", num3)
            e8.data = num3
            print(" Sender Device is 8")
            print(" Receiver Device is 10")
            print("Searching for MAC address of End Device : 10 ")
            print("Mac Address of End Device 10 is =", e10.mac)
            for i in range(0, 5):
                if Switch1.maclist2[i] == e10.mac:
                    print("MAC address found in MAC table within same port")
                    e6.data = e8.data
                    print("Message sent to End Device 2")
                    e7.data = e8.data
                    print("Message sent to End Device 3")
                    e9.data = e8.data
                    print("Message sent to End Device 4")
                    e10.data = e8.data
                    print("Message sent to End Device 5")

                    print("                                          ---ACK RECEIVED  from End Device 10---")
                    break
                if i == 4:
                    print("Mac Address of End Device 2 not found in the MAC table")
                    e2.data = e8.data
                    print("Message sent to End Device 10")
                    e3.data = e8.data
                    print("Message sent to End Device 9")
                    e4.data = e8.data
                    print("Message sent to End Device 7")
                    e5.data = e8.data
                    print("Message sent to End Device 6")
                    e6.data = e8.data
                    print("Message sent to End Device 5")
                    e7.data = e8.data
                    print("Message sent to End Device 4")
                    e8.data = e8.data
                    print("Message sent to End Device 3")
                    e9.data = e8.data
                    print("Message sent to End Device 2")
                    e10.data = e8.data
                    print("Message sent to End Device 1")
                    print("                                          ---ACK RECEIVED  from End Device 10---")

            Switch1.maclist2[2] = e8.mac
            Switch1.maclist2[4] = e10.mac

            print("Enter the message")
            num3 = str(input())
            print("Message : ", num3)
            e10.data = num3
            print(" Sender Device is 10")
            print(" Receiver Device is 6")
            print("Searching for MAC address of End Device : 6 ")
            print("Mac Address of End Device 6 is =", e6.mac)
            for i in range(0, 5):
                if Switch1.maclist2[i] == e6.mac or Switch1.maclist1[i] == e6.mac :
                    print("MAC address found in MAC table within same port")
                    e6.data = e10.data
                    print("Message sent to End Device 2")
                    e7.data = e10.data
                    print("Message sent to End Device 3")
                    e8.data = e10.data
                    print("Message sent to End Device 4")
                    e9.data = e10.data
                    print("Message sent yo End Device 5")

                    print("                                               ---ACK RECEIVED  from End Device 6---")
                    break
                if i == 4:
                    print("Mac Address of End Device 6 not found in the MAC table")
                    e9.data = e10.data
                    print("Message sent to End Device 1")
                    e8.data = e10.data
                    print("Message sent to End Device 3")
                    e7.data = e10.data
                    print("Message sent to End Device 4")
                    e6.data = e10.data
                    print("Message sent to End Device 5")
                    e6.data = e10.data
                    print("Message sent to End Device 6")
                    e5.data = e10.data
                    print("Message sent to End Device 7")
                    e4.data = e10.data
                    print("Message sent to End Device 8")
                    e3.data = e10.data
                    print("Message sent to End Device 9")
                    e2.data = e10.data
                    print("Message sent to End Device 2")
                    print("                                           ---ACK RECEIVED  from End Device 6---")
            Switch1.maclist2[4] = e10.mac


            print("Mac Address Table of Port1")
            for i in range(0, 5):
                print("                                             END DEVICE ", i+1, "-", Switch1.maclist1[i])
            print("Mac Address Table of Port2")
            for i in range(0, 5):
                print("                                             END DEVICE ", i+6, "-", Switch1.maclist2[i])





    elif 4 == num4:
        if Hub1.Hub_vacant() == 0 and Switch1.Switch_vacant() ==0 and Hub2.Hub_vacant() == 0:
            print("Connection made between --Hub1------Switch------Hub2-- ")
            Switch1.port1 = 2
            Hub1.port6 = 6
            Hub2.port6 = 4
        if End_Device_Vacant() == 0 and Hub1.Hub_vacant() == 0:
            print("......................HUB 1  CONNECTING.......................")

            print("Connection made between Hub1 and  End Device 1")
            e1.port = 1
            Hub1.port1 = 9
            if Hub1.port2 == 0 and Hub1.port3 == 0 and Hub1.port4 == 0 and Hub1.port5 == 0:
                print("Connection made between Hub1 and  End Device 2")
                print("Connection made between Hub1 and  End Device 3")
                print("Connection made between Hub1 and  End Device 4")
                print("Connection made between Hub1 and  End Device 5")
                e2.port = 7
                e3.port = 2
                e4.port = 8
                e5.port = 1
                Hub1.port2 = 5
                Hub1.port3 = 8
                Hub1.port4 = 52
                Hub1.port5 = 80
            else:
                print("No Port vacant in HUB")
        else:
            print("---No end device vacant---")

        if End_Device_Vacant() == 0 or Hub2.Hub_vacant() == 0:
            print("......................HUB 2  CONNECTING.......................")
            print("Connection made between Hub2 and  End Device 6")
            e6.port = 1
            Hub2.port1 = 9
            if Hub2.port2 == 0 and Hub2.port3 == 0 and Hub2.port4 == 0 and Hub2.port5 == 0:
                print("Connection made between Hub2 and  End Device 7")
                print("Connection made between Hub2 and  End Device 8")
                print("Connection made between Hub2 and  End Device 9")
                print("Connection made between Hub2 and  End Device 10")
                e7.port = 71
                e8.port = 22
                e9.port = 71
                e10.port = 22
                Hub2.port2 = 50
                Hub2.port3 = 801
                Hub2.port4 = 501
                Hub2.port5 = 800
            else:
                print("No Port vacant in HUB")

        else:
            print("---No end Device vacant---")
        print("Enter token value")
        token = int(input())
        print("Enter Sender Device no")
        num1 = int(input())
        token_passing(token, num1)
        print("Enter receiver Device no")
        num2 = int(input())
        print("Enter message :")
        num3 = str(input())

        print("Choose the flow control protocol ")
        print("1.STOP AND WAIT ARQ")
        print("2.SELECTIVE REPEAT")
        num5 = int(input())
        if 1 == num5:
            stop_and_wait_arq_HUb(num1, num2, num3)
        else:
            Selective_Repeat_Hub(num1, num2, num3)




    elif 5 == num4:
        if Switch1.Switch_vacant() == 0 and  End_Device_Vacant() ==0:
           print("-----------CONNECTING TO SWITCH------------")
           for i in range(1, 6):
               print("End Device", i, " Connected to Switch" )
           print("Enter token value")
           token = int(input())
           print("Enter Sender Device no")
           num1 = int(input())
           token_passing(token, num1)
           print("Enter receiver Device no")
           num2 = int(input())
           print("Enter message :")
           num3 = str(input())
        if num2 != num1:
           print("Choose the flow control protocol ")
           print("1.STOP AND WAIT ARQ")
           print("2.SELECTIVE REPEAT ")
           num5 = int(input())
           if 1 == num5:
               stop_and_wait_arq(num1, num2, num3)
           else:
               Selective_Repeat(num1, num2, num3)
        else:
            print(" Enter valid number. No communication possible!")

              

Connections()

