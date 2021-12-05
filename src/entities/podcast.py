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

    def get_episode(self):
        """
        Return episode of the podcast.

        Returns:
            String: Episode given when this podcast-object was constructed.
        """
        return self._episode

    def get_description(self):
        """
        Return description of the podcast.

        Returns:
            String: Description given when this podcast-object was constructed.
        """
        return self._description
