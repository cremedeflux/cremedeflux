from cStringIO import StringIO
from textwrap import dedent
from cdf.settings import SettingsFile


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
