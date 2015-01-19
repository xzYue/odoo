.. _setup/install:

===============
Installing Modoo
===============

There are mutliple ways to install Modoo, or not install it at all, depending
on the intended use case.

This documents attempts to describe most of the installation options.

:ref:`setup/install/demo`
    the simplest "installation", only suitable for getting a quick feel for
    Modoo or trying something out
:ref:`setup/install/saas`
    trivial to start with and fully managed and migrated by Modoo S.A., can be
    used to both test Modoo and use it for your business, but restricts the
    flexibility of the system somewhat (check: no custom modules? what else?).

    Can be used for both testing Modoo and long-term "production" use.
:ref:`setup/install/packaged`
    simple to get started, allows more flexibility in hosting and deploying
    the system and greater control over where data is stored. The maintenance
    burden is shifted to the user.

    Suitable for testing Modoo, developing modules and can be used for
    long-term production use with additional deployment and maintenance work.
:ref:`setup/install/source`
    harder to get started than :ref:`setup/install/packaged`, provides
    even greater flexibility: packaged installers don't generally allow
    multiple running Modoo versions on the same system, and don't provide easy
    source access to Modoo itself.

    Good for developing modules, can be used as base for production
    deployment.

    The source code can be obtained by downloading a tarball or using git.
    Using git makes it easier to update, switching between multiple versions
    and contribute.

.. _setup/install/demo:

Demo
====

To simply get a quick idea of Modoo, demo_ instances are available. They are
shared instances which only live for a few hours, and can be used to browse
around and try things out with no commitment.

Demo_ instances require no local installation, just a web browser.

.. _setup/install/saas:

SaaS
====

Modoo's SaaS_ provides private instances and starts out free. It can be used to
discover and test Modoo and do non-code customizations without having to
install it locally.

Like demo_ instances, SaaS_ instances require no local installation, a web
browser is sufficient.

.. _setup/install/packaged:

Packaged installers
===================

Modoo provides packaged installers for Windows, deb-based distributions
(Debian, Ubuntu, …) and RPM-based distributions (Fedora, CentOS, RHEL, …).

These packages automatically set up all dependencies, but may be difficult to
keep up-to-date.

Official packages with all relevant dependency requirements are available on
https://nightly.modoo.com.

Windows
-------

* download https://nightly.modoo.com/8.0/nightly/exe/odoo_8.0.latest.exe
* run the downloaded file

  .. warning:: on Windows 8, you may see a warning titled "Windows protected
               your PC". Click :guilabel:`More Info` then
               :guilabel:`Run anyway`

* Accept the UAC_ prompt
* Go through the various installation steps

Modoo will automatically be started at the end of the installation.

Configuration
'''''''''''''

The :ref:`configuration file <reference/cmdline/config>` can be found at
:file:`{%PROGRAMFILES%}\\Modoo 8.0-{id}\\server\\openerp-server.conf`.

The configuration file can be edited to connect to a remote Postgresql, edit
file locations or set a dbfilter.

To reload the configuration file, restart the Modoo service via
:menuselection:`Services --> modoo server`.

Deb
---

To install Modoo 8.0 on Debian-based distribution, execute the following
commands as root:

.. code-block:: console

    # wget -O - https://nightly.modoo.com/modoo.key | apt-key add -
    # echo "deb http://nightly.modoo.com/8.0/nightly/deb/ ./" >> /etc/apt/sources.list
    # apt-get update && apt-get install modoo

This will automatically install all dependencies, install Modoo itself as a
daemon and automatically start it.

.. danger:: to print PDF reports, you must install wkhtmltopdf_ yourself:
            the version of wkhtmltopdf_ available in debian repositories does
            not support headers and footers so it can not be installed
            automatically. Use the version available on
            `the wkhtmltopdf download page`_.

Configuration
'''''''''''''

The :ref:`configuration file <reference/cmdline/config>` can be found at
:file:`/etc/modoo/openerp-server.conf`

When the configuration file is edited, Modoo must be restarted using
``service``:

.. code-block:: console

    $ sudo service modoo restart
    Restarting modoo: ok

RPM
---

.. warning::

    with RHEL-based distributions (RHEL, CenOS, Scientific Linux), EPEL_ must
    be added to the distribution's repositories for all of Modoo's
    dependencies to be available. For CenOS:

    .. code-block:: console

        $ sudo yum install -y epel-release

    For other RHEL-based distribution, see the EPEL_ documentation.

