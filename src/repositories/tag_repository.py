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

    def get_books_by_tag(self, tag_id, user_id):
        try:
            sql = "SELECT * FROM books, book_tags \
                WHERE tag_id=:tag_id AND user_id:user_id \
                    AND book_tags.book_id=books.id"
            result = self._db.session.execute(
                sql, {"tag_id": tag_id, "user_id": user_id})
            return result.fetchone()
        except:
            return None
    
    def get_tags_by_book(self, book_id):
        try:
            sql = "SELECT tags.id, tags.tag FROM tags, \
                book_tags WHERE book_tags.tag_id=tags.id \
                    AND book_tags.book_id=:book_id"
            result = self._db.session.execute(
                sql, {"book_id": book_id})
            return result.fetchone()
        except:
            return None

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

    def get_blogs_by_tag(self, tag_id, user_id):
        try:
            sql = "SELECT * FROM blogs, blog_tags \
                WHERE tag_id=:tag_id AND user_id:user_id \
                    AND blog_tags.blog_id=blogs.id"
            result = self._db.session.execute(
                sql, {"tag_id": tag_id, "user_id": user_id})
            return result.fetchone()
        except:
            return None

    def get_tags_by_blog(self, blog_id):
        try:
            sql = "SELECT tags.id, tags.tag FROM tags, \
                blog_tags WHERE blog_tags.tag_id=tags.id \
                    AND blog_tags.blog_id=:blog_id"
            result = self._db.session.execute(
                sql, {"blog_id": blog_id})
            return result.fetchone()
        except:
            return None

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

    def get_videos_by_tag(self, tag_id, user_id):
        try:
            sql = "SELECT * FROM videos, video_tags \
                WHERE tag_id=:tag_id AND user_id:user_id \
                    AND video_tags.video_id=videos.id"
            result = self._db.session.execute(
                sql, {"tag_id": tag_id, "user_id": user_id})
            return result.fetchone()
        except:
            return None

    def get_tags_by_video(self, video_id):
        try:
            sql = "SELECT tags.id, tags.tag FROM tags, \
                video_tags WHERE video_tags.tag_id=tags.id \
                    AND video_tags.video_id=:video_id"
            result = self._db.session.execute(
                sql, {"video_id": video_id})
            return result.fetchone()
        except:
            return None

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

    def get_podcasts_by_tag(self, tag_id, user_id):
        try:
            sql = "SELECT * FROM podcasts, podcast_tags \
                WHERE tag_id=:tag_id AND user_id:user_id \
                    AND podcast_tags.podcast_id=podcasts.id"
            result = self._db.session.execute(
                sql, {"tag_id": tag_id, "user_id": user_id})
            return result.fetchone()
        except:
            return None
    
    def get_tags_by_podcast(self, podcast_id):
        try:
            sql = "SELECT tags.id, tags.tag FROM tags, \
                podcast_tags WHERE podcast_tags.tag_id=tags.id \
                    AND podcast_tags.podcast_id=:podcast_id"
            result = self._db.session.execute(
                sql, {"podcast_id": podcast_id})
            return result.fetchone()
        except:
            return None

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