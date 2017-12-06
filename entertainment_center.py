import media
import fresh_tomatoes

# movie instances
gladiator = media.Movie("Gladiator",
                      "The Gladiator who defied an empire.",
                      "http://bit.ly/2jMcefw",
                      "https://www.youtube.com/watch?v=Q-b7B8tOAQU",
                      "2000")
the_bourne_identity = media.Movie("The Bourne Identity",
                      "He was the perfect weapon until he became the target.",
                      "http://bit.ly/2jdp1bz",
                      "https://www.youtube.com/watch?v=FpKaB5dvQ4g",
                      "2002")
fifty_first_dates = media.Movie("50 First Dates",
                      "Imagine having to win over the girl of your dreams... every friggin' day!",
                      "http://bit.ly/2BK2VFl",
                      "https://www.youtube.com/watch?v=H1SVxJZTgI4",
                      "2004")
forrest_gump = media.Movie("Forrest Gump", 
                      "Life is like a box of chocolates...you never know what you're gonna get.",
                      "http://bit.ly/2Ap66ns",
                      "https://www.youtube.com/watch?v=bLvqoHBptjg",
                      "1994")
the_equalizer = media.Movie("The Equalizer",
                      "What do you see when you look at me?",
                      "http://bit.ly/2noxU6o",
                      "https://www.youtube.com/watch?v=VjctHUEmutw",
                      "2014")
john_wick = media.Movie("John Wick",
                      "Don't set him off.",
                      "http://bit.ly/2ATbsIR",
                      "https://www.youtube.com/watch?v=2AUmvWm5ZDQ",
                      "2014")
wonder_woman = media.Movie("Wonder Woman",
                      "The future of justice begins with her.",
                      "http://bit.ly/2A2X1C1",
                      "https://www.youtube.com/watch?v=VSB4wGIdDwo",
                      "2017")
insidious = media.Movie("Insidious",
                      "It's not the House that's Haunted.",
                      "http://bit.ly/2Bx5cCx",
                      "https://www.youtube.com/watch?v=zuZnRUcoWos",
                      "2010")


# intances list
movies = [gladiator, the_bourne_identity, fifty_first_dates, forrest_gump, the_equalizer, john_wick, wonder_woman, insidious]

# generation of movie trailer website
fresh_tomatoes.open_movies_page(movies)