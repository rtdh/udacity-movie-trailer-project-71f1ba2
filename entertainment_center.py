import fresh_tomatoes
import media

'''
Create eight movie objects / instances
initialising with 4 argument each:
title - Movie Title
storyline - A brief note on movie
poster_image - url to poster image
trailer_youtube - url to youtube trailer
'''
Jurassic_World = media.Movie(
    "Jurassic World", "The film is a sequel to \
    Jurassic World(2015)and is the fifth \
    installment of the Jurassic Park film series",
    "http://www.ednlnews.com/wp-content/uploads/2018/01/jurassic-2.jpg",
    "https://www.youtube.com/watch?v=NPv5UopHnj8")
Rampage = media.Movie(
    "Rampage Story", "Rampage is an upcoming \
    American science fiction monster film \
    directed by Brad Peyton",
    "http://www.ednlnews.com/wp-content/uploads/2018/01/Rampage-2.jpg",
    "https://www.youtube.com/watch?v=SaZNFH4OORg")

Harray_Potter = media.Movie(
    "Harray Potter", "Harry Potter and the Cursed Child \
    is a two-part West End stage play written by Jack Thorne",
    "http://www.ednlnews.com/wp-content/uploads/2018/01/Harry-4.gif",
    "https://www.youtube.com/watch?v=VPIOygtubEQ")

Babuabli2 = media.Movie(
    "Babuabli2",
    "A Story of Bahubali",
    "http://www.ednlnews.com/wp-content/uploads/2018/01/Bahubali-2.jpg",
    "https://www.youtube.com/watch?v=qD-6d8Wo3do")

Dangal = media.Movie(
    "Dangal",
    "Indian Hindi-language biographical sports drama film, \
    directed by Nitesh Tiwari",
    "http://www.ednlnews.com/wp-content/uploads/2018/01/dangal.jpg",
    "https://www.youtube.com/watch?v=x_7YlGv9u1g")

three_idiots = media.Movie(
    "Three Idiots",
    "The film is about the friendship of three students \
    at an Indian engineering college.",
    "http://www.ednlnews.com/wp-content/uploads/2018/01/3idiot-33-12x9.jpg",
    "https://www.youtube.com/watch?v=K0eDlFX9GMc")

titanic = media.Movie(
    "Titanic",
    "Titanic is a 1997 American epic romantic disaster movie. \
    It was directed, written, and co-produced by James Cameron. \
    The movie is about the 1912 sinking of the RMS Titanic",
    "http://www.ednlnews.com/wp-content/uploads/2018/01/titanic.jpg",
    "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

Sachin_A_Billion_Dream = media.Movie(
    "Sachin: A Billion Dream",
    "Sachin: A Billion Dreams is a 2017 Indian  \
    docudrama-biographical film directed by James Erskine",
    "http://www.ednlnews.com/wp-content/uploads/2018/01/sachin.jpg",
    "https://www.youtube.com/watch?v=8gTeE6pa4Kg")

# Store the Movie objects in a list.
movies = [
    Jurassic_World, Rampage, Harray_Potter,
    Babuabli2, Dangal, three_idiots, titanic,
    Sachin_A_Billion_Dream]

# call movie trailer page method and pass movies array
fresh_tomatoes.open_movies_page(movies)
