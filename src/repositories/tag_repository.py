from entities.tag import Tag

class TagRepository:
    def __init__(self, db):
        self._db = db

    def get_tags(self, user_id):
        try:
            sql = "SELECT * FROM tags WHERE user_id=:user_id"
            result = self._db.session.execute(
                sql, {"user_id": user_id}).fetchall()
            tags = []
            for data in result:
                tag = Tag(data[0], data[1])
                tags.append(tag)
            return tags
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
