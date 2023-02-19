from project.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self, filters):
        page = filters.get('page')
        directors = self.session.query(Director)
        return directors.paginate(page=page).items

    def create(self, director_d):
        director = Director(**director_d)
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, did):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()
