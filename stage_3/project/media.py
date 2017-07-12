# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie(object):
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_story_line, poster_image, trailer_youtube):
        """
        Initialize instance of class Movie.
        Arguments:
        movie_title: title of the movie
        movie_story_line: storyline of the movie
        poster_image: image of the poster movie
        trailer_youtube: video trailer of the movie
        '''
        Returns:
        None
        """
        self.title = movie_title
        self.storyline = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Open trailer youtube video in browser.
        Arguments:
        None
        '''
        Returns:
        Open browser that contains url youtube video and play it.
        """
        webbrowser.open(self.trailer_youtube_url)
