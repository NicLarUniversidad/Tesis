

class BasicFileReader(object):

    def __init__(self, path_to_dataset):
        f = open(path_to_dataset)
        lines = f.readlines()
        data = []
        for line in lines:
            if len(line) > 0:
                data.append(line)
        self.data = data
        f.close()