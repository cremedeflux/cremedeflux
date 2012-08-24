from pkg_resources import iter_entry_points


class Collector(object):

    def __init__(self, name, configitems):
        self.name = name
        self_config = {}
        plugin_configitems = []
        for key, value in configitems:
            if key in ('title', 'plugin'):
                self_config[key] = value
            else:
                plugin_configitems.append((key, value))
        self.title = self_config.get('title', name)
        # Load the plugin, or mark ourselves as invalid.
        plugin_name = self_config.get('plugin')
        if plugin_name:
            PluginClass = None
            for entrypoint in iter_entry_points('cremedeflux_plugins', plugin_name):
                PluginClass = entrypoint.load()
            if PluginClass:
                self.plugin = PluginClass(self, plugin_configitems)
            else:
                self.plugin = None
        else:
            self.plugin = None


class CollectorPlugin(object):

    def __init__(self, collector, configitems):
        self.pre_init()
        for key, value in configitems:
            getter = getattr(self, 'init_' + key, None)
            if callable(getter):
                getter(value)
        self.post_init()

    def pre_init(self):
        pass

    def post_init(self):
        pass
