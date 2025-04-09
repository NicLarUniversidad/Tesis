

class BasicFileReader(object):

    def __init__(self, path_to_dataset):
        f = open(path_to_dataset)
        self.promtps = f.readlines()
        f.close()