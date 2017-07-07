# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

narnia_tltwtw = media.Movie("The Chronicles of Narnia: The Lion, The Witch, and The Wardrobe",
                        "Peter, Susan, Edmund, and Lucy discover a wardrobe to travel in Narnia.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/10/The_Chronicles_of_Narnia_-_The_Lion%2C_the_Witch_and_the_Wardrobe.jpg/220px-The_Chronicles_of_Narnia_-_The_Lion%2C_the_Witch_and_the_Wardrobe.jpg",
                        "https://www.youtube.com/watch?v=lWKj41HZBzM")

# print toy_story.storyline

narnia_pc = media.Movie("The Chronicles of Narnia: Prince Caspian",
                    "The adventure of Prince Caspian that his uncle Miraz want to kill him.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c8/Principe_Caspain_poster.jpg/220px-Principe_Caspain_poster.jpg",
                    "https://www.youtube.com/watch?v=oZRZ-2et2uY")

# print avatar.storyline
# avatar.show_trailer()

narnia_tvotdt = media.Movie("The Chronicles of Narnia: The Voyage of The Dawn Treader",
                            "Three years after the events of Prince Caspian, Lucy and Edmund Pevensie are staying with their irritating bookworm cousin Eustace Scrubb until the war is over, separated from Peter and Susan Pevensie.",
                            "https://upload.wikimedia.org/wikipedia/en/d/d4/The_Voyage_of_the_Dawn_Treader_poster.jpg",
                            "https://www.youtube.com/watch?v=hrJQDPpIK6I")

# game_of_thrones.show_trailer()

hobbit_dos = media.Movie("The Hobbit: The Desolation of Smaug",
                            "Thorin Oakenshield and his company facing the Dragon Smaug.",
                            "https://upload.wikimedia.org/wikipedia/en/4/4f/The_Hobbit_-_The_Desolation_of_Smaug_theatrical_poster.jpg",
                            "https://www.youtube.com/watch?v=OPVWy1tFXuc")

hobbit_auj = media.Movie("The Hobbit: An Unexpected Journey",
                            "Bilbo Baggins starts journey to travel around the world.",
                            "https://upload.wikimedia.org/wikipedia/en/b/b3/The_Hobbit-_An_Unexpected_Journey.jpeg",
                            "https://www.youtube.com/watch?v=SDnYMbYB-nU")

hobbit_tbotfa = media.Movie("The Hobbit: The Battle of the Five Armies",
                            "After Bard killed the Dragon Smaug, Thorin refuses to share the treasures. Orc, Wargs, and Bats are the enemies that want to get all the treasures over Thorin.",
                            "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Hobbit_-_The_Battle_of_the_Five_Armies.jpg",
                            "https://www.youtube.com/watch?v=iVAgTiBrrDA")

movies = [narnia_tltwtw, narnia_pc, narnia_tvotdt, hobbit_dos, hobbit_auj, hobbit_tbotfa]
fresh_tomatoes.open_movies_page(movies)
# print media.Movie.VALID_RATINGS
# print media.Movie.__doc__
