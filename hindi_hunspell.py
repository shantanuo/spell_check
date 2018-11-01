
# coding: utf-8

# In[64]:


get_ipython().system('wget https://raw.githubusercontent.com/Shreeshrii/hindi-hunspell/master/Hindi/hi_IN.dic')


# In[195]:


with open('hi_IN1.dic', 'w') as nf:
    with open('hi_IN.dic') as f :
        for l in f:
            l = l.rstrip()
            try:
                tags = l.split('/')[1]
            except IndexError:
                nline= l 
            else:
                ntags=''.join(sorted(tags))
                nline= l.split('/')[0] + '/' + ntags
            nf.write(nline+'\n')


# In[203]:


from collections import defaultdict
import nltk
myl=defaultdict(list)


# In[204]:


with open('hi_IN1.dic') as f :
    for l in f:
        l = l.rstrip()
        try:
            tags = l.split('/')[1]
            ntags=''.join(sorted(tags))
            myl[ntags].append(l.split('/')[0])
            for t in tags:
                myl[t].append( l.split('/')[0])
            bigrm = list(nltk.bigrams([i for i in tags]))
            nlist=[x+y for x, y in bigrm]
            for t1 in nlist:
                t1a=''.join(sorted(t1))
                myl[t1a].append(l.split('/')[0])
        except:
            pass


# In[205]:


len(myl.keys())


# In[213]:


sorted(list(myl.keys()))


# In[219]:


import string
mylist=list()
for c in string.punctuation:
    mylist.append(c)


# In[223]:


for c in string.ascii_letters:
    mylist.append(c)


# In[224]:


for c in string.digits:
    mylist.append(c)


# In[230]:


myd=dict()
myn=dict()
for i in mylist:
    myd[i] = myl[i]
    myn[i] = len(myl[i])


# In[231]:


len(myd.keys())


# In[233]:


myn


# In[238]:


sorted(myn.items(), key=lambda kv: kv[1])


# In[239]:


get_ipython().system(" grep 'b' hi_IN.dic")

