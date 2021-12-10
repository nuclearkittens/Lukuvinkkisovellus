class TagRepository:
    def __init__(self, db):
        self._db = db

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
            sql = "UPDATE tags SET tag=:edited_tag WHERE id=:tag_id"
            self._db.session.execute(sql, {"tag_id": tag_id, "edited_tag": edited_tag})
            self._db.session.commit()
            return True
        except:
            return False

    def delete_tag(self):
        pass

    def attach_tag_book(self):
        pass

    def attach_tag_blog(self):
        pass

    def attach_tag_podcast(self):
        pass

    def attach_tag_video(self):
        pass
