info={"Original Address": [16386, 16387, 16388, 16389, 16390, 16391, 16394, 16395, 16396, 16397, 16398, 16399, \
16402, 16403, 16404, 16405, 16406, 16407, \
16412, 16413, 16414, 16415, 16416, 16417, 16418, 16419, \
16426, 16427, \
16434, 16435, \
16456, 16457, \
16460, 16461, \
16472, 16473, \
16384, 16385, \
16442, 16443, 16444, 16445, 16446, 16447, \
16477, 16481, 16514, 16548, 16582, 16616, 16649, 16682], \
"ID Address": [1, 2, 3, 4, 5, 6, 7, 8, \
9, 10, 11, 12, 13, 14, \
15, 16, 17, 18, 19, 20, \
21, 22, 23, 24, 25, 26, 27, 28, \
29, 30, \
31, 32, \
33, 34, 35, 36, 37, 38, \
39, 40, \
41, 42, \
43, 44, \
45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], \
"Higher Byte": [8, 1, 1, 1, 1, 1, 1, 1, \
1, 1, 1, 1, 1, 1, \
1, 1, 1, 1, 1, 1, \
1, 1, 1, 1, 1, 1, 1, 1, \
1, 1, \
1, 1, \
1, 1, 1, 1, 1, 1, \
1, 1, \
1, 1, \
1, 1, \
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
"Lower Byte": [8, 1, 1, 1, 1, 1, 1, 1, \
1, 1, 1, 1, 1, 1, \
1, 1, 1, 1, 1, 1, \
1, 1, 1, 1, 1, 1, 1, 1, \
1, 1, \
1, 1, \
1, 1, 1, 1, 1, 1, \
1, 1, \
1, 1, \
1, 1, \
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] }


def getIDAddress(originalAddress):
    return info["ID Address"][info["Original Address"].index(originalAddress)]

def getOriginalAddress(idAddress):
    return info["Original Address"][info["ID Address"].index(idAddress)]

def getLowerByte(idAddress):
    return info["Lower Byte"][info["ID Address"].index(idAddress)]

def getHigherByte(idAddress):
    return info["Higher Byte"][info["ID Address"].index(idAddress)]

def getDataLength():
    return len(info["Original Address"])

def setHigherByte(value, index):
    info["Higher Byte"][index]= value

def setLowerByte(value, index):
    info["Lower Byte"][index]= value
