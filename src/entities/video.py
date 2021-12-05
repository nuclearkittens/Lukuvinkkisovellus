class Video:
    
    def __init__(self, title, url, description):
        """
        Creates video object.

        Args:
            title (String): Title of the video.
            url (String): Url to the video.
            description (String): Description of the video.
        """
        self._title = title
        self._url = url
        self._description = description


    def get_title(self):
        """
        Return title of the video.

        Returns:
            String: Title given when this video-object was constructed.
        """
        return self._title

    def get_url(self):
        """
        Return url of the video.

        Returns:
            String: Url given when this video-object was constructed.
        """
        return self._url

    def get_description(self):
        """
        Return description of the video.

        Returns:
            String: Description given when this video-object was constructed.
        """
        return self._description
