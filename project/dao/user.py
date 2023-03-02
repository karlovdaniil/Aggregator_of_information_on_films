from project.models import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_user_by_id(self, uid):
        return self.session.query(User).get(uid)

    def get_user_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, user_d):
        user = User(**user_d)

        self.session.add(user)
        self.session.commit()

        return user

    def update(self, user_d):
        user = self.get_user_by_id(user_d.get('id'))

        for k, v in user_d.items():
            setattr(user, k, v)

        self.session.add(user)
        self.session.commit()

    def delete(self, uid):
        user = self.get_user_by_id(uid)

        self.session.delete(user)
        self.session.commit()

