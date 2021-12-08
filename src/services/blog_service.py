class BlogService:
    def __init__(self, blog_repository):
        self._blog_repository = blog_repository

    def new_blog(self, blog, user_id):
        return self._blog_repository.add_blog(blog, user_id)

    def get_my_blogs(self, user_id):
        """
        Matches given user_id to found blogs from the database and returns them.

        Args:
            user_id (Integer): user_id of the logged in user.

        Returns:
            List(Tuple) / None: List of blogs if any is found. Else None.
        """
        my_blogs = self._blog_repository.get_users_blogs(user_id)
        if len(my_blogs) == 0:
            return None
        else:
            return my_blogs

    def mark_blog_finished(self, blog_id):
        return self._blog_repository.mark_finished(blog_id)

    def is_blog_mine(self, user_id, blog_id):
        return self._blog_repository.is_owner(user_id, blog_id)