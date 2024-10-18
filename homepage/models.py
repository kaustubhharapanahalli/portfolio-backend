from django.db import models


class Homepage(models.Model):
    """
    A Django model representing the content displayed on the homepage.

    Attributes:
        name (CharField): The name of the individual. Defaults to "Kaustubh Harapanahalli".
        title (CharField): The title or position of the individual. Defaults to "MS Student, Arizona State University".
        profile_image (ImageField): An optional image field for the profile picture. Images are uploaded to "homepage/images/".
        email (CharField): The email address of the individual. Defaults to "kharapan [at] asu [dot] edu".

    Methods:
        __str__: Returns the string representation of the Homepage instance, which is the name of the individual.
    """

    name = models.CharField(max_length=255, default="Kaustubh Harapanahalli")
    title = models.CharField(max_length=255, default="MS Student")
    institution = models.CharField(
        max_length=255, default="Arizona State University"
    )
    profile_image = models.ImageField(
        upload_to="homepage/images/", blank=True, null=True
    )
    email = models.CharField(
        max_length=255, default="kharapan [at] asu [dot] edu"
    )

    def __str__(self):
        return self.name
