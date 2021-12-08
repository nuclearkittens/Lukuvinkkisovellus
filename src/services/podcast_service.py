class PodcastService:
    def __init__(self, podcast_repository):
        self._podcast_repository = podcast_repository

    def new_podcast(self, podcast, user_id):
        return self._podcast_repository.add_podcast(podcast, user_id)

    def get_my_podcasts(self, user_id):
<<<<<<< HEAD
        """
        Matches given user_id to found podcasts from the database and returns them.

        Args:
            user_id (Integer): user_id of the logged in user.

        Returns:
            List(Tuple) / None: List of podcasts if any is found. Else None.
        """
=======
>>>>>>> 5c93c7191d28f84dbbf6987a1342615407a5414f
        my_podcasts = self._podcast_repository.get_users_podcasts(user_id)
        if len(my_podcasts) == 0:
            return None
        else:
            return my_podcasts

    def mark_podcast_finished(self, podcast_id):
        return self._podcast_repository.mark_finished(podcast_id)

    def is_podcast_mine(self, user_id, podcast_id):
        return self._podcast_repository.is_owner(user_id, podcast_id)
