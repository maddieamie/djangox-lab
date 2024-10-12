# cats/tests.py
from django.test import TestCase
from .forms import CatForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .models import Cat

class CatFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'Fluffy',
            'breed': 'Persian',
            'nicknames': 'Fluff, Fluffykins',
            'emoji_preference': '😻',
            'color': 'White',
            'tail': 'Long',
            'age': 3,
            'magical_properties': 'Invisibility',
            'image': None  # Assuming image can be optional
        }
        form = CatForm(data=form_data)
        self.assertTrue(form.is_valid())  # Test valid data
        self.assertEqual(form.cleaned_data['name'], 'Fluffy')  # Check cleaned data

    def test_invalid_form(self):
        form_data = {
            'name': '',  # Missing name
            'breed': 'Siamese',
            'nicknames': 'Siam',
            'emoji_preference': '😼',
            'color': 'Brown',
            'tail': 'Short',
            'age': 2,
            'magical_properties': 'None',
            'image': None
        }
        form = CatForm(data=form_data)
        self.assertFalse(form.is_valid())  # Test invalid data
        self.assertIn('name', form.errors)  # Check that name field has errors

    def test_age_field(self):
        form_data = {
            'name': 'Whiskers',
            'breed': 'Maine Coon',
            'nicknames': 'Whisk, Whisker',
            'emoji_preference': '🐱',
            'color': 'Gray',
            'tail': 'Medium',
            'age': -1,  # Invalid age
            'magical_properties': 'Teleportation',
            'image': None
        }
        form = CatForm(data=form_data)
        self.assertFalse(form.is_valid())  # Check that the form is invalid
        self.assertIn('age', form.errors)  # Ensure age field has errors

    def test_image_upload(self):
        # Create a fake image using SimpleUploadedFile
        fake_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\xff\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',  # Simple GIF content
            content_type='image/jpeg'
        )

        # Create a new cat instance using the form
        form_data = {
            'name': 'Whiskers',
            'breed': 'Tabby',
            'nicknames': 'Whisky',
            'emoji_preference': '😸',
            'color': 'Brown',
            'tail': 'Long',
            'age': 3,
            'magical_properties': 'Invisibility',
            'image': fake_image,  # Pass the fake image here
        }

        response = self.client.post(reverse('cat_create'), data=form_data)

        # Check if the cat was created successfully
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        cat = Cat.objects.first()
        self.assertIsNotNone(cat.image)  # Check if the image was saved
        self.assertIn('test_image.jpg', cat.image.name)  # Check if the image name matches

        # Clean up: remove the test image from storage
        cat.image.delete()
