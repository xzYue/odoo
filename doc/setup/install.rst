.. _setup/install:

================
Installing Modoo
================

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
    Using git makes it easier to update, switch between multiple versions
    (including the current development version) or contribute.
`docker image <https://registry.hub.docker.com/_/modoo/>`_
    if you usually use docker_ for development or deployment, an official
    docker_ base image is available, see the image's help document for more
    information

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

There are two way to get the modoo source source zip or git.

* Modoo zip can be downloaded from
  https://nightly.modoo.com/8.0/nightly/src/odoo_8.0.latest.zip, the zip file
  then needs to be uncompressed to use its content

* git allows simpler update and easier switching between differents versions
  of Modoo. It also simplifies maintaining non-module patches and
  contributions.  The primary drawback of git is that it is significantly
  larger than a tarball as it contains the entire history of the Modoo project.

  The git repository is https://github.com/modoo/modoo.git.

  Downloading it requires a `a git client <http://git-scm.com/download/>`_
  (which may be available via your distribution on linux) and can be performed
  using the following command:

  .. code-block:: console

      $ git clone https://github.com/modoo/modoo.git

Installing dependencies
-----------------------

Source installation requires manually installing dependencies:

* Python 2.7.

  - on Linux and OS X, included by default
  - on Windows, use `the official Python 2.7.9 installer
    <https://www.python.org/downloads/windows/>`_.

    .. warning:: select "add python.exe to Path" during installation, and
                 reboot afterwards to ensure the :envvar:`PATH` is updated

    .. note:: if Python is already installed, make sure it is 2.7.9, previous
              versions are less convenient and 3.x versions are not compatible
              with Modoo

* PostgreSQL, to use a local database

  After installation you will need to create a postgres user: by default the
  only user is ``postgres``, and Modoo forbids connecting as ``postgres``.

  - on Linux, use your distribution's package, then create a postgres user
    named like your login:

    .. code-block:: console

        $ sudo su - postgres -c "createuser -s $USER"

    Because the role login is the same as your unix login unix sockets can be
    use without a password.

  - on OS X, `postgres.app <http://postgresapp.com>`_ is the simplest way to
    get started, then create a postgres user as on Linux

  - on Windows, use `PostgreSQL for windows`_ then

    - add PostgreSQL's ``bin`` directory (default:
      ``C:\Program Files\PostgreSQL\9.4\bin``) to your :envvar:`PATH`
    - create a postgres user with a password using the pg admin gui: open
      pgAdminIII, double-click the server to create a connection, select
      :menuselection:`Edit --> New Object --> New Login Role`, enter the
      usename in the :guilabel:`Role Name` field (e.g. ``modoo``), then open
      the :guilabel:`Definition` tab and enter the password (e.g. ``modoo``),
      then click :guilabel:`OK`.

      The user and password must be passed to Modoo using either the
      :option:`-w <modoo.py -w>` and :option:`-r <modoo.py -r>` options or
      :ref:`the configuration file <reference/cmdline/config>`

* Python dependencies listed in the :file:`requirements.txt` file.

  - on Linux, python dependencies may be installable with the system's package
    manager or using pip.

    For libraries using native code (Pillow, lxml, greenlet, gevent, psycopg2,
    ldap) it may be necessary to install development tools and native
    dependencies before pip is able to install the dependencies themselves.
    These are available in ``-dev`` or ``-devel`` packages for Python,
    Postgres, libxml2, libxslt, libevent and libsasl2. Then the Python
    dependecies can themselves be installed:

    .. code-block:: console

        $ pip install -r requirements.txt

  - on OS X, you will need to install the Command Line Tools
    (``xcode-select --install``) then download and install a package manager
    of your choice (homebrew_, macports_) to install non-Python dependencies.
    pip can then be used to install the Python dependencies as on Linux:

    .. code-block:: console

        $ pip install -r requirements.txt

  - on Windows you need to install some of the dependencies manually, tweak the
    requirements.txt file, then run pip to install the remaning ones.

    Install ``psycopg`` using the installer here
    http://www.stickpeople.com/projects/python/win-psycopg/

    Then edit the requirements.txt file:

    - remove ``psycopg2`` as you already have it.
    - remove the optional ``python-ldap``, ``gevent`` and ``psutil`` because
      they require compilation.
    - add ``pypiwin32`` because it's needed under windows.

    Then use pip to install install the dependencies using the following
    command from a cmd.exe prompt (replace ``\YourOdooPath`` by the actual
    path where you downloaded Modoo):

    .. code-block:: ps1

        C:\> cd \YourOdooPath
        C:\YourOdooPath> C:\Python27\Scripts\pip.exe install -r requirements.txt

* *Less CSS* via nodejs

  - on Linux, use your distribution's package manager to install nodejs and
    npm.

    .. warning::

        In debian wheezy and Ubuntu 13.10 and before you need to install
        nodejs manually:

        .. code-block:: console

            $ wget -qO- https://deb.nodesource.com/setup | bash -
            $ apt-get install -y nodejs

        In later debian (>jessie) and ubuntu (>14.04) you may need to add a
        symlink as npm packages call ``node`` but debian calls the binary
        ``nodejs``

        .. code-block:: console

            $ apt-get install -y npm
            $ sudo ln -s /usr/bin/nodejs /usr/bin/node

    Once npm is installed, use it to install less and less-plugin-clean-css:

    .. code-block:: console

        $ sudo npm install -g less less-plugin-clean-css

  - on OS X, install nodejs via your preferred package manager (homebrew_,
    macports_) then install less and less-plugin-clean-css:

    .. code-block:: console

        $ sudo npm install -g less less-plugin-clean-css

  - on Windows, `install nodejs <http://nodejs.org/download/>`_, reboot (to
    update the :envvar:`PATH`) and install less and less-plugin-clean-css:

    .. code-block:: ps1

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
  over a UNIX socket on port 5432 with the current user and no password. By
  default this should work on Linux and OS X, but it *will not work* on
  windows as it does not support UNIX sockets.

* Custom addons path beyond the defaults, to load your own modules

Under Windows a typical way to execute modoo would be:

.. code-block:: ps1

    C:\YourOdooPath> python modoo.py -w modoo -r modoo --addons-path=addons,../mymodules --db-filter=mydb$

Where ``modoo``, ``modoo`` are the postgresql login and password,
``../mymodules`` a directory with additional addons and ``mydb`` the default
db to serve on localhost:8069

Under Unix a typical way to execute modoo would be:

.. code-block:: console

    $ ./modoo.py --addons-path=addons,../mymodules --db-filter=mydb$

Where ``../mymodules`` is a directory with additional addons and ``mydb`` the
default db to serve on localhost:8069

.. _demo: https://demo.modoo.com
.. _docker: https://www.docker.com
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
