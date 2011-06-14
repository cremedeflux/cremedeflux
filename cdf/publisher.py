class Publisher(object):

    def __init__(self, name, configitems):
        self.name = name
        configitems = dict(configitems)
        self.title = configitems.pop('title', name)
