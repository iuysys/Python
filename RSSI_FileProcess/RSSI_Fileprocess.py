Str_Left = 'LEFT_NODE:'
Str_Right = 'RIGHT_NODE:'
Str_Master = 'MASTER_NODE:'
Str_Rear = 'REAR_NODE:'

FileDirector = "F:\PythonProject\RSSI_FileProcess\\"            # 更改为用户选择路径
FileNameTemp = 'data01.TXT'


def HexList2DecList(HexList):
    HexListSplit = HexList.strip().split()
    DecList = list()

    for HexStr in HexListSplit:
        DecList.append(bytes.fromhex(HexStr))

    return DecList


RssiFile = open(FileDirector + FileNameTemp)
OutPutFile = open(FileDirector + "OutPutFile.txt", 'w')
LineBuff = list()

for line in RssiFile:
    if line.find(Str_Left) >= 0:
        print(line)
        LineBuff.append(line)
    elif line.find(Str_Right) >= 0:
        print(line)
        LineBuff.append(line)
    elif line.find(Str_Master) >= 0:
        print(line)
        LineBuff.append(line)
    elif line.find(Str_Rear) >= 0:
        print(line)
        LineBuff.append(line)
OutPutFile.writelines(LineBuff)
