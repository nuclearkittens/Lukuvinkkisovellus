class Video:
    
    def __init__(self, title, url, description, read=False, id=0, tags=[]):
        """
        Creates video object.

        Args:
            title (String): Title of the video.
            url (String): Url to the video.
            description (String): Description of the video.
            read (boolean): read status of the video.
            id (int): Id of the video. default to 0.
            tags (List): List of tags attached to the video. Default to an empty list.
        """
        self._title = title
        self._url = url
        self._description = description
        self._read = read
        self._id = id
        self._tags = tags


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
    
    def get_tags(self):
        """
        Return tags of the video.

        Returns:
            List: tags given when this video-object was constructed.
        """
        return self._tags
    
    def get_id(self):
        """
        Return id of the video.

        Returns:
            int: id given when this video-object was constructed.
        """
        return self._id
    
    def get_read(self):
        """
        Return read status of the video.

        Returns:
            boolean: indicates whether or not the video is marked as read.
        """
        return self._read
