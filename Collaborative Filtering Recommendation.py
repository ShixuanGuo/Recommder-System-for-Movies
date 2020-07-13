#!/usr/bin/env python
# coding: utf-8

# ## Collaborative Filtering Recommendation
# Find top-N similar users for a users and recommend items those similar users liked to the current user

# In[ ]:


import pandas as pd


# ### 1. Read-in the movie file

# In[ ]:


def read_in_movie_preference():
    file_location = "./data/movie_preference.csv"
    df = pd.read_csv(file_location)
    column_names = list(df.columns[1:])
    preference = {}
    
    for index, row in df.iterrows():
        name=row['Please fill in your name. (You can also use an alias name). ']
        preference[name]=list(row['The Shawshank Redemption':'Kingsman: The Secret Service'])
    
    return [df, column_names, preference]
[df, column_names, preference] = read_in_movie_preference()


# ### 2. Similarity

# In[ ]:


def jaccard_similarity(preference_1, preference_2):
    '''
    calculate the jaccard_similarity of two users
    Parameters
    ----------
    
    preference_1: list
        a list of moive preferences of user 1
    preference_2: list
        a list of moive preferences of user 2
    
    Return
    ------
    js: float
        jaccard similarity score of user 1 and user 2
    '''
    
    js = 0
    both=0
    at_least=0
    
    for i in range(len(preference_1)):
        if preference_1[i]==1 or preference_2[i]==1:
            if preference_1[i]==1 and preference_2[i]==1:
                both+=1
                at_least+=1
            else:
                at_least+=1
    js=both/at_least
    
    return js


# ### 3. Finding Soulmates

# In[ ]:


def Find_Soul_Mate(preference, name):
     '''
    find the user among all users who has the highest jaccard similarity that is less than 1 with the focal person
    pick the person with the smallest name, sorting names in the ascending order
    
    Parameters
    ----------
    
    preference: dict
        the memory of previous users with their movie preference
    name: str
        name of target person
    
    Return
    ------
    soulmate: str
        name of previous user who has the highest jaccard similarity score with the focal person
    soulmate_preference: list
        the memory of previous user's movie preference
    max_js: float
        the highest jaccard similarity score of previous user with the focal person
    '''

    soulmate_preference = []
    soul=[]
    max_js = 0
    
    target_preference=preference[name]
    for potential_soul in preference:
        soulmate_preference=preference[potential_soul]
        js=jaccard_similarity(target_preference, soulmate_preference)
        if js==max_js and js<1:
            soul.append(potential_soul)
        elif js>max_js and js<1:
            soul=[potential_soul]
            max_js=js
    if len(soul)>1:
        soul.sort()
        soulmate=soul[0]
    else:
        soulmate=soul[0]
    soulmate_preference=preference[soulmate]
    
    return [soulmate, soulmate_preference, max_js]


# ### 4. Recommendation

# In[ ]:


def Recommendation(preference, name, movie_names):
    '''
    Recommend all the movies this person's soulmate has watched but this person has not
    
    Parameters
    ---------
    preference: dict
        the memory of previous users with their movie preference
    name: str
        name of target person
    movie_names: list
        a list of all movies stored in the memory
    
    Return
    ------
    recommendation: list
        a list of recommended movie names. If such movie does not exist, return an empty string. If it exists, returns the name of the movie.
    '''
    recommendation = []

    [soulmate, soulmate_preference, js] = Find_Soul_Mate(preference, name)
    target_pre=preference[name]
    index=[]
    exist=False
    for i in range(len(target_pre)):
        if soulmate_preference[i]==1 and target_pre!=1:
            index+=i
            exist=True
    if exist:
        recommendation=movie_names[i for i in index]
    
    return recommendation

