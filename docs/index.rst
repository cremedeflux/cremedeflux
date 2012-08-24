Welcome to Crème de Flux's documentation!
=========================================

Contents:

.. toctree::
   :maxdepth: 2


Introduction
============

..  note::

    This is a lot of "what is to be".

Crème de Flux (or "CDF")
aims to provide an automated journal
based on your lifestream,
and to publish separate editions
for each part of your life.

Here are some things CDF may do to accomplish this goal:

- Aggregate lifestream sources using agents called "collectors":

  Collectors listen for changes in data sources,
  and transforms them into "event" data
  suitable for your stream.

  Examples include:

  - Code repository commits
  - Issue tracker submissions
  - Invoice timer start/stop events
  - Skype chats
  - Web browser history
  - Email sent
  - Tweets / Facebook posts
  - Weather conditions
  - Screenshots
  - Evernote notes
  - Audio notes

- Serve you a live view of your complete stream:

  As events enter the stream,
  your web browser will display them.

  Each collector gives its events a "type"
  which is used to select templates and CSS styles
  when rendering each event.

- Allow annotation of your stream in the live view:

  - Comment at any point in the stream.
  - Comment about any event in the stream.
  - Start/stop ad hoc events.

- Provide tools for publishing separate editions:

  You'll always have a "personal" edition,
  which by default will contain your entire stream.

  Easily mark individual events as personal-only,
  which will prevent them
  from appearing in any other edition.

  Delete events that you do not want to keep at all.

  Select spans of time,
  and attach them to one or more other editions.
  Elect to continue including detail in your personal edition,
  or to only provide a summary.

  For example, one could have these editions:

  - Personal:

    Include entire stream,
    except for confidential client work
    which is only summarized.

    Suitable for long-term storage.

  - Public:

    Include all events marked for the "public" edition,
    except for individually-excluded events.

    Showcase projects you're contributing to,
    or interesting things you've found.

  - Consultancy:

    Include all events marked for each client's edition,
    except for individually-excluded events.

    Use it for your own purposes,
    or share it with your client.

    When your contract expires and you need to clean up,
    only a summary was included in your personal edition.


Architecture
------------

