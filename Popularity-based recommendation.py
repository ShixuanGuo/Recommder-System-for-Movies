#!/usr/bin/env python
# coding: utf-8

# ## Popularity-based Recommendation
# In the movie setting, we will recommend the movie that most users have liked and consumed. In other words, this system utilizes the "widom of the crowds."

# ### 1. Read-in the movie file

# In[1]:


import pandas as pd
def read_in_movie_preference():
    file_location = "./data/movie_preference.csv"
    df = pd.read_csv(file_location)
    column_names = list(df.columns[1:])
    preference = {}
    
    for index, row in df.iterrows():
        name=row['Please fill in your name. (You can also use an alias name). ']
        preference[name]=list(row['The Shawshank Redemption':'Kingsman: The Secret Service'])
    
    return [df, column_names, preference]


# ### 2. Compute the ranking of most popular movies

# In[ ]:


def movies_popularity_ranking(df):
    '''
    Take the movie preference dataframe and computes the popular ranking of movies from the most popular to the least popular. 
    
    Parameter
    --------
    df: data frame
        input data frame includes previous users' preferences
    
    Return
    ------
    movie_popularity_rank: list
        a list where each element represents the popularity ranking of the movies,
        the order of the list reflects the order of the movie names in the dataframe
    '''
    
    score=df.sum(axis=0)[1:].reset_index()
    movie_popularity_rank=score[0].rank(ascending=False,method='min').values
    
    return movie_popularity_rank


# ### 3. Recommendation

# In[ ]:


def Recommendation(movie_popularity_rank, preference, movie_names, name):
    '''
    Recommend the top movie that this user has not watched and has best popularity ranking
    
    Parameters
    ---------
    movie_popularity_rank: list
        a list where each element represents the popularity ranking of the movies
    preference: dict
        the memory of previous users with their movie preference
    movie_names: list
        a list of all movies stored in the memory
    name: str
        name of target person
    
    Return
    ------
    recommendation_movie: str
        recommended movie name
        if the user name does not exit, return an empty string. 
        if the user has watched all movies, return an empty string.
    '''
    
    recommended_movie = ""
    
    if name in preference.keys():
        pref=preference[name]
        if sum(pref)<len(pref):
            rank=len(pref)
            for p,index in enumerate(pref):
                if p==0 and movie_popularity_rank[index]<rank:
                    rank=movie_popularity_rank[index]
                    i=index
            recommended_movie=movie_names[i]  
            
    return recommended_movie

