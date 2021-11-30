class BookRepository:
    def __init__(self, db):
        self._db = db

    def get_book(self, book):
        sql = "SELECT * FROM books WHERE title=:title"
        result = self._db.session.execute(sql, {"title": book._title})
        return result.fetchone()
    
    def add_book(self, book, user_id):
        try:
            sql = "INSERT INTO books (author, title, type, isbn, user_id) VALUES (:author, :title, book, :isbn, :user_id)"
            self._db.session.execute(sql, {"author": book._author, "title": book._title, "isbn": book._isbn, "user_id": user_id})
            self._db.session.commit()
            print("BookRepository add_book onnistui!")
            return True
        except:
            print("BookRepository add_book epäonnistui!")
            return False

    def get_users_books(self, user_id):
        try:
            sql = "SELECT * FROM books WHERE user_id=:user_id"
            result = self._db.session.execute(sql, {"user_id": user_id})
            return result.fetchall()
        except:
            return None