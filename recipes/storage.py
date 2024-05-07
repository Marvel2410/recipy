from django.core.files.storage import FileSystemStorage

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        """
        Returns the name of the file that the file storage system
        should use for the given file.
        """
        return name
