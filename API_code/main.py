# Ella Greetis - EGR314 - API for STEMteresting project 
# (bidirectional internet comm. subsystem)

# pseudo code: 
# import modules from uart echo lab: 
from machine import UART
from machine import Pin
import time

# import array 
# import array as array <-- not necessary, use bytearray
# create character array: 
message = bytearray() 

baudRate = 9600 
ledPin = 23
CONST_messageLen = 64 # length of a message in bytes

# initialize a new UART class: 
uart = UART(0, baudRate, tx=1, rx=3)
# run the init method with more details: baudrate and parity
uart.init(baudRate, bits = 8, parity = None, stop = 1)
# initialize LED pin as an output
led = Pin(ledPin, Pin.OUT)

# MESSAGE RECEIVER: 
# when message received -> trigger interrupt handler which handles the message?

# void interrupt handler: 
# receive entire message (store in char array?)
# parse message for prefix, suffix, then sender and receiver designators (separate function?)
# if message is over 64 bytes -> trash
# if message written by me -> trash
# if message is one of the messages supposed to be passed by me 
# --> pass it along
# if message is supposed to be received by me
# --> test for coherence
# if message is not one of the messages supposed to be sent or passed by me -> trash

# void(?) parse: 
def parse(mssg):
    for i in mssg: 
        # define meat array
        messageMeat = bytearray()

        # break out if message too long 
        timeout = False
        if i > CONST_messageLen: 
            timeout = True
            raise Exception("ERROR: message timeout occurred")
        
        # look for prefix
        prefix = False
        if i == 0: 
            if mssg[i] == b'\x01' or b'\x02' or b'\x03' or b'\x04' or b'\x05' or b'\x06': 
                prefix = True
            else: 
                raise Exception("ERROR: prefix not valid")
            
        # put meat of message into messageMeat array: 
        if 3 < i < 62: 
            messageMeat += mssg[i]

        # look for suffix
        suffix = False
        sufBit1 = False
        if i == 62: 
            if mssg[i] == b'\x6e': 
                sufBit1 = True
        elif i == 63: 
            if mssg[i] == b'\x64':
                sufBit2 = True
        if sufBit1 and sufBit2: 
            suffix = True
        else: 
            raise Exception("ERROR: suffix not valid")
        
    if prefix and suffix and len(messageMeat) == 59: 
        print("Parsing Successful")
        print("message meat: %s", messageMeat) # this line NOT confirmed working -- find correct type designator
        return messageMeat
            

def IDchecker(byte1, byte2): 
    if byte1 == b'\x47': 
        person = "Greetis" 
    elif byte1 == b'\x48': 
        person = "Heafey" 
    elif byte1 == b'\x42': 
        person = "Bohart" 
    elif byte1 == b'\x53': 
        person = "Smith"
    elif byte1 == b'\x41' and byte2 == b'\x5a': # AZ
        person == "Test Prefix"
    elif byte1 == b'\x59' and byte2 == b'\x42': # YB
        person =="Test Suffix"
    else: 
        trash()
        raise Exception("ERROR: sender/receiver ID not read")
    print(person)
    return person

def TypeChecker(byte):
    if byte == b'\x01': 
        mssgType = "Desired Speed"
        mssgNum = 1
    elif byte == b'\x02': 
        mssgType = "user safe?" 
        mssgNum = 2
    elif byte == b'\x03': 
        mssgType = "motor on?"
        mssgNum = 3
    elif byte == b'\x04': 
        mssgType = "motor off?"
        mssgNum = 4
    elif byte == b'\x05': 
        mssgType = "direct drive"
        mssgNum = 5
    elif byte == b'\x06': 
        mssgType = "motor speed"
        mssgNum = 6
    else:
        trash()
        raise Exception("message type designator not found")
    print(mssgType)
    return mssgNum

# function to pass message: 
def passMessage(mssg): 
    for i in range(0, len(mssg)): 
        uart.write(mssg[i])
    while uart.txdone() == False: 
        pass
    return

# function to handle message for me:
def handleMessage(): 
    # a bunch of wifi stuff goes here
    return

# function to trash message: 
def trash():
    print("Trashing message...")
    message.clear()
    print("Message Trashed.")
    return

# main function
def main(): 
    # startup code would go here
    print("main function starting")
    # loop goes here:
    while True: 
        receiving = False; 
        c = uart.read(1)
        if c is not None: 
            message.append(c)
            receiving = True
        while receiving == True: 
            i = 0
            while i < CONST_messageLen: 
                char = uart.read(1)
                message.append(char)
                i += 1
            receiving = False
        c = None
        # message has now been put into message array

        # now, parse the message
        meat = parse(message)
        mssgNum = TypeChecker(meat[0])
        mssgSender = IDchecker(meat[1])
        mssgReceiver = IDchecker(meat[2])

main()