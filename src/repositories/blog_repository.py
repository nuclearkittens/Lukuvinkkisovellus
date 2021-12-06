from sqlalchemy import exc


class BlogRepository:
    def __init__(self, db):
        self._db = db

    def add_blog(self, blog, user_id):
        """
        Adds Blog-object to database and links it to current user with id.

        Args:
            blog (blog): blog-object to be added
            user_id (Integer): Id of the user adding the blog.

        Returns:
            Boolen: True if successful.
        """
        try:
            author = blog.get_author()
            title = blog.get_title()
            url = blog.get_url()
            description = blog.get_description()
            sql = "INSERT INTO blogs (author, title, url, description, type, user_id, marked_read) \
                    VALUES (:author, :title, :url, :description, 'Blog', :user_id, NULL)"
            self._db.session.execute(
                sql, {"author": author, "title": title, "url": url, "description": description, "user_id": user_id})
            self._db.session.commit()
            return True
        except:
            return False

    def mark_finished(self, blog_id):
        try:
            sql = "UPDATE blogs SET marked_read=NOW() WHERE id=:blog_id"
            self._db.session.execute(sql, {"blog_id": blog_id})
            self._db.session.commit()
            return True
        except:
            return False

    def is_owner(self, user_id, blog_id):
        try:
            sql = "SELECT * FROM blogs WHERE user_id=:user_id AND id=:blog_id"
            result = self._db.session.execute(sql, {"user_id": user_id, "blog_id": blog_id})
            if result.fetchone() is not None:
                return True
            else:
                return False
        except:
            return False

    def get_users_blogs(self, user_id):
        """
        Gets all added blogs by the given user-id.

        Args:
            user_id (Integer): Id of the user whose blogs will be retrieved.

        Returns:
            List(Tuple): List of blogs found. If no blogs were found, return None.
        """
        try:
            sql = "SELECT * FROM blogs WHERE user_id=:user_id"
            result = self._db.session.execute(sql, {"user_id": user_id})
            return result.fetchall()
        except:
            return None
