import media
import fresh_tomatoes

cars = media.movie("Cars",
                  "Its a Story of car getting lost and reliasing  a lot of things about life ",
                  "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
                  "https://youtu.be/SbXIj2T-_uk")

avatar = media.movie('Avatar',
                    'story of a marine being sent to an alien planet',
                    'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                    'https://youtu.be/5PSNL1qE6VY')

avengers_infinity_war= media.movie('Avengers Infinity War',
                                   "A alien hunting for ancient relic which can control the reailty as we know it while the Avengers try to stop him",
                                   "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                                   'https://youtu.be/6ZfuNTqbHE8')

Iron_man = media.movie("Iron Man",
                       "A billionair  man who  manufactures weapon  and then gets kidnapped by terrorist  but  escaped by  making a suit for himself",
                       'https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG',
                       'https://youtu.be/8hYlB38asDY')

batman_begins = media.movie('Batman Begins',
                     'A story of a child whose parents get killed in front of him and  becomes a crime fighting vigilanti  who serves justice and protect the city',
                     'https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg',
                     'https://youtu.be/vak9ZLfhGnQ')

movies = [cars, avatar, avengers_infinity_war, Iron_man, batman_begins]

fresh_tomatoes.open_movies_page(movies)
                     
                
