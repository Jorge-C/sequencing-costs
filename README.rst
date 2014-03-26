DNA sequencing costs graph
==========================

DNA sequencing costs are decreasing at an exceptionally fast pace. The National Human Genome Research Institute (NHGRI) has kept track of the changing costs, and makes graphs and raw data available [1]_.

This package downloades and parses the raw data, and then plots it with some relevant annotations like the publication of QIIME [2]_ or the transition from Sanger-based sequencing technologies to next-generation ones.


Dependencies
============

Font
----

To get the right font, you'll need to have installed Humor-Sans (https://github.com/shreyankg/xkcd-desktop). Otherwise, the plot will default to Comic Sans. Please remember to remove matplotlib's font cache after installing a new font (in Linux, deleting ``~/.matplotlib/fontList.cache`` is enough).

Software
--------

- `pandas` is required to parse an excel file.

- `matplotlib` for plotting.

- `numpy`

- `requests` is used to download the data.

Usage
=====

Download the `.py` file and run it. It will create a pdf image: `sequencing_cost.pdf`. The code is quite simple, so it should be easy to tweak it if needed.

Contribute
==========

Please post any issue that you may find in the issue tracker, share it with friends, contribute a different plot style...


References
==========

.. [1] Wetterstrand KA. DNA Sequencing Costs: Data from the NHGRI Genome Sequencing Program (GSP) Available at: www.genome.gov/sequencingcosts. Accessed 2014-03-26.

.. [2] QIIME allows analysis of high-throughput community sequencing data. J Gregory Caporaso, Justin Kuczynski, Jesse Stombaugh, Kyle Bittinger, Frederic D Bushman, Elizabeth K Costello, Noah Fierer, Antonio Gonzalez Pena, Julia K Goodrich, Jeffrey I Gordon, Gavin A Huttley, Scott T Kelley, Dan Knights, Jeremy E Koenig, Ruth E Ley, Catherine A Lozupone, Daniel McDonald, Brian D Muegge, Meg Pirrung, Jens Reeder, Joel R Sevinsky, Peter J Turnbaugh, William A Walters, Jeremy Widmann, Tanya Yatsunenko, Jesse Zaneveld and Rob Knight; Nature Methods, 2010; doi:10.1038/nmeth.f.303