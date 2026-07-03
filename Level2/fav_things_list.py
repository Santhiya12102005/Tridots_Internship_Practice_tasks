movie = ['Batman','Ironman','Avengers','Deadpool','Spiderman']
print("Movie list is:\n",movie)
movie.append('The Dark Knight')
print("Movie list after the insertion:\n",movie)
movie.pop(1) # or del movie[1]
print("Movie list after the remove(2nd position):\n",movie)
movie.sort()
print("Movies in Alphabetical order:\n",movie)