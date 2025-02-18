pyAndroZoo
==========

`pyAndroZoo <https://github.com/ICC-analysis/pyAndroZoo>`_ is a Python library
to access the `AndroZoo <https://androzoo.uni.lu>`_ data set.

Installation
------------

.. code:: bash

    $ sudo pip install pyAndroZoo


Usage
-----

Retrieve APKs with asynchronous HTTP requests.

.. code:: python

    Python 3.6.1 (default, Mar 22 2017, 07:04:41)
    [GCC 6.2.0 20161005] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pyandrozoo
    >>> androzoo = pyandrozoo.pyAndroZoo('<YOUR-API-KEY>')

    >>> apks = [
        '0000003B455A6C7AF837EF90F2EAFFD856E3B5CF49F5E27191430328DE2FA670',
        '00000439A3FFA123C3F9BC45E5E821351B1A5C276871B36447AB80C74261F354',
        '00000989F3E215BA9FC3BDD5B56AF751343B540C1026BF42AEA8FEBF68874ECC',
        '00000F8EE4F64324BA04356745E946152C2F43ECB63372E89DB79830BADAF1BA',
        '00001112E046D8BBF8B5529A9ECB39920F828209EF4ABFEB95AAB46D41F56A7D',
        '0000143EF8D00E3A65C5C8C380221D00678FED906FDC2EBC483D1987457C7B2B',
        '000014F7037586315DE348D21337B90B83A1C887E247DA8E4CC043702E36DFBA',
        '00001A21E96C4D131B5DC27897E89D23FC35D6D75A4CE1B15D6D30A4E4FC60F1'
    ]

    >>> androzoo.get(apks)


Alternatively you can set the AndroZoo API key in an environment variable:

.. code:: shell

    $ export androzoo_api_key=<YOUR-API-KEY>

.. code:: python

    Python 3.6.1 (default, Mar 22 2017, 07:04:41)
    [GCC 6.2.0 20161005] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pyandrozoo
    >>> androzoo = pyandrozoo.pyAndroZoo()
    >>> androzoo.get(['<SHA256>'])



Contact
-------

`Cédric Bonhomme <https://www.cedricbonhomme.org>`_

Copyright (C) 2017-2025 Cédric Bonhomme - https://github.com/cedricbonhomme
