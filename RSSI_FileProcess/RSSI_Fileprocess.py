# ================================================================
# -- Import
# ================================================================
from matplotlib import pyplot as plt
import re
import win32ui

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
LineBuff = []


# ================================================================
# --
# ================================================================
def HexList2DecList(HexList):
    HexListSplit = HexList.strip().split()
    DecList = []

    for HexStr in HexListSplit:
        DecList.append(int(HexStr, 16) - 256)

    return DecList


# ================================================================
# -- 去除字符串控制字
# ================================================================
def ClearControlChar(s):
    temp = re.sub('[\x00-\x09|\x0b-\x0c|\x0e-\x1f]', '', s)
    return temp


# ================================================================
# --
# -- 当Flash不存在手机信息,flash值0xff会被当做控制字打印在文本中,造成文本
#       处理出错,此处需要做异常处理
#       使用sub正则表达式去除
# ================================================================
def ReadPhoneInfo(fileBuff):
    info = []
    Str_Brand = "PhoneBrand is"
    Str_Model = "PhoneModel is"
    for InfoLine in fileBuff:
        if InfoLine.find(Str_Brand) >= 0:
            info.append(InfoLine[len(Str_Brand) + 1:])  # 默认数据打印完全
        elif InfoLine.find(Str_Model) >= 0:
            info.append(InfoLine[len(Str_Model) + 1:])
    return info


test = win32ui.CreateFileDialog(1)
test.DoModal()
InfoFilePath = test.GetPathName()

with open(InfoFilePath) as InfoFile:
    with open("PhoneInfoOutFile.txt", 'w') as InfoFileOut:
        InfoFileOut.writelines(ReadPhoneInfo(InfoFile))

with open(FileDirector + FileNameTemp) as RssiFile:
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

with open(FileDirector + "OutPutFile.txt", 'w') as OutPutFile:
    OutPutFile.writelines(LineBuff)

xx = range(0, len(LeftRawBuff))
plt.plot(xx, LeftRawBuff)
plt.gca().invert_yaxis()
plt.show()
