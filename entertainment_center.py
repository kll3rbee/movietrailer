import media
import fresh_tomatoes
'''
Gladiator (2000)
R | 2h 35min | Action, Adventure, Drama | 5 May 2000 (USA) 8.5

The Bourne Identity (2002)
PG-13 | 1h 59min | Action, Mystery, Thriller | 14 June 2002 (USA) 7.9

50 First Dates (2004)
PG-13 | 1h 39min | Comedy, Romance | 13 February 2004 (USA) 6.8

Forrest Gump (1994)
PG-13 | 2h 22min | Drama, Romance | 6 July 1994 (USA) 8.8

The Equalizer (2014)
R | 2h 12min | Action, Crime, Thriller | 26 September 2014 (USA) 7.2

John Wick (2014)
R | 1h 41min | Action, Crime, Thriller | 24 October 2014 (USA) 7.3

Wonder Woman (2017)
PG-13 | 2h 21min | Action, Adventure, Fantasy | 2 June 2017 (USA) 7.6

Insidious (2010)
PG-13 | 1h 43min | Horror, Mystery, Thriller | 1 April 2011 (USA) 6.8
'''
# movie instances
gladiator = media.Movie("Gladiator",
                      "The Gladiator who defied an empire.",
                      "http://bit.ly/2jMcefw",
                      "https://www.youtube.com/watch?v=Q-b7B8tOAQU")
the_bourne_identity = media.Movie("The Bourne Identity",
                      "He was the perfect weapon until he became the target.",
                      "http://bit.ly/2jdp1bz",
                      "https://www.youtube.com/watch?v=FpKaB5dvQ4g")
fifty_first_dates = media.Movie("50 First Dates",
                      "Imagine having to win over the girl of your dreams... every friggin' day!",
                      "http://bit.ly/2BK2VFl",
                      "https://www.youtube.com/watch?v=H1SVxJZTgI4")
forrest_gump = media.Movie("Forrest Gump", 
                      "Life is like a box of chocolates...you never know what you're gonna get.",
                      "http://bit.ly/2Ap66ns",
                      "https://www.youtube.com/watch?v=bLvqoHBptjg")
the_equalizer = media.Movie("The Equalizer",
                      "What do you see when you look at me?",
                      "http://bit.ly/2noxU6o",
                      "https://www.youtube.com/watch?v=VjctHUEmutw")
john_wick = media.Movie("John Wick",
                      "Don't set him off.",
                      "http://bit.ly/2ATbsIR",
                      "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")
wonder_woman = media.Movie("Wonder Woman",
                      "The future of justice begins with her.",
                      "http://bit.ly/2A2X1C1",
                      "https://www.youtube.com/watch?v=VSB4wGIdDwo")
insidious = media.Movie("Insidious",
                      "It's not the House that's Haunted.",
                      "http://bit.ly/2Bx5cCx",
                      "https://www.youtube.com/watch?v=zuZnRUcoWos")


# intances list
movies = [ gladiator, the_bourne_identity, fifty_first_dates, forrest_gump, the_equalizer, john_wick, wonder_woman, insidious]

# Generate a web page that displays the movies in the list
fresh_tomatoes.open_movies_page(movies)