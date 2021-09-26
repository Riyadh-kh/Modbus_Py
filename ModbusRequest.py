import serial
from CRCCalculator import CRCBuffer
from AddressMapping import getLowerByte, getHigherByte

def getRequest():
    with serial.Serial('/dev/ttyUSB1', 9600, parity=serial.PARITY_NONE, bytesize=8, stopbits=1) as ser:
        while(True):
            try: 
                loraQuery=ser.read(8) # Read the query coming from Lora 8 bytes
                loraQueryList=list(loraQuery)

                # Obtain CRC from the received Query
                CRC=CRCBuffer(loraQueryList[0:6]) 

                # Check if CRC matches (bytes are 7 and 8)
                if (loraQueryList[6:8]==CRC[6:8]):
                    
                    ## Obtain slaveID
                    slaveID= loraQueryList[0]

                    if (slaveID == 8):

                        length=loraQueryList[4]+ loraQueryList[5] # GeT the number of registers requried to read
                        address= loraQueryList[2] + loraQueryList[3] # Get the register Address
                        # Final format should be: [SlaveID, Functioncode, Datasize, :Data, CRC]
                        arrayToTransmit=[slaveID, 3, length*2]

                        for i in range(1, length+1):
                            # Map the ID into the original address and append it to a list
                            arrayToTransmit.append(getHigherByte(i+address)) 
                            arrayToTransmit.append(getLowerByte(i+address))
                        print(arrayToTransmit)
                        arrayToTransmit= CRCBuffer(arrayToTransmit) # Determine and add CRC to the list
                        print(arrayToTransmit)

                        print(bytearray(arrayToTransmit))
                        ser.write(bytearray(arrayToTransmit)) # Write the list in a bytearray format

                        arrayToTransmit.clear()
                else:
                    print("CRC has been indentified to be incorrect")
            except KeyboardInterrupt:
                ser.close()
                break