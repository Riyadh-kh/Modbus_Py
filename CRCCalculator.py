
def CalCRC16(data, length):
    #print(data, length) #Print data, length
    crc=0xFFFF
    if length == 0:
       length = 1
    j = 0
    while length != 0:
        crc ^= list.__getitem__(data, j)
        #print('j=0x%02x, length=0x%02x, crc=0x%04x' %(j,length,crc))
        for i in range(0,8):
            if crc & 1:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
        length -= 1
        j += 1
    return crc
# ===============================================================
def CRCBuffer(buffer):     
    crc_transformation = CalCRC16(buffer,len(buffer))    
    #crc_calculation = hex(crc_transformation)
    #print('crc_calculation:',crc_calculation)
    tasd = [0x00,0x00]
    tasd[0] = crc_transformation & 0xFF
    tasd[1] = (crc_transformation >> 8) & 0xFF
    H =hex(tasd[0])
    L =hex(tasd[1])
    H_value = int(H,16)
    L_value = int(L,16)
    buffer.append(H_value)
    buffer.append(L_value)
    return buffer
