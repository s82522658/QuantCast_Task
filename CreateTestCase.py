import csv, os
from io import open
DATA = [
    ['', ''],
    ['ajslkdjfijf', '2019-07-12Tdasd']
]

def Main(OutputFileName):
    output = os.path.join(os.path.dirname(__file__), OutputFileName)
    WriteIntoCsv(DATA, output)

def WriteIntoCsv(data, output):
    with open(output, 'wb') as o:
        header = ['cookie', 'timestamp']
        csv.writer(o).writerow(header)

    with open(output, 'ab') as o:
        writer = csv.writer(o)
        for i in data:
            cookie = i[0]
            timestamp = i[1]
            writer.writerow([cookie, timestamp])
