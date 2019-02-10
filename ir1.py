

#Name- Manali Walke
#NET ID- mwalke25


import os,string
from nltk import PorterStemmer
from nltk.corpus import stopwords

directory="citeseer"

# In[8]:


def tokenize(contents):
    table = str.maketrans({key: None for key in string.punctuation})
    contents = contents.translate(table) 
    contents=contents.lower()
    contents=contents.split()
    return contents


# In[9]:


def parse():
    
    for filename in os.listdir(directory):
        file=directory+'/'+filename
        f = open(file, 'r')
        contents=f.read()
        tokens=tokenize(contents)
        for val in tokens:
            word_list.append(val)
            if val in word_dict:
                word_dict[val]+=1
            else:
                word_dict[val]=1
        f.close()


# In[10]:


def porter_stemmer():
    stemmer = PorterStemmer()
    for i in word_list:
        if i not in stopwords:
            val=stemmer.stem(i)
            ps_list.append(val)
            if val in ps_dict:
                ps_dict[val]+=1
            else:
                ps_dict[val]=1


# In[11]:


def stats(sorted_val, max_unique_number):
    common=[]
    total_achieved=0
    unique_count=0
    for i in range(20):
        print(sorted_val[i])
        if sorted_val[i][0] in stopwords:
            common.append(sorted_val[i])
    for i in range(len(sorted_val)):
        if total_achieved<max_unique_number:
            total_achieved+=sorted_val[i][1]
            unique_count+=1
    print("\nFrom these top 20 words, the stop words are:")
    for i in common:
        print(i)
    print("Number of stop words in top 20 words: ",len(common))
    print("Minimum number of unique words accounting for 15% of the total number of words in the collection: ",unique_count)


# In[12]:


stopwords = set(stopwords.words('english')) 
word_list=[]
word_dict={}

ps_list = []
ps_dict = {}

parse()
print("Total number of words in the collection: ",len(word_list))
print("Vocabulary size: ",len(word_dict))
print("\nTop 20 words with highest frequencies are:")
normal_sorted_val=sorted(word_dict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
max_unique_number = 0.15*len(word_list)

stats(normal_sorted_val, max_unique_number)

print("\nAfter Stemming and stop words removal\n")
porter_stemmer()
print("Total number of words in the collection after stemming and stop words removal are: ",len(ps_list))
print("Vocabulary size after stemming and stop words removal: ",len(ps_dict))
print("\nTop 20 words with highest frequencies after stemming and stop words removal:")
ps_sorted_val=sorted(ps_dict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
max_unique_number = 0.15*len(ps_list)
stats(ps_sorted_val,max_unique_number)

