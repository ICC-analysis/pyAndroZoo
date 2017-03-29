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

.. code:: python

    Python 3.6.1 (default, Mar 22 2017, 07:04:41)
    [GCC 6.2.0 20161005] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pyandrozoo
    >>> androzoo = pyandrozoo.pyAndroZoo('<YOUR-API-KEY>')
    >>> result, apk_name = androzoo.get('<SHA256>')


Alternatively you can set the AndroZoo API key in an environment variable:

.. code:: shell

    $ export androzoo_api_key=<YOUR-API-KEY>

.. code:: python

    Python 3.6.1 (default, Mar 22 2017, 07:04:41)
    [GCC 6.2.0 20161005] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pyandrozoo
    >>> androzoo = pyandrozoo.pyAndroZoo()
    >>> result, apk_name = androzoo.get('<SHA256>')



Contact
-------

`Cédric Bonhomme <https://www.cedricbonhomme.org>`_
