
import webbrowser

class Movie():
		""" 
		Movie Class Attributes:
		title: The title of the movie
		storyline: Movie tagline
		poster_image_url: URL location of the movie poster
		trailer_youtube_url: trailer URL in youtube
		year: year movie released
		"""
		def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, year):
			self.title = movie_title
			self.storyline = movie_storyline
			self.poster_image_url = poster_image
			self.trailer_youtube_url = trailer_youtube
			self.year = year

		def show_trailer(self):
			webbrowser.open(self.trailer_youtube_url)
