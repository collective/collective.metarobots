Introduction
============

This addon add a tag <meta name="robots"... /> and let you specify values
site wide depending on the hostname.

More information on this meta:

* http://support.google.com/webmasters/bin/answer.py?answer=79812
* https://developers.google.com/webmasters/control-crawl-index/docs/robots_meta_tag

This addon has been created to not index content from staging webiste.

Warning: this addon suffer from a Plone bug: https://dev.plone.org/ticket/13158

Use cases
=========

staging or private website
--------------------------

If you want your content not to be indexed, you just have to select
'noindex' and 'nofollow' in configuration.

content with end date
---------------------

If you manage job proposal content or events, you can choose
"unavailable_after_end" in configuration.

Credits
=======

Companies
---------

|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact Makina Corpus <mailto:python@makina-corpus.org>`_

Authors
-------

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

.. Contributors
.. ------------

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
