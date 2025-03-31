string = "YB"
hex_representation = ''.join(hex(ord(char)) for char in string)
print(hex_representation)
print(b'\x47')

#import array as array
messageMeat = bytearray()

message = bytearray('\x55' + '\x02' + "Hello World", "utf-8")


for i in range(3, len(message)): 
    messageMeat.append(message[i])


print("message meat: ", bytes(messageMeat).decode())