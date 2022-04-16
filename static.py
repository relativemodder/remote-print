class Static:
    def __init__(self):
        pass
    def load(resource, isblob=False):
        mode = "r"
        if isblob:
            mode = "rb"
        f = open("static/"+resource, mode)
        content = f.read()
        f.close()
        return content
        
