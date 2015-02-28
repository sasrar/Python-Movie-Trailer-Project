import media
import fresh_tomatoes

inception = media.Movie("Inception",
                        "A story of a boy and his toys that come to life",
                        "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM",
                        "Leonado Dicaprio,Joseph Gordon-Levitt")
the_dark_knight = media.Movie("The Dark Knight",
                        "A marine on an alien planet",
                        "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=yrJL5JxEYIw",
                        "Christian Bale, Heath Ledger")
the_matrix = media.Movie("The Matrix",
                        "A man goes back to school and impersonates a music teacher",
                        "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                        "Keanu Reeves, Laurence Fishburne")
up =        media.Movie("Up",
                        "A story of a mouse with chef aspriations",
                        "http://upload.wikimedia.org/wikipedia/en/0/05/Up_(2009_film).jpg",
                        "https://www.youtube.com/watch?v=qas5lWp7_R0",
                        "Edward Asner, Jordan Nagai")
zombieland = media.Movie("Zombieland",
                        "Romance in paris",
                        "http://www.sonypictures.com/movies/zombieland/assets/images/onesheet.jpg",
                        "https://www.youtube.com/watch?v=8m9EVP8X7N8",
                        "Jessie Eisenberg, Emma Stone")
kickass = media.Movie("Kick Ass",
                        "A post-apocalyptic tale about survival",
                        "http://ia.media-imdb.com/images/M/MV5BMTMzNzEzMDYxM15BMl5BanBnXkFtZTcwMTc0NTMxMw@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=mcKIMqRF5Gc",
                        "Aaron Taylor-Johnson, Nicolas Cage")

movies = [inception,the_dark_knight,the_matrix,up,zombieland,kickass]
fresh_tomatoes.open_movies_page(movies)
