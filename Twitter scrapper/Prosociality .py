# Objective: Perform text analysis to study the degree of prosociality.


import pandas as pd
import re
import os

# Prepare the dictionary of text files
biglist = {}
files = [f for f in os.listdir('C:\\Text_files')  ]
print ("I found these many files", files)
for fileName in files:
    file = open('C:\\Text_files\\'+fileName)
    print(fileName)
    listOfWords=re.sub("[^\w]", " ",  file.read().lower()).split()
    biglist[fileName] = listOfWords
    file.close()

# The prosocial list, will be copied
prosocial = ["accepting", "accommodat*", "affect*" ,"agreeable*", "aid*", "altruis*", "appreciat*", "approachable", "assist*", "benefit*",
             "benevolen*", "biodivers*", "care", "caring", "charit*", "collective*", "commun*", "compassion*", "compliment", "concern*",
             "confide", "conscien*", "conservation*","considerate", "contribut*","cooperat*", "cope*", "coping", "courteous*", "courtesy", "defend*",
             "dependab*","dignity", "donat*", "earth", "ecolog*", "education*", "egalitar*", "empath*", "empower*","encourag*", "environment*",
             "equal*", "ethic*", "everybod*", "everyone*", "facilitat*", "fair*", "forgiv*", "freed*", "genero*", "gentle*", "genuin*", "giv*",
             "goodhearted*", "greater good", "guard*", "harmon*", "help*", "helpful*", "honest*", "honorable", "honourable", "hospit*", "human*",
             "impartial*", "inspiring", "integrat*", "integrity", "interact*", "invit*", "involv*", "justice", "kids", "kindness", "listen*", "loyal*",
             "moral*", "NGO*", "nice*", "nonjudgmental", "nonprofit*", "not for profit*", "nurtur*", "peace*", "philanthrop*", "prais*", "prejud*",
             "protect*", "reciproc*", "relia*", "relied", "rely", "respectful*", "responsib*", "responsiv*", "righteous*", "rights", "role model*",
         "selfless*", "sensitiv*", "serv*", "share*", "shari*", "shield*", "sincer*", "societ*", "solidarit*", "support*", "sustainab*", "sympath*",
             "taught", "teach*", "team*", "tender*", "the people", "therap*", "thoughtful*", "tolera*", "trust*", "tutor*","underst*", "universal*",
             "unprejudiced", "upright", "virtuous*", "volunteer*"]

# Make a dictionary from prosocial.
bigdataframe_prior = {i:0 for i in prosocial}

# From dictionary to dataframe, where prosocial keys are indexes.
bigdataframe = pd.DataFrame.from_dict(bigdataframe_prior, orient = "index")

firmnames = []

for filename, wordslist in biglist.iteritems():
    my_dict =  {i:0 for i in prosocial} # make a dictionary of every prosocial word
    dict_density = {i:0 for i in prosocial}
    for k in wordslist:
        for key in my_dict:
            if key.endswith("*"):
                key_changed = key[:-1] # Removes * from the word
                if k.startswith(key_changed):
                    my_dict[key] =  1 + my_dict[key]  #square bracket to update value related to the key
                    dict_density[key] = (float(100*(float(my_dict[key]))/(float(len(wordslist))))) #update value of the density

            else:
                count = wordslist.count(key) # count number of times the key is present in the wordlist
                my_dict[key] = count
                dict_density[key] = (float(100*((float(count))/(float(len(wordslist))))))

    #Add word count to the dataframe
    df = pd.DataFrame.from_dict(my_dict, orient = "index")
    bigdataframe = pd.concat([bigdataframe, df], axis=1)

    #Add density to the dataframe
    df = pd.DataFrame.from_dict(dict_density, orient = "index")
    bigdataframe = pd.concat([bigdataframe, df], axis=1)


    firmnames.append(filename)


print (firmnames)









# In[ ]:


print (bigdataframe)


# In[ ]:


bigdataframe.to_excel('testsocial.xls',  encoding='utf-8')


# In[ ]:


bigdataframe.to_csv('testsocial.csv',  encoding='utf-8')
