# Projects
***
This folder contains different projects which I have done in order to practice newly learnt coding and data analysis related stuff. Over time, the number of files here will increase. The following subsections, named after the respective file names, elaborate on the nature of each project.

## dictTrainerProg.py
A (tiny) dictionary trainer program, most of which was coded during a single morning, and the first mini-program I have ever written. Functionalities include:
* Vocab practice mode: word is shown, user prompted to enter translation, feedback given. If answer was correct, word is dropped from the practice round, otherwise it will be shown again.
* Vocab test mode: same as above, but if the user entered the wrong translation, (s)he gets no 2nd chance to get it right. At the end, a test result is shown.
* Viewing, adding and deleting vocab. Changes to the vocab (as well as previous fails) are recorded and written to file prior to the user exiting the program.
* User input validation provided to avoid breakdowns.

## imdbDataProj.py (and sampleJsonMovieRequest.txt)
A small automated program which uses the IMDB API to first obtain a movie's respective imdb ID and then requests JSON formatted data on that movie, extracting the data of interest and putting it into a DF. Please note the following: 
* Movie names have been extracted from another dataset, [Grouplens](https://grouplens.org/datasets/movielens/latest/), in order to use them in the API requests. The data was cleaned and shuffled beforehand (since it was sorted by year and API requests on Imdb are limited to 100 a day on a free account). Moreover, two columns were added: movie_id (still NaN, to be obtained via program) and dataObtained (0/1). The result is a DF object named movieRequest
* The program was written to work as a program in the sense that, upon running imdbDataProj.py, it checks whether it has been run before and if this is not the case, a file is loaded and some objects are generated and written to another file. One of these objects, the DF to be used to store the extracted data, is constructed directly from a sample Imdb JSON type dictionary (to show the code and possible be able to make changes, such as which data is to be extracted). BOTH THE movieRequest AND THE sampleJsonDfConstruction OBJECTS ARE STORED IN sampleJsonMovieRequest.txt. IN ORDER TO RUN SUCCESSFULLY for the first time, both the imdbDataProj.py and the sampleJsonMovieRequest.txt files must be located in your WD.
* This is the first part of three concerning this project. In the second part, the DF's data will be cleaned and then fed into a PostgreSQL DB. In the third part, a program will be written to facilitate users to query the DB.
* My API key has (obviously) been removed from the url strings. To test the program, introduce your own Imdb API key into the URL strings (place is marked with ***).

## 
