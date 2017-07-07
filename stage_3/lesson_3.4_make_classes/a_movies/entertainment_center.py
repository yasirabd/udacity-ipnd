# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/id/4/4c/Toy_Story_4_poster.jpg",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk")

# print toy_story.storyline

avatar = media.Movie("Avatar",
                    "A marine on an alien planet.",
                    "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# print avatar.storyline
# avatar.show_trailer()

game_of_thrones = media.Movie("Game of Thrones Season 7",
                            "After a summer lasting almost ten years, the words of House Stark have finally become reality once again: winter has come.",
                            "https://upload.wikimedia.org/wikipedia/en/0/04/Game_of_Thrones_Season_7.jpg",
                            "https://www.youtube.com/watch?v=giYeaKsXnsI")

game_of_thrones.show_trailer()

# movies = [toy_story, avatar]
# fresh_tomatoes.open_movies_page(movies)
