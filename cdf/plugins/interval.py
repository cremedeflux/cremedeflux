from cdf.collector import CollectorPlugin


class IntervalPlugin(CollectorPlugin):

    seconds = None

    message = 'Default message'

    def init_seconds(self, value):
        self.seconds = int(value)

    def init_message(self, value):
        self.message = unicode(value)
