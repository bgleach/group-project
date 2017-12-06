from flask_script import Manager
from base import app, db, Director, Film


manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    director1 = Director(name='Ang Lee', age=63, gender='Male')
    director2 = Director(name='Christopher Nolan', age=47, gender='Male')
    director3 = Director(name='Kathryn Bigelow', age=66, gender='Female')
    film1 = Film(name='Dunkirk', year=2017, description="In May 1940, Germany advanced into France, trapping Allied troops on the beaches of Dunkirk. Under air and ground cover from British and French forces, troops were slowly and methodically evacuated from the beach using every serviceable naval and civilian vessel that could be found. At the end of this heroic mission, 330,000 French, British, Belgian and Dutch soldiers were safely evacuated.", director=director1)
    film2 = Film(name="Harry Potter and the Philosopher's Stone", year=2001, description="Adaptation of the first of J.K. Rowling's popular children's novels about Harry Potter, a boy who learns on his eleventh birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. He is summoned from his life as an unwanted child to become a student at Hogwarts, an English boarding school for wizards. There, he meets several friends who become his closest allies and help him discover the truth about his parents' mysterious deaths.")
    film3 = Film(name="The Shawshank Redemption", year=1994, description="Andy Dufresne (Tim Robbins) is sentenced to two consecutive life terms in prison for the murders of his wife and her lover and is sentenced to a tough prison. However, only Andy knows he didn't commit the crimes. While there, he forms a friendship with Red (Morgan Freeman), experiences brutality of prison life, adapts, helps the warden, etc., all in 19 years.")
    db.session.add(director1)
    db.session.add(director2)
    db.session.add(director3)
    db.session.add(film1)
    db.session.add(film2)
    db.session.add(film3)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
