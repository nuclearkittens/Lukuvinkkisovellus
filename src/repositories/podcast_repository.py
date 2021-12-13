from sqlalchemy import exc
from entities.tag import Tag
from entities.podcast import Podcast

class PodcastRepository:
    def __init__(self, db):
        self._db = db

    def delete_podcast(self, podcast_id):
        try:
            sql = "DELETE FROM podcasts WHERE id=:podcast_id"
            self._db.session.execute(sql, {"podcast_id": podcast_id})
            self._db.session.commit()
            return True
        except:
            return False

    def add_podcast(self, podcast, user_id):
        """
        Adds Podcast-object to database and links it to current user with id.

        Args:
            podcast (podcast): podcast-object to be added
            user_id (Integer): Id of the user adding the podcast.

        Returns:
            Boolean: True if successful.
        """
        try:
            title = podcast.get_title()
            episode = podcast.get_episode()
            description = podcast.get_description()
            sql = "INSERT INTO podcasts (title, episode, description, type, user_id, marked_read) \
                    VALUES (:title, :episode, :description, 'Podcast', :user_id, NULL)"
            self._db.session.execute(
                sql, {"title": title, "episode": episode, "description": description, "user_id": user_id})
            self._db.session.commit()
            return True
        except:
            return False

    def get_podcast(self, podcast_id):
        try:
            sql = "SELECT * FROM podcasts WHERE id=:podcast_id"
            result = self._db.session.execute(sql, {"podcast_id": podcast_id}).fetchone()
            tags = self.get_tags_by_podcast(result[0])
            podcast = Podcast(
                title=result[1],
                episode=result[2],
                description=result[3],
                read=result[6],
                id=result[0],
                tags=tags
                )
            return podcast
        except:
            return None

    def update_podcast(self, title, episode, description, podcast_id):
        try:
            sql = "UPDATE podcasts SET title=:title, episode=:episode, description=:description WHERE id=:podcast_id"
            self._db.session.execute(sql, {"title": title, "episode": episode, "description": description, "podcast_id": podcast_id})
            self._db.session.commit()
            return True
        except:
            return False

    def mark_finished(self, podcast_id):
        try:
            sql = "UPDATE podcasts SET marked_read=NOW() WHERE id=:podcast_id"
            self._db.session.execute(sql, {"podcast_id": podcast_id})
            self._db.session.commit()
            return True
        except:
            return False

    def mark_unfinished(self, podcast_id):
        try:
            sql = "UPDATE podcasts SET marked_read=NULL WHERE id=:podcast_id"
            self._db.session.execute(sql, {"podcast_id": podcast_id})
            self._db.session.commit()
            return True
        except:
            return False

    def is_owner(self, user_id, podcast_id):
        """
        Checks if the user-id and the podcast-id are in the same row in the database.

        Args:
            user_id (Integer): User-id of the currently logged in user.
            podcast_id (Integer): podcast-id of the podcast to be checked.

        Returns:
            Boolean: True if logged user and podcast-id matches.
        """
        try:
            sql = "SELECT * FROM podcasts WHERE user_id=:user_id AND id=:podcast_id"
            result = self._db.session.execute(sql, {"user_id": user_id, "podcast_id": podcast_id})
            if result.fetchone() != None:
                return True
            else:
                return False
        except:
            return False

    def get_users_podcasts(self, user_id):
        """
        Gets all added podcasts by the given user-id.

        Args:
            user_id (Integer): Id of the user whose podcasts will be retrieved.

        Returns:
            List(Tuple): List of podcasts found. If no podcasts were found, return None.
        """
        try:
            sql = "SELECT * FROM podcasts WHERE user_id=:user_id"
            result = self._db.session.execute(sql, {"user_id": user_id}).fetchall()
            podcasts = []
            for data in result:
                tags = self.get_tags_by_podcast(data[0])
                podcast = Podcast(
                    title=data[1],
                    episode=data[2],
                    description=data[3],
                    read=data[6],
                    id=data[0],
                    tags=tags
                    )
                podcasts.append(podcast)
            return podcasts
        except:
            return None

    def get_podcasts_by_tag(self, tag_id):
        try:
            sql = "SELECT * FROM podcasts, podcast_tags \
                WHERE podcast_tags.tag_id=:tag_id AND \
                    podcast_tags.podcast_id=podcasts.id"
            result = self._db.session.execute(
                sql, {"tag_id": tag_id}).fetchall()
            podcasts = []
            for data in result:
                tags = self.get_tags_by_podcast(data[0])
                podcast = Podcast(
                    title=data[1],
                    episode=data[2],
                    description=data[3],
                    read=data[6],
                    id=data[0],
                    tags=tags
                    )
                podcasts.append(podcast)
            return podcasts
        except:
            return None
    
    def get_tags_by_podcast(self, podcast_id):
        try:
            sql = "SELECT tags.id, tags.tag FROM tags, \
                podcast_tags WHERE podcast_tags.tag_id=tags.id \
                    AND podcast_tags.podcast_id=:podcast_id"
            result = self._db.session.execute(
                sql, {"podcast_id": podcast_id}).fetchall()
            tags = []
            for data in result:
                tag = Tag(data[0], data[1])
                tags.append(tag)
            return tags
        except:
            return None

    def attach_tag(self, tag_id, podcast_id):
        try:
            sql = "INSERT INTO podcast_tags (tag_id, podcast_id) \
                    VALUES (:tag_id, :podcast_id)"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "podcast_id": podcast_id})
            self._db.session.commit()
            return True
        except:
            return False

    def remove_tag(self, tag_id, podcast_id):
        try:
            sql = "DELETE FROM podcast_tags WHERE tag_id=:tag_id \
                    AND podcast_id=:podcast_id"
            self._db.session.execute(
                sql, {"tag_id": tag_id, "podcast_id": podcast_id})
            self._db.session.commit()
            return True
        except:
            return False
