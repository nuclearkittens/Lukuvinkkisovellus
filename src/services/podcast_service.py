class PodcastService:
    def __init__(self, podcast_repository):
        self._podcast_repository = podcast_repository

    def new_podcast(self, podcast, user_id):
        return self._podcast_repository.add_podcast(podcast, user_id)

    def get_my_podcasts(self, user_id):
        my_podcasts = self._book_repository.get_users_podcasts(user_id)
        if len(my_podcasts) == 0:
            return None
        else:
            return my_podcasts

    def mark_podcast_finished(self, podcast_id):
        return self._podcast_repository.mark_finished(podcast_id)

    def is_podcast_mine(self, user_id, podcast_id):
        return self._podcast_repository.is_owner(user_id, podcast_id)
