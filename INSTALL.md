<h1>Installing the Package</h1>

Clone Github repository:
<pre>
[jed@dexter ~] > git clone http://github.com/jeddobson/tsvdro
Initialized empty Git repository in /afs/dbic.dartmouth.edu/usr/grafton/jed/tsvdro/.git/
remote: Counting objects: 419, done.
remote: Compressing objects: 100% (365/365), done.
remote: Total 419 (delta 62), reused 395 (delta 41), pack-reused 0
Receiving objects: 100% (419/419), 6.12 MiB | 5.66 MiB/s, done.
Resolving deltas: 100% (62/62), done.
</pre>


Now install (might need to run as root or via sudo):

<pre>
[jed@dexter tsvdro] > python3 setup.py install
running install
running bdist_egg
running egg_info
creating tsvdro.egg-info
...
Processing dependencies for tsvdro==1.0.0
Finished processing dependencies for tsvdro==1.0.0
</pre>


The package is now available for use:

<pre>
[jed@dexter ~] > python3
Python 3.5.3 (default, Feb 16 2017, 10:18:46) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-17)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from tsvdro import tsvdro
>>> data = tsvdro.load('tsvdro/sample/na-slave-narratives/fpn-steward-steward.dro')
>>> data['header']['workflow']
{'created_date': '2018-08-06 12:27', 'data_type': 1, 'data_option': None, 'last_updated': '2018-08-06 12:27', 'token_count': 93719, 'created_by': 'tsvdro_reference_implementation', 'created_system': 'parergon.local', 'vocab_count': 7767}
</pre>

