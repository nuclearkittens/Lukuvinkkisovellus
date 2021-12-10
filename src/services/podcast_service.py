class PodcastService:
    def __init__(self, podcast_repository):
        self._podcast_repository = podcast_repository

    def new_podcast(self, podcast, user_id):
        return self._podcast_repository.add_podcast(podcast, user_id)

    def update_podcast(self, title, episode, description, podcast_id):
        """
        First searches that podcast to be updated exists based on podcast_id. 
        Then updates its fields.

        Args:
            title (String): Updated title of the podcast.
            episode (String): Updated episode to the podcast.
            description (String): Updated description of the podcast.
            podcast_id (Integer): Id of the podcast to be updated.

        Returns:
            Boolean: True if update was successful.
        """
        podcast_db_row = self._podcast_repository.get_podcast(podcast_id)
        # Update only if podcast was actually found
        if podcast_db_row != None and len(podcast_db_row) > 0:
            return self._podcast_repository.update_podcast(title, episode, description, podcast_id)
        return False

    def get_my_podcasts(self, user_id):
        """
        Matches given user_id to found podcasts from the database and returns them.

        Args:
            user_id (Integer): user_id of the logged in user.

        Returns:
            List(Tuple) / None: List of podcasts if any is found. Else None.
        """
        my_podcasts = self._podcast_repository.get_users_podcasts(user_id)
        if len(my_podcasts) == 0:
            return None
        else:
            return my_podcasts

    def mark_podcast_finished(self, podcast_id):
        return self._podcast_repository.mark_finished(podcast_id)

    def is_podcast_mine(self, user_id, podcast_id):
        return self._podcast_repository.is_owner(user_id, podcast_id)

    def get_podcasts_by_tag(self, tag_id):
        return self._podcast_repository.get_podcasts_by_tag(tag_id)

    def get_tags_by_podcast(self, podcast_id):
        return self._podcast_repository.get_tags_by_podcast(podcast_id)

    def attach_tag(self, tag_id, podcast_id):
        return self._podcast_repository.attach_tag(tag_id, podcast_id)

    def remove_tag(self, tag_id, podcast_id):
        return self._podcast_repository.remove_tag(tag_id, podcast_id)
