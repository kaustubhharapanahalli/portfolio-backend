from rest_framework import serializers

from .models import Homepage


class HomepageSerializer(serializers.ModelSerializer):
    """
    A serializer class for the Homepage model.

    Attributes:
        name (CharField): The name of the individual.
        title (CharField): The title or position of the individual.
        institution (CharField): The institution or organization of the individual.
        profile_image (ImageField): An image field for the profile picture.
        email (CharField): The email address of the individual.

    Methods:
        None
    """

    class Meta:
        model = Homepage
        fields = "__all__"
