# ================================================================
# -- Import
# ================================================================
from matplotlib import pyplot as plt


# ================================================================
# -- Const
# ================================================================
Str_Left = 'LEFT_NODE:'
Str_Right = 'RIGHT_NODE:'
Str_Master = 'MASTER_NODE:'
Str_Rear = 'REAR_NODE:'
# ================================================================
# -- Variable
# ================================================================
FileDirector = "F:\PythonProject\RSSI_FileProcess\\"  # 更改为用户选择路径
FileNameTemp = 'data01.TXT'

LeftRawBuff = []



def HexList2DecList(HexList):
    HexListSplit = HexList.strip().split()
    DecList = []

    for HexStr in HexListSplit:
        DecList.append(int(HexStr, 16) - 256)

    return DecList


RssiFile = open(FileDirector + FileNameTemp)
OutPutFile = open(FileDirector + "OutPutFile.txt", 'w')
LineBuff = []

for line in RssiFile:
    if line.find(Str_Left) >= 0:
        print(line)
        LeftRawBuff += HexList2DecList(line[len(Str_Left):])
        LineBuff.append(line)
    elif line.find(Str_Right) >= 0:
        print(line)
        print(HexList2DecList(line[len(Str_Right):]))
        LineBuff.append(line)
    elif line.find(Str_Master) >= 0:
        print(line)
        print(HexList2DecList(line[len(Str_Master):]))
        LineBuff.append(line)
    elif line.find(Str_Rear) >= 0:
        print(line)
        print(HexList2DecList(line[len(Str_Rear):]))
        LineBuff.append(line)

OutPutFile.writelines(LineBuff)

xx = range(0, len(LeftRawBuff))
plt.plot(xx,LeftRawBuff)
plt.gca().invert_yaxis()
plt.show()