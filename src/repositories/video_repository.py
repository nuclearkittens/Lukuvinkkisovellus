from sqlalchemy import exc
from entities.tag import Tag
from entities.video import Video

class VideoRepository:
    def __init__(self, db):
        self._db = db

    def delete_video(self, video_id):
        try:
            sql = "DELETE FROM videos WHERE id=:video_id"
            self._db.session.execute(sql, {"video_id": video_id})
            self._db.session.commit()
            return True
        except:
            return False

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

    def mark_unfinished(self, video_id):
        try:
            sql = "UPDATE videos SET marked_read=NULL WHERE id=:video_id"
            self._db.session.execute(sql, {"video_id": video_id})
            self._db.session.commit()
            return True
        except:
            return False

    def is_owner(self, user_id, video_id):
        """
        Checks if the user-id and the video-id are in the same row in the database.

        Args:
            user_id (Integer): User-id of the currently logged in user.
            video_id (Integer): video-id of the video to be checked.

        Returns:
            Boolean: True if logged user and video-id matches.
        """
        try:
            sql = "SELECT * FROM videos WHERE user_id=:user_id AND id=:video_id"
            result = self._db.session.execute(sql, {"user_id": user_id, "video_id": video_id})
            if result.fetchone() != None:
                return True
            else:
                return False
        except:
            return False

    def get_video(self, video_id):
        try:
            sql = "SELECT * FROM videos WHERE id=:video_id"
            result = self._db.session.execute(sql, {"video_id": video_id}).fetchone()
            tags = self.get_tags_by_video(result[0])
            video = Video(
                title=result[1],
                url=result[2],
                description=result[3],
                read=result[6],
                id=result[0],
                tags=tags
                )
            return video
        except:
            return None

    def update_video(self, title, url, description, video_id):
        try:
            sql = "UPDATE videos SET title=:title, url=:url, description=:description WHERE id=:video_id"
            self._db.session.execute(sql, {"title": title, "url": url, "description": description, "video_id": video_id})
            self._db.session.commit()
            return True
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
            result = self._db.session.execute(sql, {"user_id": user_id}).fetchall()
            videos = []
            for data in result:
                tags = self.get_tags_by_video(data[0])
                video = Video(
                    title=data[1],
                    url=data[2],
                    description=data[3],
                    read=data[6],
                    id=data[0],
                    tags=tags
                    )
                videos.append(video)
            return videos
        except:
            return None

    def get_videos_by_tag(self, tag_id):
        try:
            sql = "SELECT * FROM videos, video_tags \
                WHERE video_tags.tag_id=:tag_id AND \
                    video_tags.video_id=videos.id"
            result = self._db.session.execute(
                sql, {"tag_id": tag_id}).fetchall()
            videos = []
            for data in result:
                tags = self.get_tags_by_video(data[0])
                video = Video(
                    title=data[1],
                    url=data[2],
                    description=data[3],
                    read=data[6],
                    id=data[0],
                    tags=tags
                    )
                videos.append(video)
            return videos
        except:
            return None

    def get_tags_by_video(self, video_id):
        try:
            sql = "SELECT tags.id, tags.tag FROM tags, \
                video_tags WHERE video_tags.tag_id=tags.id \
                    AND video_tags.video_id=:video_id"
            result = self._db.session.execute(
                sql, {"video_id": video_id}).fetchall()
            tags = []
            for data in result:
                tag = Tag(data[0], data[1])
                tags.append(tag)
            return tags
        except:
            return None

    def attach_tag(self, tag_id, video_id):
        try:
            sql = "INSERT INTO video_tags (tag_id, video_id) \
                    VALUES (:tag_id, :video_id)"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "video_id": video_id})
            self._db.session.commit()
            return True
        except:
            return False

    def remove_tag(self, tag_id, video_id):
        try:
            sql = "DELETE FROM video_tags \
                WHERE tag_id=:tag_id AND video_id=:video_id"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "video_id": video_id})
            self._db.session.commit()
            return True
        except:
            return False
