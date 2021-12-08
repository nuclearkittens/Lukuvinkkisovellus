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

    def set_title(self, title):
        """
        Sets a new title for the video.

        Args:
            title (String): Title of the video.
        """

        self._title = title

    def get_url(self):
        """
        Return url of the video.

        Returns:
            String: Url given when this video-object was constructed.
        """
        return self._url

    def set_url(self, url):
        """
        Sets a new url for the video.

        Args:
            url (String): Url of the video.
        """

        self._url = url

    def get_description(self):
        """
        Return description of the video.

        Returns:
            String: Description given when this video-object was constructed.
        """
        return self._description

    def set_description(self, description):
        """
        Sets a new description for the video.

        Args:
            description (String): description of the video.
        """

        self._description = description