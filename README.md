Prototype format for data-rich humanities objects

This file defines the header and data objects for the TSV-DRHO (Tab Separated
Values - Data-Rich Humanities Object) proposed standard for data sharing.
 
This Python package provides high-level format-independent access to humanities
data for computational purposes.  

Created by Jed Dobson (James.E.Dobson@Dartmouth.EDU) 08/02/2018


- - -

'DRO' is a Data Rich Object (a named borrowed from Katherine Bode--see "The
Equivalence of 'Close' and 'Distant' Reading; Or, Toward a New Object for
Data-Rich Literary History." _Modern Language Quarterly_ 78.1 (2017)) and
attached to the commonly used tab-separated value data favored by many scholars
working on computational methods in the humanities.

It was inspired by data formats and metadata used in several other fields,
including neuroimaging and the [NIfT-T1](https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1.h) data format.

Several discussions on Twitter have also contributed to the design.


- - - 

<h2> Contributing? </h2>

Create a Pull Request!! What header fields are missing? What other types of data
need to be stored? How can we better support the community working on
computational methods for humanities data?


- - - 

<h2>Why use this??</h2>

- Capture and share critical bibliographic metadata.

- Record workflow information (what produced this file? when was it produced?) necessary for reproduction and replication.

- Store data and metadata together in a single, platform-agnostic format (JSON).

- Provide a standard interface for loading and saving data for computational applications.

- - - 

<h2> Using TSVDRO </h2>

Simple display of JSONified object:

<pre>
>>> from tsvdro import tsvdro
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
 'workflow': {'created_by': 'tsvdro_reference_implementation',
              'created_date': '2018-08-02 13:50',
              'created_system': 'parergon.local',
              'token_count': 21533,
              'vocab_count': 2920}}

</pre>

We can easily directly access token counts:

<pre>
>>> dro_object['data']['cotton']
34
</pre>

Files can be loaded, modified, and then saved:

<pre>
>>> dro_object['header']['workflow']['created_by'] = 'Jed Dobson'
>>> tsvdro.save(dro_object,'na-slave-narratives-dro/fpn-jackson-jackson.dro')
</pre>


Already have TSV files and want to convert them? It's trivial--the script will
create a header, convert your TSV data to a dictionary, and wrap the whole
thing up in JSON.

<pre>
>>> from tsvdro import tsvdro
>>> dro_object = tsvdro.load('existing-data-file.tsv')
Not in DRO format: converting
>>> dro_object['header']
{'bibliographic_data': {'publisher_location': '', 'file_uri': '', 'publisher': '', 'author_name': '', 'volumes': '', 'publication_date': '', 'pages': '', 'title': ''}, 'tsvdro_ver': '1.0', 'workflow': {'vocab_count': '', 'created_by': 'tsdro_reference_implementation', 'token_count': '', 'created_system': 'parergon.local', 'created_date': '2018-08-02 14:24'}}
>>> tsvdro.save('dro_object','updated-data-file.dro')
</pre>

<h2> Example: Calculating Distance Between Texts</h2>

Storing CountVectorizer objects (for example, as pickled objects) isn't as
portable as raw token counts. You can easily vectorize the stored values from a
TSV file by converting the list of tokens to a single string and including all
repetitions of included words and then supplying these strings to the
vectorizer.

<pre>
def unpack_text(input_object):
   expanded_doc = list()
   for key in input_object['data']:
      expanded_doc.append([key] * input_object['data'][key])
   return(' '.join([item for list in expanded_doc for item in list]))
</pre>

This [Jupyter notebook](https://github.com/jeddobson/tsvdro/blob/master/sample/vector-distance-matrix-using-tsvdro.ipynb) demonstrates the above method.


---

Bundled simple command-line utility dumps header of 'DRO' files:

<pre>
[jed@dexter bin] > ./tsvdro  ../sample/na-slave-narratives/neh-norris-norris.dro 
tsvdro_ver          : 1.0
created_date        : 2018-08-06 12:21
data_option         : None
token_count         : 42211
created_system      : parergon.local
last_updated        : 2018-08-06 12:21
data_type           : 1
vocab_count         : 5393
created_by          : tsvdro_reference_implementation
publisher           : None
publication_date    : 1789
author_name         : Robert  Norris
file_uri            : http://docsouth.unc.edu/full-text/na-slave-narratives/data/texts/neh-norris-norris.txt
publisher_location  : None
pages               : None
volumes             : None
title               : Memoirs of the Reign of Bossa Ahadee, King of Dahomy, an Inland Country of Guiney. To Which Are Added, the Author's Journey to Abomey, the Capital; and a Short Account of the African Slave Trade
</pre>
