import urllib.request
import json
import urllib

class VideoService:
    def __init__(self, video_repository):
        self._video_repository = video_repository

    def new_video(self, video, user_id):
        if video.get_title() == "":
            video.set_title(self.get_title_from_url(video.get_url()))
            
        return self._video_repository.add_video(video, user_id)

    def get_video(self, video_id):
        return self._video_repository.get_video(video_id)

    def update_video(self, title, url, description, video_id):
        """
        First searches that video to be updated exists based on video_id. 
        Then updates its fields.

        Args:
            title (String): Updated title of the video.
            url (String): Updated url to the video.
            description (String): Updated description of the video.
            video_id (Integer): Id of the video to be updated.

        Returns:
            Boolean: True if update was successful.
        """
        video_db_row = self._video_repository.get_video(video_id)
        # Update only if video was actually found
        if video_db_row != None:
            return self._video_repository.update_video(title, url, description, video_id)
        return False

    def get_my_videos(self, user_id):
        """
        Matches given user_id to found videos from the database and returns them.

        Args:
            user_id (Integer): user_id of the logged in user.

        Returns:
            List(Tuple) / None: List of videos if any is found. Else None.
        """
        my_videos = self._video_repository.get_users_videos(user_id)
        if len(my_videos) == 0:
            return None
        else:
            return my_videos

    def mark_video_finished(self, video_id):
        return self._video_repository.mark_finished(video_id)

    def is_video_mine(self, user_id, video_id):
        return self._video_repository.is_owner(user_id, video_id)

    def get_title_from_url(self, url):
        """
        Returns the title of a Youtube video when given an url.

        Args:
            url (String): URL of a Youtube video.
        """

        params = {"format": "json", "url": url}
        query_url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        query_url = query_url + "?" + query_string

        with urllib.request.urlopen(query_url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
            return(data["title"])

    def get_videos_by_tag(self, tag_id):
        return self._video_repository.get_videos_by_tag(tag_id)

    def get_tags_by_video(self, video_id):
        return self._video_repository.get_tags_by_video(video_id)

    def attach_tag(self, tag_id, video_id):
        return self._video_repository.attach_tag(tag_id, video_id)

    def remove_tag(self, tag_id, video_id):
        return self._video_repository.remove_tag(tag_id, video_id)