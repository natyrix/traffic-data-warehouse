

class PreProcessPipeline():
    def __init__(self) -> None:
        pass

    def load_file(self, path="../data/raw_dataset.csv"):
        # with open(path, 'r')as f:
        self.reader = open(path, 'r')
    
    def add_extra_cols(self):
        max_num = 0
        line = self.reader.readline()
        while line:
            l = str(line).split(';')
            l = l[9:]
            if len(l) > 0:
                if len(l) / 6 > max_num:
                    max_num = len(l) / 6

            line = self.reader.readline()
        self.max_num = max_num
        print(f"MAX NUM: {max_num}")


pipeline = PreProcessPipeline()

pipeline.load_file('./data/raw_dataset.csv')
pipeline.add_extra_cols()