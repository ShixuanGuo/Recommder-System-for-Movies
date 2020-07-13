# Recommder-System-for-Movies

## Part 1 Overview  
1. **Objective**  
The objective of this Recommender System is to recommend relevant movies for users, based on their preference.  
2. **Approach**  
  - **Popularity-based recommendation**  
  This model recommends to a user the most popular items that the user has not previously consumed. In the movie setting, we will recommend the movie that most users have liked and consumed. In other words, this system utilizes the "widom of the crowds." It usually provides good recommendations for most of the people. Since it is easy to implement, it can be used as a baseline.  
  - **Collaborative Filtering Recommendation**  
  This approach uses the memory of previous users interactions to compute users similarities based on items they've interacted (user-based approach) or compute items similarities based on the users that have interacted with them (item-based approach). Then recommend items those similar users liked, but the current user have not interacted yet.  
3. **Package**  
  `import pandas as pd`  

## Part 2 Getting started: Popularity-based recommendation
1. Read in the movie file using `[df, column_names, preference] = read_in_movie_preference()`.  
  It returns three items:  
    - A dictionary where the key is username and the value is a vector of (-1, 0, 1) that indicates the users preference across movies (in the order of the csv file).  
    - A list of strings that indicate the order of column names.  
    - A data frame that contains the csv file.  

2. Compute the ranking of most popular movies  
  Take the movie preference dataframe and computes the popular ranking of movies from the most popular to the least popular.  
  Return a list where each element represents the popularity ranking of the movies and the order of the list reflects the order of the movie names in the dataframe.  
  `movie_popularity_rank=movies_popularity_ranking(df)`  
  
3. Make recommendation  
  Recommend the top movie that this user has not watched and has best popularity ranking.  
  If the user name does not exit, return an empty string. If the user has watched all movies, return an empty string.  
  `recommended_movie=Recommendation(movie_popularity_rank, preference, movie_names, name)`  
  
## Part 3 Getting started: Collaborative Filtering Recommendation
1. Read in the movie file  
  `[df, column_names, preference] = read_in_movie_preference()`   
  
2. Compute the similarity of any two users.  
  In this model, I use Jaccard similarity. The Jaccard similarity of any two persons are equal to  
    <img src="https://render.githubusercontent.com/render/math?math=\frac{\text{Number of Movies both people like}}{\text{Number of Movies at least one person likes}}">  
    If there is no movie liked by either of the two persons, jaccard similarity is equal to 0.  
    To get Jaccard similiarity of two users, run  
    `js=jaccard_similarity(preference_1, preference_2)`  

3. Finding soulmates.  
  Given a person's name, find the person's movie soulmate.  
  Soulmate is defined as the other person who has the highest jaccard similarity that is less than 1 with the focal person. If there are multiple people having the same jaccard similarity with the focal person, pick the person with the smallest name.  
  `[soulmate, soulmate_preference, js] = Find_Soul_Mate(preference, "Target_name")`  
  Returns the soul mate name the movie preference of the soul mate, and the jaccard similarity score of the soul mate.  

4. Make recommendation.  
  Take the previous users' preference and a target name, recommend movies that the target person's soulmate has watched but the target person has not. If such movie does not exist, return an empty string. If exist, returns the movie names.  
  `Recommendation(preference, "target_name", column_names)`  
  
  
