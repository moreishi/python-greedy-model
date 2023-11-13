import csv

class Normalize:

    filePath = None
    filePathSave = None
    data = None
    nomalized = []

    def __init__(self) -> None:
        pass

    def setFilePath(self, path):
        self.filePath = path

    def setFilePathSave(self, path):
        self.filePathSave = path

    def run(self):
        self.setFilePath(self.filePath)
        self.setData()
        self.process()

    def setData(self):
        with open(self.filePath, 'r') as csvfile:
            self.data = list(csv.reader(csvfile))[0]
    
    def process(self):
        
        data = self.data.copy()
        normalized = []
        
        for idx, item in enumerate(data):
            next = data[idx: idx + 25]
            if len(next) == 25:
                normalized.append(next)
        
        self.saveToFile(normalized)

    def saveToFile(self, data):
        for item in data:
            self.write_csv(item)
        
    def write_csv(self, data):

        # open the file in the write mode
        f = open(self.filePathSave, 'a+')
        # create the csv wri ter
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(data)
        # close the file
        f.close()

normalize = Normalize()
normalize.setFilePath('result/37.csv')
normalize.setFilePathSave('result/greedy.csv')
normalize.run()
