def movies_from_year(movies, year):
    return[movie.title for movie in movies if movie.year == year]

def movies_with_actor(movies, actor):
    return[movie.title for movie in movies if movie.actor == actor]

def divisors(n):
    return[n for i in range(n) if i%2]