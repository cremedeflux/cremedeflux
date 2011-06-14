class Publisher(object):

    def __init__(self, name, configitems):
        self.name = name
        configitems = dict(configitems)
        if 'title' in configitems:
            self.title = configitems['title']
        else:
            self.title = name
