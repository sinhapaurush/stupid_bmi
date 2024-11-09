import csv
    
    
class Storage:
        _filename = "data.csv"
        def __init__(self):
            self._fh = open(self._filename, "a+")
            
        def __del__(self):
            self._fh.close()
            
        def readFile(self):
            self._fh.seek(0)
            csvRecs = csv.reader(self._fh)
            row = []
            for i in csvRecs:
                row.append(i)
            return row
        def appendRecord(self, record):
            self._fh.seek(0, 2)
            csvW = csv.writer(self._fh)
            csvW.writerow(record)
        