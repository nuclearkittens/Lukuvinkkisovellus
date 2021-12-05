from sqlalchemy import exc


class PodcastRepository:
    def __init__(self, db):
        self._db = db

    def add_podcast(self, podcast, user_id):
        """
        Adds Podcast-object to database and links it to current user with id.

        Args:
            podcast (podcast): podcast-object to be added
            user_id (Integer): Id of the user adding the podcast.

        Returns:
            Boolen: True if successful.
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
            result = self._db.session.execute(sql, {"user_id": user_id})
            return result.fetchall()
        except:
            return None
