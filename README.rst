========
pyboleto
========

.. _pyboleto-synopsis:

pyboleto provides a python class to generate "boletos de cobranca" as these
are the Brazilian equivalent for invoices.

It's easy to implement classes for new banks.

This class is still in development and currently has no documented API.

.. contents::
    :local:

.. _pyboleto-implemented-bank:

Implemented Banks
=================

You can help writing code for more banks or printing and testing current
implementations.

For now here's where we are.

 +----------------------+----------------+-----------------+------------+
 | **Bank**             | **Carteira /** | **Implemented** | **Tested** |
 |                      | **Convenio**   |                 |            |
 +======================+================+=================+============+
 | **Banco do Brasil**  | 18             | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Banrisul**         | -              | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Bradesco**         | 09, 06, 03     | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Caixa Economica**  | SR ,SIGCB,SINCO| Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Banco Nordeste**   | 51             | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Bancoob (Sicoob)** | 1              | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **HSBC**             | CNR, CSB       | Yes             | No         |
 +----------------------+----------------+-----------------+------------+
 | **Itau**             | 175, 174, 178, | Yes             | Yes        |
 |                      | 104, 109, 157  |                 |            |
 +----------------------+----------------+-----------------+------------+
 | **Banco da Amazonia**| CNR            | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Sicredi**          | A(Simples)     | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Real**             | 57             | Yes             | No         |
 +----------------------+----------------+-----------------+------------+
 | **Santander**        | 102, 101, 201  | Yes             | No         |
 +----------------------+----------------+-----------------+------------+


Installation
============

Using the development version
-----------------------------

You can clone the repository by doing the following::

    $ git clone https://github.com/thiagosm/pyboleto.git
    $ cd pyboleto
    $ python setup.py install 


License
=======

This software is licensed under the `New BSD License`. See the ``LICENSE``
file in the top distribution directory for the full license text.

.. vim:tw=0:sw=4:et
