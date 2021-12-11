class TagService:
    def __init__(self, tag_repository):
        self._tag_repository = tag_repository
    
    def get_tags(self, user_id):
        return self._tag_repository.get_tags(user_id)

    def add_tag(self, tag, user_id):
        return self._tag_repository.add_tag(tag, user_id)

    def edit_tag(self, tag_id, edited_tag):
        return self._tag_repository.edit_tag(tag_id, edited_tag)

    def delete_tag(self, tag_id):
        return self._tag_repository.delete_tag(tag_id)
