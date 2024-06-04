def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs, xy):
    cset = set()
    for x in xs:
        if x in xy:
            cset.add(x)
            
    return cset
    
        