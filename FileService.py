import csv

class FileService(object):

    fileNameWithExt = None
    fileWriteMode = None
    fileColumns = None
    data = None 

    def __init__(self, fileNameWithExt):
        pass
        self.fileNameWithExt = fileNameWithExt

    def write(self):
        # open the file in the write mode
        f = open(self.fileNameWithExt, 'w+')
        # create the csv wri ter
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(self.fileColumns)
        writer.writerow(self.data)
        # close the file
        f.close()

    def setColumns(self, columns):
        data = []
        
        for item in range(columns):
            data.append(f"r{item + 1}")

        self.fileColumns = data

    def setData(self, row):
        self.data = row