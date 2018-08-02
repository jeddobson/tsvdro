Prototype format for data-rich humanities objects

This file defines the header and data objects for the TSV-DRHO (Tab Separated
Values - Data-Rich Humanities Object) proposed standard for data sharing.
 
This Python package provides high-level format-independent access to humanities
data for computational purposes.  

Created by Jed Dobson (James.E.Dobson@Dartmouth.EDU) 08/02/2018


- - -

'DRO' is a Data Rich Object (a named borrowed from Katherine Bode) and attached
to the commonly used tab-separated value data favored by many scholars working
on computational methods in the humanities.


- - - 

<h2>Why do this??<h2>

- Capture critical bibliographic metadata

- Record workflow information (what produced this file? when was it produced?) necessary for reproduction

- Store data and metadata together in a single, platform-agnostic format (JSON)

- Provide a standard interface for loading and saving data for computational applications

- - - 

<h2> Using TSVDRO <h2>

Simple display of JSONified object:

<pre>
>>> import tsvdro
>>> import pprint
>>> dro_object = tsvdro.load('na-slave-narratives-dro/fpn-jackson-jackson.dro')
>>> pprint.pprint(dro_object['header'])
{'bibliographic_data': {'author': 'John Andrew Jackson',
                        'author_name': '',
                        'file_uri': 'http://docsouth.unc.edu/full-text/na-slave-narratives/data/texts/fpn-jackson-jackson.txt',
                        'pages': '',
                        'publication_date': '',
                        'publication_year': 1862,
                        'publisher': '',
                        'publisher_location': '',
                        'title': 'The Experience of a Slave in South Carolina',
                        'volumes': ''},
 'tsvdro_ver': '1.0',
 'workflow': {'created_by': 'tsdro_reference_implementation',
              'created_date': '2018-08-02 13:50',
              'created_system': 'parergon.local',
              'token_count': 21533,
              'vocab_count': 2920}}

</pre>

We can 
