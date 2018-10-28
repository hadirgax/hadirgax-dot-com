
# PostgreSQL in Ubuntu

## Installation
------------
Ubuntu comands to install postgresql:

```bash
$ update the repository base
```

Install the repository:
```bash
$ sudo apt-get install postgresql-10
```

## Setting the role user:
The default postgresql user role is the `postgres`, then to activate it, type at bash console:

```bash
$ sudo -i -u postgres
```
So you can access to the prompt :bash:'$ psql', or use the next command to access postgresql role without change bash role:

.. code-block:: bash
    $ sudo -u postgres psql


Create a new role
-----------------
To add a new postgre role, different of the default :bash:'postgres'

Creating from :bash:'postgres' role:

.. code-block:: bash
    postgres@server:~$ createuser --interavtive

Creating from :bash:'sudo'

.. code-block:: bash
    $ sudo -u postgres createuser --interavtive


Creating a new database
-----------------------

postgresql help
---------------
To acces the help list
