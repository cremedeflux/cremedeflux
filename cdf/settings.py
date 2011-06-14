from ConfigParser import ConfigParser
from cdf.collector import Collector
from cdf.publisher import Publisher


class SettingsFile(object):

    def __init__(self, filename=None, fp=None):
        cp = self.cp = ConfigParser()
        if filename is not None and fp is None:
            cp.read([filename])
        elif fp is not None:
            cp.readfp(fp, filename)
        else:
            raise ValueError('Must specificy filename or fp.')
        self._parse_cp()

    def _parse_cp(self):
        # First create publishers
        self.collectors = {}
        self.publishers = {}
        for section in self.cp.sections():
            try:
                type, name = section.split(':', 1)
            except ValueError:
                continue
            if name == '':
                continue
            elif type == 'collector':
                collector = Collector(name, self.cp.items(section))
                if collector.plugin is not None:
                    self.collectors[name] = collector
            elif type == 'publisher':
                publisher = Publisher(name, self.cp.items(section))
                self.publishers[name] = publisher
            else:
                continue