..  figure:: http://ditaa.org/ditaa/render?grid=%2B-------------%2B+++%2B-------------%2B+++%2B-------------%2B%0D%0A%7C+%7Bd%7D+++++++++%7C+++%7C+%7Bs%7D+++++++++%7C+++%7C+%7Bio%7D++++++++%7C%0D%0A%7C+Filesystem++%7C+++%7C+Database++++%7C+++%7C+Remote++++++%7C%0D%0A%7C+Data+Source+%7C+++%7C+Data+Source+%7C+++%7C+Data+Source+%7C%0D%0A%2B-------------%2B+++%2B-------------%2B+++%2B-------------%2B%0D%0A+++++++%7C+++++++++++++++++%7C+++++++++++++++++%5E%0D%0A+++++++%7C+++++++++++++++++%7C+++++++++++++++++%7C%0D%0A+++++++v+++++++++++++++++v+++++++++++++++++v%0D%0A+%2B-----------%2B+++++%2B-----------%2B+++++%2B-----------%2B%0D%0A+%7C+Collector+%7C+++++%7C+Collector+%7C+++++%7C+Collector+%7C%0D%0A+%2B-----%2B-----%2B+++++%2B-----%2B-----%2B+++++%2B-----%2B-----%2B%0D%0A+++++++%7C+++++++++++++++++%7C+++++++++++++++++%7C%0D%0A+++++++%7C+++++++++++++++++%7C+++++++++++++++++%7C%0D%0A+++++++v+++++++++++++++++v+++++++++++++++++v%0D%0A+++++%2F---%2B+++++++++++++%2F---%2B+++++++++++++%2F---%2B%0D%0A+++++%7C+X+%7C+%28event%29+++++%7C+Y+%7C+%28event%29+++++%7C+Z+%7C+%28event%29%0D%0A+++++%2B-%2B-%2B+++++++++++++%2B-%2B-%2B+++++++++++++%2B-%2B-%2B%0D%0A+++++++%7C+++++++++++++++++%7C+++++++++++++++++%7C%0D%0A+++++++%7C+++++++++++++++++%7C+++++++++++++++++%7C%0D%0A+++++++%5C-----------------%2B-----------------%2B----------%5C%0D%0A++++++++++++++++++++++++++++++++++++++++++++++++++++++%7C%0D%0A++++++++++++++++++++++++++++++++++++++++++++++++++++++%7C%0D%0A++++++++++++++++++++++++++++++++++++++++++++++++++++++%7C+++++%3C--+via+ZeroMQ%0D%0A++++++++++++++++++++++++++++++++++++++++++++++++++++++%7C%0D%0A+++++++++++%2B----------%2B++++%2F---%2B+++++++%2B---------%2B++++%7C%0D%0A+++++++++++%7C+%7Bs%7D++++++%7C%3C---%2BXYZ%2B-------%2B+Storage+%7C%3C---%2B%0D%0A+++++++++++%7C+Event+db+%7C++++%2B---%2B+++++++%7C+Process+%7C++++%7C%0D%0A+++++++++++%2B----------%2B++++++++++++++++%2B---------%2B++++%7C%0D%0A+++++++++++++++++%7C++++++++++++++++++++++++++++++++++++%7C%0D%0A+++++++++++++++%2F-%2B-%2B++++++++++++++++++++++++++++++++++%7C%0D%0A+++++++++++++++%7CABC%7C++++++++++++++++++++++++++++++++++%7C%0D%0A+++++++++++++++%2B-%2B-%2B++++++++++++++++++++++++++++++++++%7C%0D%0A+++++++++++++++++%7C+++++++++++++++++++++%2B---------%2B++++%7C%0D%0A+++++++++++++++++%5C--------------------%3E%7C+UI++++++%7C%3C---%2F%0D%0A+++++++++++++++++++++++++++++++++++++++%7C+Process+%7C%0D%0A+++++++++++++++++++++++++++++++++++++++%2B----%2B----%2B%0D%0A++++++++++++++++++++++++++++++++++++++++++++%7C%0D%0A++++++++++++++++++++++++++++++++++++++++++++%7C%0D%0A++++++++++++++++++++++++++++++++++++++++++%2F-%2B-%2B%0D%0A++++++++++++++++++++++++++++++++++++++++++%7CABC%7C+++++%3C--+via+HTTP%0D%0A++++++++++++++++++++++++++++++++++++++++++%7CXYZ%7C+++++++++or+WebSockets%0D%0A++++++++++++++++++++++++++++++++++++++++++%2B-%2B-%2B%0D%0A++++++++++++++++++++++++++++++++++++++++++++%7C%0D%0A++++++++++++++++++++++++++++++++++++++++++++%7C%0D%0A+++++++++%2B----------------------------------%7C------------------%2B%0D%0A+++++++++%7C+Web+Browser++++++++++++++++++++++%7C++++++++++++++++++%7C%0D%0A+++++++++%2B----------------------------------%7C------------------%2B%0D%0A+++++++++%7C++++++++++++++++++++++++++++++++++v++++++++++++++++++%7C%0D%0A+++++++++%7C+++++++++++++++++++++++++++++%2B-----------------%2B+++++%7C%0D%0A+++++++++%7C+++++++++++++++++++++++++++++%7C+Javascript%3A%3A++++%7C+++++%7C%0D%0A+++++++++%7C+++++++++++++++++++++++++++++%7C+Apply+templates+%7C+++++%7C%0D%0A+++++++++%7C+++++++++++++++++++++++++++++%2B----%2B------------%2B+++++%7C%0D%0A+++++++++%7C++++++++++++++++++++++++++++++++++%7C++++++++++++++++++%7C%0D%0A+++++++++%7C++++++++++++++++++++++++++++++++++v++++++++++++++++++%7C%0D%0A+++++++++%7C++%2B-----------------------------------------------%2B++%7C%0D%0A+++++++++%7C++%7C+A+%40+...%3A+...++++++++++++++++++++++++++++++++++%7C++%7C%0D%0A+++++++++%7C++%2B-----------------------------------------------%2B++%7C%0D%0A+++++++++%7C++%7C+B+%40+...%3A+...++++++++++++++++++++++++++++++++++%7C++%7C%0D%0A+++++++++%7C++%2B-----------------------------------------------%2B++%7C%0D%0A+++++++++%7C++%7C+C+%40+...%3A+...++++++++++++++++++++++++++++++++++%7C++%7C%0D%0A+++++++++%7C++%2B-----------------------------------------------%2B++%7C%0D%0A+++++++++%7C++%7C+X+%40+...%3A+...++++++++++++++++++++++++++++++++++%7C++%7C%0D%0A+++++++++%7C++%2B-----------------------------------------------%2B++%7C%0D%0A+++++++++%7C++%7C+Y+%40+...%3A+...++++++++++++++++++++++++++++++++++%7C++%7C%0D%0A+++++++++%7C++%2B-----------------------------------------------%2B++%7C%0D%0A+++++++++%7C++%7C+Z+%40+...%3A+...++++++++++++++++++++++++++++++++++%7C++%7C%0D%0A+++++++++%7C++%2B-----------------------------------------------%2B++%7C%0D%0A+++++++++%7C+++++++++++++++++++++++++++++++++++++++++++++++++++++%7C%0D%0A+++++++++%2B-----------------------------------------------------%2B&scale=1&background=FFFFFF&E=on&timeout=10
    :alt: Proposed Crème de Flux architecture

    An overview of the proposed CDF architecture.

    Three collectors receive data
    from different kinds of data sources.
    The collectors generate events
    and publish them via ZeroMQ.

    A storage process receives events
    and stores them in a database.

    A UI process receives events,
    and also retrieves past events from the database,
    then transmits them to a web page
    via HTTP or WebSockets.

    JavaScript in the web browser
    applies event data to templates,
    then renders events in chronological order.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
