class Podcast:
    
    def __init__(self, title, episode, description, read=False, id=0, tags=[]):
        """
        Creates podcast object.

        Args:
            title (String): Title of the podcast.
            episode (String): Episode of the podcast.
            description (String): Description of the podcast.
            read (boolean): read status of the podcast.
            id (int): Id of the podcast. default to 0.
            tags (List): List of tags attached to the podcast. Default to an empty list.
        """
        self._title = title
        self._episode = episode
        self._description = description
        self._read = read
        self._id = id
        self._tags = tags

    def get_title(self):
        """
        Return title of the podcast.

        Returns:
            String: Title given when this podcast-object was constructed.
        """
        return self._title

    def set_title(self, title):
        """
        Sets a new title for the podcast.

        Args:
            title (String): Title of the podcast.
        """

        self._title = title

    def get_episode(self):
        """
        Return episode of the podcast.

        Returns:
            String: Episode given when this podcast-object was constructed.
        """
        return self._episode

    def set_episode(self, episode):
        """
        Sets a new name of episode for the podcast.

        Args:
            episode (String): Episode name of the podcast.
        """

        self._episode = episode

    def get_description(self):
        """
        Return description of the podcast.

        Returns:
            String: Description given when this podcast-object was constructed.
        """
        return self._description

    def set_description(self, description):
        """
        Sets a new description for the podcast.

        Args:
            description (String): description of the podcast.
        """

        self._description = description
    
    def get_tags(self):
        """
        Return tags of the podcast.

        Returns:
            List: tags given when this podcast-object was constructed.
        """
        return self._tags

    def get_tag_ids(self):
        return [tag.get_id() for tag in self._tags]
    
    def get_tag_names(self):
        """
        Return tag names from the tag entity list as string.

        Returns:
            String: tags given when this podcast-object was constructed.
        """
        names = [tag.get_name() for tag in self._tags]
        if len(names) == 0:
            return "-"
        return ", ".join(names)

    def get_id(self):
        """
        Return id of the podcast.

        Returns:
            int: id given when this podcast-object was constructed.
        """
        return self._id
    
    def get_read(self):
        """
        Return read status of the podcast.

        Returns:
            boolean: indicates whether or not the podcast is marked as read.
        """
        return self._read
