#
# conversion script to produce TSV-DRO (Data Rich Object) 
# for computational analysis in the humanities from
# DocSouth North American Slave Narrative archive
#
# James E. Dobson (james.e.dobson@dartmouth.edu)
# Dartmouth College
# http://www.dartmouth.edu/~jed
#

# load module
import tsvdro
import csv
import nltk
import os

docsouth_root = "../../na-slave-narratives/data/"
output_dir = "na-slave-narratives/"
neh_toc = docsouth_root + "toc.csv"

def preprocess(text_object, options = "default"):
        from nltk.corpus import stopwords
        stopwords = stopwords.words('english')

        # *step one* (default): drop to lowercase 
        pp_text = [word.lower() for word in text_object]

        # *step two* (default): remove non-alpha characters,
        # punctuation, and as many other "noise" elements as
        # possible. If dealing with a single character word,    
        # drop non-alphabetical characters. This will remove 
        # most punctuation but preserve many words containing
        # marks such as the '-' in 'self-emancipated'

        tmp_text=list()
        for word in pp_text:
                if len(word) == 1:
                        if word.isalpha == True:
                                tmp_text.append(word)
                else:
                        tmp_text.append(word)           

        pp_text = tmp_text
        tmp_text=list()

        # now remove leading and trailing quotation marks,      
        # hyphens and  dashes

        drop_list = [u'“'.encode('utf-8'),'"',u'”'.encode('utf-8'),'-','—']
        for word in pp_text:
                if word[0].encode('utf-8') in drop_list:
                        word = word[1:]
                if word[-1:].encode('utf-8') in drop_list:
                        word = word[:-1]
                # catch any zero-length words remaining
                if len(word) > 0:
                        tmp_text.append(word)

        pp_text = tmp_text

        # preprocessing function: preserve *ONLY* NLTK stopwords
        if options == "onlystop":
                pp_text = [word for word in pp_text if word in stopwords]
                return(pp_text)
       
        # *step three* (default): remove stopwords
        # enable an option for preserving stopwords
        if options != "nostop":
                # add additional stopwords, also containing some remainders from
                # tokenizing
                custom_stopwords="""like go going gone one said says would got still really get 's 'll n't"""
                stopwords += custom_stopwords.split()

                pp_text = [word for word in pp_text if word not in stopwords]
        
        return(pp_text)

#
# loop through input files
#


# create output directory
os.mkdir(output_dir)

row_count=0
with open(neh_toc, 'rt') as csvfile:
   reader = csv.reader(csvfile)
   for row in reader:
        # deal with the header
        if row_count != 0:

            print('processing:',row[0])
            file = docsouth_root + "texts/" + row[0].replace(".xml",".txt")
            tsvdro_object = dict()
            tsvdro_object['header'] = tsvdro.build_header()
            tsvdro_object['header']['bibliographic_data']['file_uri'] = row[5]
            tsvdro_object['header']['bibliographic_data']['author_name'] = row[1]
            tsvdro_object['header']['bibliographic_data']['title'] = row[2]

            # try to convert date to an integer (year)
            try:
                year=int(row[3])
            except ValueError:
                year=False
                pass

            tsvdro_object['header']['bibliographic_data']['publication_date'] = year

            # produce TSV token count
            raw_text = open(file,encoding="utf-8").read()
            tokens = nltk.word_tokenize(raw_text)
            text = nltk.Text(tokens)

            # update raw token count
            tsvdro_object['header']['workflow']['token_count']  = len(text)
            text = preprocess(text)

            # update vocab count
            tsvdro_object['header']['workflow']['vocab_count'] = len(set(text))
 
            # now build TSV
            tsvdro_object['data'] = dict()

            for token in set(text):
                tsvdro_object['data'][token] = text.count(token)                  

            output = output_dir + row[0].replace(".xml",".dro") 
            tsvdro.save(tsvdro_object,output)
        row_count += 1

print('processed',row_count)
