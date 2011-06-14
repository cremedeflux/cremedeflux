from cStringIO import StringIO
from textwrap import dedent
from cdf.settings import SettingsFile
from cdf.tests.plugins.hourly import HourlyPlugin


def settings_file(contents):
    return SettingsFile(fp=StringIO(dedent(contents)))


def test_empty_file():
    settings = settings_file('')
    assert len(settings.publishers) == 0


def test_publishers_names_titles():
    settings = settings_file("""\
    [publisher:public]
    title = Public stream

    [publisher:private]
    title = Private stream
    
    [publisher:untitled]

    [publisher:]
    # Unnamed publishers are skipped

    [nonpublisher:foo]
    bar = baz

    [nonpublisher2]
    """)
    assert len(settings.publishers) == 3
    assert set(settings.publishers.keys()) == {
        'private',
        'public',
        'untitled',
    }
    assert settings.publishers['private'].title == 'Private stream'
    assert settings.publishers['public'].title == 'Public stream'
    # Untitled publishers inherit name as title
    assert settings.publishers['untitled'].title == 'untitled'


def test_collectors_names_titles_plugins():
    settings = settings_file("""\
    [collector:hourly]
    plugin = test_hourly

    [collector:hourly2]
    title = every other hourly
    plugin = test_hourly
    every = 2

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
    # Untitled collectors inherit name as title
    assert settings.collectors['hourly2'].title == 'every other hourly'
    assert isinstance(settings.collectors['hourly'].plugin, HourlyPlugin)
    assert isinstance(settings.collectors['hourly2'].plugin, HourlyPlugin)
    assert settings.collectors['hourly'].plugin.every == 1
    assert settings.collectors['hourly2'].plugin.every == 2
    