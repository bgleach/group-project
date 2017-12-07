# group-project
Our project is a movie database that involves two tables:
  1. Film
  2. Director

A director can be involved with many films, but a film can only be associated with one director (One-to-many relationship).

The columns for the Film table will be:
  1. FilmID, Name, Year, Director, and Description


  FilmID # | Name |Year | Director | Description
  ------ | ----------|-----|------|-------
  1|	*Dunkirk*	| 2017 | Ang Lee | In May 1940, Germany advanced into France, trapping Allied troops on the beaches of Dunkirk. Under air and ground cover from British and French forces, troops were slowly and methodically evacuated from the beach using every serviceable naval and civilian vessel that could be found. At the end of this heroic mission, 330,000 French, British, Belgian and Dutch soldiers were safely evacuated.
  2|	*Harry Potter and the Philosopher's Stone*|2001|Christopher Nolan |Adaptation of the first of J.K. Rowling's popular children's novels about Harry Potter, a boy who learns on his eleventh birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. He is summoned from his life as an unwanted child to become a student at Hogwarts, an English boarding school for wizards. There, he meets several friends who become his closest allies and help him discover the truth about his parents' mysterious deaths.
  3|	*The Shawshank Redemption*|1994	|Kathryn Bigelow | Andy Dufresne (Tim Robbins) is sentenced to two consecutive life terms in prison for the murders of his wife and her lover and is sentenced to a tough prison. However, only Andy knows he didn't commit the crimes. While there, he forms a friendship with Red (Morgan Freeman), experiences brutality of prison life, adapts, helps the warden, etc., all in 19 years.


  The columns for the Director table will be:
    1. ID, Name, Age，Gender


  ID # | Name |Age | Gender
  ------ | ----------|-----|------
  1|	*Ang Lee*	| 63 | Male
  2|	*Christopher Nolan*|47|Male
  3|	*Kathryn Bigelow*|66|Female

In order to run our application:
  1. Pull file from GitHub
  2. Open GIT command
  3. Locate file location
  4. run the following lines:
    pip install virtualenv
    install -r requirements.txt
    venv\Scripts\activate
    python manage.py deploy
    python manage.py runserver -d 
