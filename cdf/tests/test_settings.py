from cStringIO import StringIO
from textwrap import dedent

from cdf.settings import SettingsFile
from cdf.plugins.interval import IntervalPlugin


def settings_file(contents):
    return SettingsFile(fp=StringIO(dedent(contents)))


def test_empty_file():
    settings = settings_file('')
    assert len(settings.collectors) == 0


def test_collectors_names_titles_plugins():
    settings = settings_file("""\
    [collector:hourly]
    # title is implicit from collector name
    plugin = interval
    seconds = 3600

    [collector:hourly2]
    title = every other hourly
    plugin = interval
    seconds = 7200

    [collector:noplugin]
    # Collectors without plugins are skipped

    [collector:invalidplugin]
    # Collectors with unloadable plugin names are skipped
    plugin = nonexistent

    [collector:]
    # Unnamed collectors are skipped

    [noncollector:foo]

    [noncollector2]
    """)
    assert len(settings.collectors) == 2
    assert set(settings.collectors.keys()) == {
        'hourly',
        'hourly2',
    }
    assert settings.collectors['hourly'].title == 'hourly'
    assert settings.collectors['hourly2'].title == 'every other hourly'
    assert isinstance(settings.collectors['hourly'].plugin, IntervalPlugin)
    assert isinstance(settings.collectors['hourly2'].plugin, IntervalPlugin)
    assert settings.collectors['hourly'].plugin.seconds == 3600
    assert settings.collectors['hourly2'].plugin.seconds == 7200
