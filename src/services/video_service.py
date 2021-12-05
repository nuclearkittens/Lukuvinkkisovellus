class VideoService:
    def __init__(self, video_repository):
        self._video_repository = video_repository

    def new_video(self, video, user_id):
        return self._video_repository.add_video(video, user_id)

    def get_my_videos(self, user_id):
        return self._video_repository.get_users_videos(user_id)
