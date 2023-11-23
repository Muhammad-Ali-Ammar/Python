"""


 ########################### to send Integer Number #######################################3

            ## To Send Integer
            data_to_send = struct.pack('!B', 123)
            ser.write(data_to_send)


 ########################### to send ascii, char #######################################3

            char_number = ord('1')
            # Send the ASCII value as a single byte
            ser.write(([char_number]))


            char_number = ord('a')
            # Send the ASCII value as a single byte
            ser.write(([char_number]))


########################### to send String #######################################3

            string_to_send = "Ammar\0" #receives A M M A R + \0

            # Encode the string and send it
            ser.write(string_to_send.encode('utf-8'))
            

"""


import serial
import glob
import struct
import time
import threading
import sys


####################################################### SET UP #############################################################################
def Get_SerialPort():
    Loc_PortsList = glob.glob('/dev/ttyUSB*')
    return Loc_PortsList[0] if Loc_PortsList else None

# Find the serial port
Global_SerialPort = Get_SerialPort()

if Global_SerialPort is None:
    print("No suitable serial port found.")
    sys.exit()


## Serial Configuration 

print(f"Serial port found: {Global_SerialPort}")
Global_BaudRate = 115200
ser = serial.Serial(Global_SerialPort, Global_BaudRate, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS, timeout=1)
ser.flush()
print(f"Serial communication established on {Global_SerialPort} at {Global_BaudRate} baud")


##################################################### ISR #####################################################################################


## Rx Isr For Strings 

def Rx_ISR(Copy_SerialPort):
    Loc_StringBuffer = ""  # Buffer to accumulate characters

    while True:
        Loc_ReceivedChar = Copy_SerialPort.read(1).decode('utf-8')  # Read one character

        if Loc_ReceivedChar == '\0':
            # Process the accumulated characters
            if Loc_StringBuffer == "Ammar":
                print("Tmaam Ammar")
            elif Loc_StringBuffer == "1":
                print("Tmaam 1")
            else:
                print(f"Received unexpected data: {Loc_StringBuffer}.")

            # Clear the buffer after processing the data
            Loc_StringBuffer = ""
        else:
            # Accumulate characters until a null character is encountered
            Loc_StringBuffer += Loc_ReceivedChar








# Start a separate thread for receiving data
RxIsr_Thread = threading.Thread(target=Rx_ISR, args=(ser,), daemon=True)
RxIsr_Thread.start()

################################################################################################################################################


# Main program continues to execute other tasks
while True:
     """
     your main code here !! 
     """
     
     string_to_send = "Ammar\0" #receive Ammar + '\0'
     ser.write(string_to_send.encode('utf-8'))
     time.sleep(1)


        

# Close the serial port when the program exits
ser.close()


