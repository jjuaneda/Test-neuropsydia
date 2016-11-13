.. neuropsydia documentation master file, created by
   sphinx-quickstart on Sun Nov 13 12:53:57 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Neuropsydia's documentation!
=======================================

Contents:

.. toctree::
   :maxdepth: 2

   neuropsydia
   tutorials


Installation
------------

Installation can be easily done with ``pip``:

.. code:: bash

    $ pip install biosppy

Simple Example
--------------

The code below loads an ECG signal from the ``examples`` folder, filters
it, performs R-peak detection, and computes the instantaneous heart
rate.

.. code:: python

    import numpy as np
    from biosppy.signals import ecg

    # load raw ECG signal
    signal = np.loadtxt('./examples/ecg.txt')

    # process it and plot
    out = ecg.ecg(signal=signal, sampling_rate=1000., show=True)
Index
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
