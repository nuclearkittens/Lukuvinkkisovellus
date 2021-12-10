class TagRepository:
    def __init__(self, db):
        self._db = db

    def get_tags(self, user_id):
        try:
            sql = "SELECT * FROM tags WHERE user_id=:user_id"
            result = self._db.session.execute(
                sql, {"user_id": user_id})
            return result.fetchone()
        except:
            return None

    def add_tag(self, tag, user_id):
        try:
            sql = "INSERT INTO tags (tag, user_id) \
                    VALUES (:tag, :user_id)"
            self._db.session.execute(
                sql, {"tag": tag, "user_id": user_id})
            self._db.session.commit()
            return True
        except:
            return False

    def edit_tag(self, tag_id, edited_tag):
        try:
            sql = "UPDATE tags SET tag=:edited_tag \
                WHERE id=:tag_id"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "edited_tag": edited_tag})
            self._db.session.commit()
            return True
        except:
            return False

    def delete_tag(self, tag_id):
        try:
            sql = "DELETE FROM tags WHERE id=:tag_id"
            self._db.session.execute(sql, {"tag_id": tag_id})
            self._db.session.commit()
            return True
        except:
            return False

    def attach_book_tag(self, tag_id, book_id):
        try:
            sql = "INSERT INTO book_tags (tag_id, book_id) \
                    VALUES (:tag_id, :book_id)"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "book_id": book_id})
            self._db.session.commit()
            return True
        except:
            return False

    def remove_book_tag(self, tag_id, book_id):
        try:
            sql = "DELETE FROM book_tags \
                WHERE tag_id=:tag_id AND book_id=:book_id"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "book_id": book_id})
            self._db.session.commit()
            return True
        except:
            return False

    def attach_blog_tag(self, tag_id, blog_id):
        try:
            sql = "INSERT INTO blog_tags (tag_id, blog_id) \
                    VALUES (:tag_id, :blog_id)"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "blog_id": blog_id})
            self._db.session.commit()
            return True
        except:
            return False

    def remove_blog_tag(self, tag_id, blog_id):
        try:
            sql = "DELETE FROM blog_tags \
                WHERE tag_id=:tag_id AND blog_id=:blog_id"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "blog_id": blog_id})
            self._db.session.commit()
            return True
        except:
            return False

    def attach_video_tag(self, tag_id, video_id):
        try:
            sql = "INSERT INTO video_tags (tag_id, video_id) \
                    VALUES (:tag_id, :video_id)"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "video_id": video_id})
            self._db.session.commit()
            return True
        except:
            return False

    def remove_video_tag(self, tag_id, video_id):
        try:
            sql = "DELETE FROM video_tags \
                WHERE tag_id=:tag_id AND video_id=:video_id"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "video_id": video_id})
            self._db.session.commit()
            return True
        except:
            return False

    def attach_podcast_tag(self, tag_id, podcast_id):
        try:
            sql = "INSERT INTO podcast_tags (tag_id, podcast_id) \
                    VALUES (:tag_id, :podcast_id)"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "podcast_id": podcast_id})
            self._db.session.commit()
            return True
        except:
            return False

    def remove_podcast_tag(self, tag_id, podcast_id):
        try:
            sql = "DELETE FROM podcast_tags WHERE tag_id=:tag_id \
                    AND podcast_id=:podcast_id"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "podcast_id": podcast_id})
            self._db.session.commit()
            return True
        except:
            return False