.. code-block:: console

    $ sudo yum install -y postgresql-server
    $ sudo postgresql-setup initdb
    $ sudo systemctl enable postgresql
    $ sudo systemctl start postgresql
    $ sudo yum-config-manager --add-repo=https://nightly.modoo.com/8.0/nightly/rpm/modoo.repo
    $ sudo yum install -y modoo
    $ sudo systemctl enable modoo
    $ sudo systemctl start modoo

.. danger:: to print PDF reports, you must install wkhtmltopdf_ yourself:
            the version of wkhtmltopdf_ available in Fedora/CentOS
            repositories does not support headers and footers so it can not
            be installed automatically. Use the version available on
            `the wkhtmltopdf download page`_.

Configuration
'''''''''''''

The :ref:`configuration file <reference/cmdline/config>` can be found at
:file:`/etc/modoo/openerp-server.conf`

When the configuration file is edited, Modoo must be restarted via SystemD:

.. code-block:: console

    $ sudo systemctl restart modoo


.. _setup/install/source:

Source Install
==============

The source "installation" really is about not installing Modoo, and running
it directly from source instead.

This can be more convenient for module developers as the Modoo source is
more easily accessible than using packaged installation (for information or
to build this documentation and have it available offline).

It also makes starting and stopping Modoo more flexible and explicit than the
services set up by the packaged installations, and allows overriding settings
using :ref:`command-line parameters <reference/cmdline>` without needing to
edit a configuration file.

Finally it provides greater control over the system's set up, and allows more
easily keeping (and running) multiple versions of Modoo side-by-side.

There are two way to get the modoo sourcei source tarball or git.

Using git allows simpler update and easier switching between differents
versions of Modoo. It also simplifies maintaining non-module patches and
contributions.  The primary drawback of git is that it is significantly larger
than a tarball as it contains the entire history of the Modoo project.

The Modoo tarball can be downloaded from
https://nightly.modoo.com/8.0/nightly/src/odoo_8.0-latest.tar.gz

On windows `7-Zip <http://www.7-zip.org>`_ may be use to decompress the archive
as Windows does not handle .tar.gz archives natively.

The git repository is https://github.com/modoo/modoo.git and can be cloned using
the command

.. code-block:: console

    $ git clone https://github.com/modoo/modoo.git


Installing dependencies
-----------------------

Source installation requires manually installing dependencies:

* Python 2.7.

  - on Linux, already included
  - on OS X, already included
  - on Windows, use `the official Python 2.7 installer
    <https://www.python.org/downloads/windows/>`_.

* PostgreSQL, to use a local database

  After installation you will need to create a postgres user (also named a
  role), by default the only user is ``postgres``, and Modoo forbids connecting
  as ``postgres``.

  - on Linux, use your distribution's package, then create a postgres user
    named like your login:

    .. code-block:: console

        $ sudo su - postgres -c "createuser -s $USER"

    Because the role login is the same as your unix login unix sockets can be
    use without a password.

  - on OS X, `postgres.app <http://postgresapp.com>`_ is the simplest way to
    get started, then create a postgres user like on Linux.

  - on Windows, use `PostgreSQL for windows`_ then add PostgreSQL's ``bin``
    directory (default: ``C:\Program Files\PostgreSQL\9.3\bin``) to your
    :envvar:`PATH`

    Then create a postgres user with a password using the pg admin gui, for
    example login ``modoo`` and password ``modoo``.

    This user and password will be provided with the -w and -r option or in the
    config file.

* Python dependencies listed in the :file:`requirements.txt` file.


  - on Linux python dependencies may be installable with the system's package
    manager or using pip.

    For libraries using native code (Pillow, lxml, greenlet, gevent, psycopg2) it
    may be necessary to install development tools and native dependencies before
    pip is able to install the dependencies themselves. These are available in
    ``-dev`` or ``-devel`` packages for Python, Postgres, libxml2, libxslt and
    libevent. Then the dependecies can be installed using 

    .. code-block:: console

        $ pip install -r requirements.txt

  - on OS X, install the Command Line Tools (``xcode-select --install``) the
    native dependency via your preferred package manager (macports_,
    homebrew_). Then pip can be used.

    .. code-block:: console

        $ pip install -r requirements.txt

  - on Windows you need to install some of the dependencies manually, tweak the
    requirements.txt file, then run pip to install the remaning ones.

    Install ``psycopg`` using the installer here
    http://www.stickpeople.com/projects/python/win-psycopg/

    Install ``pip`` from http://www.lfd.uci.edu/~gohlke/pythonlibs/

    Then edit the requirements.txt file:

    - remove ``psycopg`` as you already have it.

    - remove the optional ``python-ldap``, ``gevent`` and ``psutil`` because they
      require compilation.

    - add ``pypiwin32`` because it's needed under windows.

    Then use pip to install install the dependecies using the following command
    from a cmd.exe prompt

    .. code-block:: console

        C:\> cd \YourOdooPath
        C:\YourOdooPath> C:\Python27\Scripts\pip.exe install -r requirements.txt

