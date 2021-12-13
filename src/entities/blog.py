class Blog:
    
    def __init__(self, author, title, url, description, read=False, id=0, tags=[]):
        """
        Creates blog object.

        Args:
            author (String): Author of the blog.
            title (String): Title of the blog.
            url (String): Url to the blog.
            description (String): Description of the blog.
            read (boolean): read status of the blog.
            id (int): Id of the blog. default to 0.
            tags (List): List of tags attached to the blog. Default to an empty list.
        """
        self._author = author
        self._title = title
        self._url = url
        self._description = description
        self._read = read
        self._id = id
        self._tags = tags

    @property
    def author(self):
        """
        Return author of the blog.

        Returns:
            String: Author given when this blog-object was constructed.
        """
        return self._author

    @author.setter
    def author(self, new):
        """
        Sets a new author for the blog.

        Args:
            author (String): Author of the blog.
        """

        self._author = new

    @property
    def title(self):
        """
        Return title of the blog.

        Returns:
            String: Title given when this blog-object was constructed.
        """
        return self._title

    @title.setter
    def title(self, new):
        """
        Sets a new title for the blog.

        Args:
            title (String): Title of the blog.
        """

        self._title = new

    @property
    def url(self):
        """
        Return url of the blog.

        Returns:
            String: Url given when this blog-object was constructed.
        """
        return self._url

    @url.setter
    def url(self, new):
        """
        Sets a new url for the blog.

        Args:
            url (String): Url of the blog.
        """

        self._url = new

    @property
    def description(self):
        """
        Return description of the blog.

        Returns:
            String: Description given when this blog-object was constructed.
        """
        return self._description

    @description.setter
    def description(self, new):
        """
        Sets a new description for the blog.

        Args:
            description (String): description of the blog.
        """

        self._description = new

    def get_tags(self):
        """
        Return tags of the blog.

        Returns:
            List: tags given when this blog-object was constructed.
        """
        return self._tags

    def get_tag_ids(self):
        return [tag.get_id() for tag in self._tags]

    def get_tag_names(self):
        """
        Return tag names from the tag entity list as string.

        Returns:
            String: tags given when this blog-object was constructed.
        """
        names = [tag.get_name() for tag in self._tags]
        if len(names) == 0:
            return "-"
        return ", ".join(names)

    def get_id(self):
        """
        Return id of the blog.

        Returns:
            int: id given when this blog-object was constructed.
        """
        return self._id
    
    def get_read(self):
        """
        Return read status of the blog.

        Returns:
            boolean: indicates whether or not the blog is marked as read.
        """
        return self._read
