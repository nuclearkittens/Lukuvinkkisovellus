class Blog:
    
    def __init__(self, author, title, url, description):
        """
        Creates blog object.

        Args:
            author (String): Author of the blog.
            title (String): Title of the blog.
            url (String): Url to the blog.
            description (String): Description of the blog.
        """
        self._author = author
        self._title = title
        self._url = url
        self._description = description

    def get_author(self):
        """
        Return author of the blog.

        Returns:
            String: Author given when this blog-object was constructed.
        """
        return self._author

    def get_title(self):
        """
        Return title of the blog.

        Returns:
            String: Title given when this blog-object was constructed.
        """
        return self._title

    def get_url(self):
        """
        Return url of the blog.

        Returns:
            String: Url given when this blog-object was constructed.
        """
        return self._url

    def get_description(self):
        """
        Return description of the blog.

        Returns:
            String: Description given when this blog-object was constructed.
        """
        return self._description
