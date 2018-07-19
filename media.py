import webbrowser
class movie():
    VALID_RATINGS=['G','PG','PG-13','R']
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title #title of the movie
        self.storyline = movie_storyline #movie plot
        self.poster_image_url = poster_image #poster of the movie
        self.trailer_youtube_url = trailer_youtube # trailer link of thhe youtub movie

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
