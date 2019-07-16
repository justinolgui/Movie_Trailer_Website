import fresh_tomatoes
import media

the_hangover = media.Movie("The hangover",
                        "Storyline",
                        "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
                        "https://www.youtube.com/watch?v=tcdUhdOlz9M")

the_dark_knight = media.Movie("The Dark Knight",
                        "Storyline",
                        "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

interstellar = media.Movie("Interstellar",
                        "Storyline",
                        "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                        "https://www.youtube.com/watch?v=zSWdZVtXT7E")

saw = media.Movie("Saw",
                        "Storyline",
                        "https://upload.wikimedia.org/wikipedia/en/8/8f/Saw_film_logo.png",
                        "https://www.youtube.com/watch?v=S-1QgOMQ-ls")

it = media.Movie("It",
                        "Storyline",
                        "https://upload.wikimedia.org/wikipedia/en/5/5a/It_%282017%29_poster.jpg",
                        "https://www.youtube.com/watch?v=hAUTdjf9rko")

the_wolf_of_wall_street = media.Movie("The Wolf of Wall Street",
                        "Storyline",
                        "https://upload.wikimedia.org/wikipedia/en/d/d8/The_Wolf_of_Wall_Street_%282013%29.png",
                        "https://www.youtube.com/watch?v=iszwuX1AK6A")

silence_of_the_lambs = media.Movie("Silence of the Lambs",
                     "A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer",
                     "https://images-na.ssl-images-amazon.com/images/I/410VHPrwUPL.jpg",
                     "https://www.youtube.com/watch?v=W6Mm8Sbe__o")


movies = [the_hangover, the_dark_knight, interstellar, saw, it, the_wolf_of_wall_street, silence_of_the_lambs]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__module__)
