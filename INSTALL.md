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
writing dependency_links to tsvdro.egg-info/dependency_links.txt
writing top-level names to tsvdro.egg-info/top_level.txt
writing tsvdro.egg-info/PKG-INFO
writing manifest file 'tsvdro.egg-info/SOURCES.txt'
reading manifest file 'tsvdro.egg-info/SOURCES.txt'
writing manifest file 'tsvdro.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_py
creating build
creating build/lib
creating build/lib/tsvdro
copying tsvdro/__init__.py -> build/lib/tsvdro
copying tsvdro/tsvdro.py -> build/lib/tsvdro
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/egg
creating build/bdist.linux-x86_64/egg/tsvdro
copying build/lib/tsvdro/__init__.py -> build/bdist.linux-x86_64/egg/tsvdro
copying build/lib/tsvdro/tsvdro.py -> build/bdist.linux-x86_64/egg/tsvdro
byte-compiling build/bdist.linux-x86_64/egg/tsvdro/__init__.py to __init__.cpython-35.pyc
byte-compiling build/bdist.linux-x86_64/egg/tsvdro/tsvdro.py to tsvdro.cpython-35.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying tsvdro.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying tsvdro.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying tsvdro.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying tsvdro.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating dist
creating 'dist/tsvdro-1.0.0-py3.5.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing tsvdro-1.0.0-py3.5.egg
Copying tsvdro-1.0.0-py3.5.egg to /afs/dbic.dartmouth.edu/usr/pkg/python/python_v3.5.3/@sys/lib/python3.5/site-packages
Adding tsvdro 1.0.0 to easy-install.pth file

Installed /afs/dbic.dartmouth.edu/usr/pkg/python/python_v3.5.3/@sys/lib/python3.5/site-packages/tsvdro-1.0.0-py3.5.egg
Processing dependencies for tsvdro==1.0.0
Finished processing dependencies for tsvdro==1.0.0
</pre>
