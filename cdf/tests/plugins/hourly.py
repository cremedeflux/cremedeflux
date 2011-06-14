from cdf.collector import CollectorPlugin


class HourlyPlugin(CollectorPlugin):

    every = 1

    def init_every(self, value):
        self.every = int(value)
