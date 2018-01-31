''' importing webbrowser module'''
import webbrowser


class Movie():
    ''' Class for representing a movie'''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):

        ''' Inits a Movie Object
        Args:

        title = a string of the movie's title
        storyline = a string about the movie
        poster_image = URL to a poster image
        trailer_youtube = youtube URL of the movie '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):

        ''' Opens trailer in a web browser '''
        webbrowser.open(self.trailer_youtube_url)

