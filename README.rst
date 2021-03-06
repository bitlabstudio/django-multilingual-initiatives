Django Multilingual Initiatives
===============================

An app for showing localized versions of initiatives. E.g. as plugin
in a blog post.

Comes with a django-cms plugin and is multilingual.

Prerequisites
-------------

You will need to have the following packages installed:

* django-cms (cms 3 beta tested)


Installation
------------

If you want to install the latest stable release from PyPi::

    $ pip install django-multilingual-initiatives

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-multilingual-initiatives.git#egg=multilingual_initiatives

Add ``multilingual_initiatives`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'multilingual_initiatives',
    )

Run the South migrations::

    ./manage.py migrate multilingual_initiatives


Usage
-----

Use the Django admin to create your initiative objects. If you are using
django-cms you can use the ``Initiative Plugin`` to display an initiative
in your placeholders.


Settings
--------

INITIATIVE_PLUGIN_DISPLAY_TYPE_CHOICES
++++++++++++++++++++++++++++++++++

Default::

    [
        ('small', _('small')),
        ('big', _('big')),
    ]

When using the ``Initiative Plugin`` in your django-cms placeholders you will
notice that you only have two choices for the ``Display type``. This field
can be helpful when you want to render an Initiative differently in different
parts of your site. If you need even more display types, just set this setting
to a different list of tuples.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
