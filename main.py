import csv, os, sys
import CreateTestCase

INPUT_FORMAT = "yyyy-mm-dd"
STDIN_ARG_LEN = 4
STDIN_POS_CSVFILE = 1
STDIN_POS_DATE = 2
STDIN_POS_DATEARG = 3
NUM_COLUMN = 2
COL_COOKIE = 0
COL_TIMESTAMP = 1

# Read and Organize CSV file into LogData
def ReadFile(Filename): # IN:str  OUT: dict
    LogData = {}
    with open(os.path.join(os.path.dirname(__file__), Filename), 'r') as f:
        Data = csv.reader(f, delimiter=',')
        dMap, lActive, iTimes, time = {}, [], 0, ''
        for index, row in enumerate(Data):
            if (index == 0) or (len(row) != NUM_COLUMN):
                continue
            cookie = row[COL_COOKIE]
            temp = TransformTime(row[COL_TIMESTAMP])
            if temp != time:
                LogData[time] = lActive
                dMap, lActive, iTimes, time = {}, [], 0, temp
            if cookie not in dMap:
                dMap[cookie] = 0
            dMap[cookie] = dMap[cookie]+1
            if dMap[cookie] == iTimes:
                lActive.append(cookie)
            elif dMap[cookie] > iTimes:
                lActive = [cookie]
                iTimes = dMap[cookie]

        LogData[time] = lActive
    return LogData

# Transform Datetime into Date
def TransformTime(Time): # IN:str  OUT: str
    # Assume all datetimes in csv are UTC time zone,
    # and assume the datetimes are all strings in csv file
    return Time[:len(INPUT_FORMAT)]

def GetActiveCookie(GivenDate, Data): # IN:str  OUT: []
    return Data[GivenDate] if GivenDate in Data else []

def Main():
    Syslen = len(sys.argv)
    Sysin = sys.argv
    if Syslen < STDIN_ARG_LEN:
        print "Invalid Arguments Len"
        return
    if Sysin[STDIN_POS_DATE] != '-d':
        print "Invalid opt Arguments in Stdin"
        return
    LogData = ReadFile(Sysin[STDIN_POS_CSVFILE])
    for i in GetActiveCookie(Sysin[STDIN_POS_DATEARG], LogData):
        print i

if __name__ == '__main__':
    CreateTestCase.Main(OutputFileName = 'cookie_log.csv')
    Main()


