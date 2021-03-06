# -*- coding: utf-8 -*-
#
# Author: Taylor Smith <taylor.smith@alkaline-ml.com>

from __future__ import absolute_import

from sklearn.externals import six

__all__ = [
    'flatten_all',
    'is_iterable'
]


def flatten_all(container):
    """Recursively flattens an arbitrarily nested iterable.

    Parameters
    ----------
    container : array_like, shape=(n_items,)
        The iterable to flatten. If the ``container`` is
        not iterable, it will be returned in a list as
        ``[container]``

    Examples
    --------
    The example below produces a list of mixed results:

        >>> a = [[[],3,4],['1','a'],[[[1]]],1,2]
        >>> list(flatten_all(a))
        [3, 4, '1', 'a', 1, 1, 2]

    Returns
    -------
    res : generator
        A generator of all of the flattened values.
    """
    if not is_iterable(container):
        yield container
    else:
        for i in container:
            if is_iterable(i):
                for j in flatten_all(i):
                    yield j
            else:
                yield i


def is_iterable(x):
    """Determine whether an element is iterable.

    This function determines whether an element is iterable by checking
    for the ``__iter__`` attribute. Since Python 3.x adds the ``__iter__``
    attribute to strings, we also have to make sure the input is not a
    string or unicode type.

    Parameters
    ----------
    x : object
        The object or primitive to test whether
        or not is an iterable.
    """
    if isinstance(x, six.string_types):
        return False
    return hasattr(x, '__iter__')
