import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                         "A story of a boy and its toys that come to life",
                         "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                         "http://www.youtube.com/watch?v=vwyZH85NQC4",)

deadpool = media.Movie("Deadpool",
                       "Ex-Mercenary talks alot of shit to people that disfigured him, oh and kills them too",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=oCvLUxICxEI")

assasins_creed = media.Movie("Assasin's Creed",
                       "Enter the anymous and become your past",
                       "https://upload.wikimedia.org/wikipedia/en/a/a0/Assassin%27s_Creed_film_poster.jpg",
                       "https://www.youtube.com/watch?v=H6bbvf4nI4M")

rogue_one = media.Movie("Rogue One",
                       "A rebellion based on hope",
                       "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
                       "https://www.youtube.com/watch?v=Ze2kpOZx_kU")

suicide_squad = media.Movie("Suicide Squad",
                       "Sometimes a lot of bad can do a little good",
                       "https://upload.wikimedia.org/wikipedia/en/a/ac/Suicide_Squad_%28film%29_Poster.jpg",
                       "https://www.youtube.com/watch?v=BKMgB01MU-w")

#print(toy_story.storyline)
#deadpool.show_trailer()

#movies = [deadpool, assasins_creed, rogue_one, suicide_squad]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__name__)
