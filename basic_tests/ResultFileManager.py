import os


class ResultFileManager:

    def __init__(self, path):
        self.path = path

    def try_init(self):
        if not os.path.exists(self.path):
            f = open(self.path, "w")
            header = "ID\tcode_original\tnl\tresponse\tcode\tBLEU\tCODE_BLEU\tEM\tparse_success\tprocessed\tmodel_id\ttechnique\n"
            f.write(header)
            f.close()

    def add(self, new_line):
        new_line = new_line.encode("cp1252", errors="replace").decode("cp1252")
        f = open(self.path, "a")
        f.write(f"{new_line}\n")
        f.close()