class Podcast:
    
    def __init__(self, title, episode, description):
        """
        Creates podcast object.

        Args:
            title (String): Title of the podcast.
            episode (String): Episode of the podcast.
            description (String): Description of the podcast.
        """
        self._title = title
        self._episode = episode
        self._description = description

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