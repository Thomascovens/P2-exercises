def title_to_director(movies):
    return {movie.title: movie.director for movie in movies}


def director_to_titles(movies):
    director_movies = {}

    for movie, info in movies.items():
        director = info[director]
        if director not in director_movies:
            director_movies[director] = []

    director_movies.append(movie)
    return director_movies
