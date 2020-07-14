import pandas as pd
[df, column_names, preference] = read_in_movie_preference()
target='Jack'

# 1. Popularity-based recommendation

movie_popularity_rank=movies_popularity_ranking(df)
movies=Recommendation(movie_popularity_rank, preference, column_names, target)
print(movies)


# 2. Collaborative filtering recommendation

movies=Recommendation(preference, target , column_names)
print(movies)
