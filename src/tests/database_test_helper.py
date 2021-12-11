class Database_test_helper:
    def __init__(self, db):
        self._db = db

    def delete(self):
        self._db.session.execute("DELETE FROM users CASCADE")
        self._db.session.execute("DELETE FROM books CASCADE")
        self._db.session.execute("DELETE FROM podcasts CASCADE")
        self._db.session.execute("DELETE FROM blogs CASCADE")
        self._db.session.execute("DELETE FROM videos CASCADE")
        self._db.session.execute("DELETE FROM tags CASCADE")
        self._db.session.commit()
