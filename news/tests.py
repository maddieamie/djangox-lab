from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CustomModel

class CustomModelTests(TestCase):
    
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass',
            email='test@example.com'
        )
    
    def test_user_creation(self):
        """Test that the user was created successfully."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('testpass'))

    def test_custom_model_creation(self):
        """Test that CustomModel can be created with a purchaser."""
        model = CustomModel.objects.create(
            title='Test Model',
            description='This is a test model description.',
            purchaser=self.user
        )
        self.assertEqual(model.title, 'Test Model')
        self.assertEqual(model.description, 'This is a test model description.')
        self.assertEqual(model.purchaser, self.user)

    def test_custom_model_str(self):
        """Test the string representation of CustomModel."""
        model = CustomModel.objects.create(
            title='Another Model',
            description='This is another model description.',
            purchaser=self.user
        )
        self.assertEqual(str(model), 'Another Model')

