import webbrowser

class Movie():
    """This class defines the attributes we will have for the movies on our website.

    Attributes:
        title: a string that holds the title of the movie.
        storyline: a string that comtains a short description of the plot.
        poster_image_url: a url to the movie poster image.
        trailer_youtube_url: a url to the youtube trailer.
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Initiates movie class with the following attributes."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens the youtube trailer when the movie poster is clicked on."""
        webbrowser.open(self.trailer_youtube_url)