* Less css compiler via nodejs

  - on Linux, use your distribution's package to install nodejs and npm.

    In debian you need at least jessie, as the packaged version of npm before
    that does not work. In Ubuntu you need at least Ubuntu 14.04, as the
    packaged version of npm before that does not work. Otherwise install nodejs
    and npm manually.

    Once you have npm working, install less and less-plugin-clean-css.

    .. code-block:: console

        $ sudo npm install -g less less-plugin-clean-css

    On debian and Ubuntu you also need to set a symbolic link from noejs to
    node because the shebang line of lessc uses node.

    .. code-block:: console

        $ sudo ln -s /usr/bin/nodejs /usr/bin/node


  - on OS X, install nodejs via your preferred package manager (macports_,
    homebrew_) then install less and less-plugin-clean-css.

    .. code-block:: console

        $ sudo npm install -g less less-plugin-clean-css


  - on Windows, install nodejs then reboot and install less and
    less-plugin-clean-css.

    .. code-block:: console

        C:\> npm install -g less less-plugin-clean-css


Running Modoo
------------

Once all dependencies are set up, Modoo can be launched by running ``modoo.py``.

:ref:`Configuration <reference/cmdline>` can be provided either through
:ref:`command-line arguments <reference/cmdline>` or through a
:ref:`configuration file <reference/cmdline/config>`.

Common necessary configurations are:

* PostgreSQL host, port, user and password.

  Modoo has no defaults beyond
  `psycopg2's defaults <http://initd.org/psycopg/docs/module.html>`_: connects
  over a UNIX socket on port 5432 with the current user and no password.

* Custom addons path beyond the defaults, to load your own modules

Under Windows a typical way to execute modoo would be:

    .. code-block:: console

        C:\YourOdooPath> python modoo.py -w modoo -r modoo --addons-path=addons,../mymodules --db-filter=mydb$

Where ``modoo``, ``modoo`` are the postgresql login and password,
``../mymodules`` a directory with additional addons and ``mydb`` the default db
to serve on localhost:8069

Under Unix a typical way to execute modoo would be:

    .. code-block:: console

        $ ./modoo.py --addons-path=addons,../mymodules --db-filter=mydb$

Where ``../mymodules`` is a directory with additional addons and ``mydb`` the default db
to serve on localhost:8069


.. _demo: https://demo.modoo.com
.. _EPEL: https://fedoraproject.org/wiki/EPEL
.. _PostgreSQL: http://www.postgresql.org
.. _the official installer:
.. _install pip:
    https://pip.pypa.io/en/latest/installing.html#install-pip
.. _PostgreSQL for windows:
    http://www.enterprisedb.com/products-services-training/pgdownload
.. _Quilt: http://en.wikipedia.org/wiki/Quilt_(software)
.. _saas: https://www.modoo.com/page/start
.. _the wkhtmltopdf download page: http://wkhtmltopdf.org/downloads.html
.. _UAC: http://en.wikipedia.org/wiki/User_Account_Control
.. _wkhtmltopdf: http://wkhtmltopdf.org
.. _pip: https://pip.pypa.io
.. _macports: https://www.macports.org
.. _homebrew: http://brew.sh
.. _Visual C++ Compiler for Python 2.7:
    http://www.microsoft.com/en-us/download/details.aspx?id=44266
.. _wheels: https://wheel.readthedocs.org/en/latest/
.. _virtual environment: http://docs.python-guide.org/en/latest/dev/virtualenvs/
.. _pywin32: http://sourceforge.net/projects/pywin32/files/pywin32/
.. _the repository: https://github.com/modoo/modoo
.. _git: http://git-scm.com
