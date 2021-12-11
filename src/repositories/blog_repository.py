from sqlalchemy import exc
from entities.tag import Tag
from entities.blog import Blog

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

    def get_blog(self, blog_id):
        try:
            sql = "SELECT * FROM blogs WHERE id=:blog_id"
            result = self._db.session.execute(sql, {"blog_id": blog_id})
            return result.fetchone()
        except:
            return None

    def update_blog(self, author, title, url, description, blog_id):
        try:
            sql = "UPDATE blogs SET author=:author, title=:title, url=:url, description=:description WHERE id=:blog_id"
            self._db.session.execute(sql, {"author": author, "title": title, "url": url, "description": description, "blog_id": blog_id})
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
        """
        Checks if the user-id and the blog-id are in the same row in the database.

        Args:
            user_id (Integer): User-id of the currently logged in user.
            blog_id (Integer): blog-id of the blog to be checked.

        Returns:
            Boolean: True if logged user and blog-id matches.
        """
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
            result = self._db.session.execute(sql, {"user_id": user_id}).fetchall()
            blogs = []
            for data in result:
                tags = self.get_tags_by_blog(data[0])
                blog = Blog(
                    author=data[1],
                    title=data[2],
                    url=data[3],
                    description=data[4],
                    read=data[7],
                    id=data[0],
                    tags=tags
                    )
                blogs.append(blog)
            return blogs
        except:
            return None
    
    def get_blogs_by_tag(self, tag_id):
        try:
            sql = "SELECT * FROM blogs, blog_tags \
                WHERE blog_tags.tag_id=:tag_id AND \
                    blog_tags.blog_id=blogs.id"
            result = self._db.session.execute(
                sql, {"tag_id": tag_id})
            return result.fetchall()
        except:
            return None

    def get_tags_by_blog(self, blog_id):
        try:
            sql = "SELECT tags.id, tags.tag FROM tags, \
                blog_tags WHERE blog_tags.tag_id=tags.id \
                    AND blog_tags.blog_id=:blog_id"
            result = self._db.session.execute(
                sql, {"blog_id": blog_id}).fetchall()
            tags = []
            for data in result:
                tag = Tag(data[0], data[1])
                tags.append(tag)
            return tags
        except:
            return None

    def attach_tag(self, tag_id, blog_id):
        try:
            sql = "INSERT INTO blog_tags (tag_id, blog_id) \
                    VALUES (:tag_id, :blog_id)"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "blog_id": blog_id})
            self._db.session.commit()
            return True
        except:
            return False

    def remove_tag(self, tag_id, blog_id):
        try:
            sql = "DELETE FROM blog_tags \
                WHERE tag_id=:tag_id AND blog_id=:blog_id"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "blog_id": blog_id})
            self._db.session.commit()
            return True
        except:
            return False
