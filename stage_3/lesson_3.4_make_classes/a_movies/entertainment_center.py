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

# game_of_thrones.show_trailer()

hobbit_dos = media.Movie("The Hobbit: The Desolation of Smaug",
                            "Thorin Oakenshield and his company facing the Dragon Smaug.",
                            "https://upload.wikimedia.org/wikipedia/en/4/4f/The_Hobbit_-_The_Desolation_of_Smaug_theatrical_poster.jpg",
                            "https://www.youtube.com/watch?v=OPVWy1tFXuc")

hobbit_auj = media.Movie("The Hobbit: An Unexpected Journey",
                            "Bilbo Baggins start his journey to travel around the world.",
                            "https://upload.wikimedia.org/wikipedia/en/b/b3/The_Hobbit-_An_Unexpected_Journey.jpeg",
                            "https://www.youtube.com/watch?v=SDnYMbYB-nU")

hobbit_tbotfa = media.Movie("The Hobbit: The Battle of the Five Armies",
                            "After Bard kille the Dragon Smaug, Thorin refuses to share the treasures. Orc, Wargs, and Bats are the enemies that want to get all the treasures over Thorin.",
                            "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Hobbit_-_The_Battle_of_the_Five_Armies.jpg",
                            "https://www.youtube.com/watch?v=iVAgTiBrrDA")

movies = [toy_story, avatar, game_of_thrones, hobbit_dos, hobbit_auj, hobbit_tbotfa]
# fresh_tomatoes.open_movies_page(movies)
print media.Movie.valid_ratings
