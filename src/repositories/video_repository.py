from sqlalchemy import exc


class VideoRepository:
    def __init__(self, db):
        self._db = db

    def add_video(self, video, user_id):
        """
        Adds Video-object to database and links it to current user with id.

        Args:
            video (video): video-object to be added
            user_id (Integer): Id of the user adding the video.

        Returns:
            Boolen: True if successful.
        """
        try:
            title = video.get_title()
            url = video.get_url()
            description = video.get_description()
            sql = "INSERT INTO videos (title, url, description, type, user_id, marked_read) \
                    VALUES (:title, :url, :description, 'Video', :user_id, NULL)"
            self._db.session.execute(
                sql, {"title": title, "url": url, "description": description, "user_id": user_id})
            self._db.session.commit()
            return True
        except:
            return False

    def mark_finished(self, video_id):
        try:
            sql = "UPDATE videos SET marked_read=NOW() WHERE id=:video_id"
            self._db.session.execute(sql, {"video_id": video_id})
            self._db.session.commit()
            return True
        except:
            return False

    def is_owner(self, user_id, video_id):
        try:
            sql = "SELECT * FROM videos WHERE user_id=:user_id AND id=:video_id"
            result = self._db.session.execute(sql, {"user_id": user_id, "video_id": video_id})
            if result.fetchone() != None:
                return True
            else:
                return False
        except:
            return False

    def get_users_videos(self, user_id):
        """
        Gets all added videos by the given user-id.

        Args:
            user_id (Integer): Id of the user whose videos will be retrieved.

        Returns:
            List(Tuple): List of videos found. If no videos were found, return None.
        """
        try:
            sql = "SELECT * FROM videos WHERE user_id=:user_id"
            result = self._db.session.execute(sql, {"user_id": user_id})
            return result.fetchall()
        except:
            return None
