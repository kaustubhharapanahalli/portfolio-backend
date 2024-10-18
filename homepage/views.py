from rest_framework import generics

from .models import Homepage
from .serializers import HomepageSerializer


class HomepageView(generics.RetrieveAPIView):
    """
    HomepageView is a RetrieveAPIView that retrieves the first object from the Homepage queryset.
    Attributes:
        queryset (QuerySet): A Django QuerySet containing all Homepage objects.
        serializer_class (Serializer): The serializer class used to serialize the Homepage objects.
    Methods:
        get_object():
    """

    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer

    def get_object(self):
        """
        Retrieve the first object from the queryset.
        Returns:
            object: The first object in the queryset, or None if the queryset is empty.
        """

        return self.queryset.first()
