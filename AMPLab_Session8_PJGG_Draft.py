
# coding: utf-8

# # Reading a subset of the provided dataset from last.fm

# Tag-cleanining.

# In[1]:

import re        
import csv
tags = {}
deleted = 0
with open('uptot2k.csv', 'r') as csvfile:  #Loading CSV file.
    filedataset = csv.reader(csvfile)
    for row in filedataset:
        mbid, track_tags = row[0], row[1:]
        if not ''.join(track_tags).strip():
            deleted+=1
            continue # ignore tracks with no tags
        tags[mbid] = []
        for i in range(len(track_tags)/2):
            if track_tags[i*2+1]>='0':
                tag = track_tags[i*2]
                tag = tag.lower()
                tag = re.sub(r'[^a-zA-Z0-9]','', tag) # remove non-alphanumeric symbols
                if tag != '':
                    tags[mbid].append(tag)
print "Number of final dataset elements: ",len(tags),"\n", "Number of deleted elements: ",deleted,"\n"
# let's see what we've got: 10 first values
for mbid in tags.keys()[:10]: 
    print "MusicBrainz ID ", mbid," Tags ", tags[mbid]


# Tag histogram in order to see which are the most frequent tags.

# In[2]:

all_tags = []
for mbid, track_tags in tags.iteritems():
    all_tags += track_tags
print "Total different tags:", len(set(all_tags))

# create a tag histogram
tags_hist = {}
for t in all_tags:
    tags_hist.setdefault(t, 0)
    tags_hist[t] += 1

# note this is VERY slow: 
tags_hist = dict((t, all_tags.count(t)) for t in all_tags)

# sort tags by occurrence frequency
import operator
sorted_tags_hist = sorted(tags_hist.items(), key=operator.itemgetter(1), reverse=True)

print "Top 100 tags:"
print sorted_tags_hist[:100]


# # Dataset creation based on mood tags

# Searching for tags related with mood: dictionary creation.

# In[3]:

str1 = str(sorted_tags_hist)   #CONVERTING DICT TO STRING
print str1 


# In[4]:

#Noun Phrase Extraction


from textblob import TextBlob


wiki = TextBlob(str1)
wiki.tags


# In[5]:

#Sentiment overall

testimonial = TextBlob(str1)
testimonial.sentiment
#Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857)
testimonial.sentiment.polarity


# In[6]:

print str1


# In[ ]:




# In[7]:

mydict = {}

best=0
awful=0
good=0
awesome=0
love=0
favourite=0

#add catchy

for i in range(len(tags.keys())):
    tags_per_row = tags[tags.keys()[i]]
    for j in tags_per_row:
        if j =='best':
            mydict[tags.keys()[i]] = 'best'
            best+=1
        if j =='awful': 
            mydict[tags.keys()[i]] = 'awful'
            awful+=1
        if j =='good': 
            mydict[tags.keys()[i]] = 'good'
            good+=1
        if j =='awesome': 
            mydict[tags.keys()[i]] = 'awesome' 
            awesome+=1
        if j =='love':
            mydict[tags.keys()[i]] = 'love'
            love+=1
        if j =='favourite': 
            mydict[tags.keys()[i]] = 'favourite'
            favourite+=1
print "Number of best : ", best,"\n", "Number of favourite : ",favourite,"\n", "Number of good  : ", good,"\n","Number of awesome : ", awesome,"\n", "Number of love : ", love,"\n"
#print "IDs: ", mydict.keys(),"\n", "Class: ", mydict.values(),"\n"
print "New dictionary length: ", len(mydict)






# In[8]:

str1 = str(mydict)   #CONVERTING DICT TO STRING

mydict2 = eval(str1)

print mydict==mydict2 #CONFIRMATION


# In[9]:

print str1


# In[ ]:




# In[ ]:




# #print mydict
# 
# def search(str1, lookup):
#     for key, value in str1.items():
#         for v in value:
#             if lookup in v:
#                 return key
# 
# import re
# counter = 0
# 
# for i in range(len(str1.values())):
#     for j in range(len(str1.values()[i])):
#         match=re.search(r'love', str1.values()[i][j])
# 
#         #print counter
#         if match:
#                  print match.group()
#                  counter=counter+1
# print "numero de matches para XxX", i
# print counter

# Dictionary to CSV file. This CSV will be evaluated on AcousticBrainz.

# myDict = {'age': ['12'], 'address': ['34 Main Street, Maryjasdasd, 212 First Avenue , Maryjox'],
#           'firstName': ['Alan', 'Mary-Ann'], 'lastName': ['Stone', 'Lee,Maryzas']}
# 
# def search(myDict, lookup):
#     for key, value in myDict.items():
#         for v in value:
#             if lookup in v:
#                 return key
# 
# #search(myDict, 'Mary')
# 
# import re
# for i in range(len(myDict.values())):
#     for j in range(len(myDict.values()[i])):
#         match=re.search(r'Mary', myDict.values()[i][j])
#          
#         if match:
#                  print match.group() #Mary
# print i
# 

# In[12]:

import csv 
writer = csv.writer(open('dict_700to705.csv', 'w'))
for key, value in mydict.items():
    key = key.replace('"', '')
    writer.writerow([key,value])
    print key, value


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



