from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'testname',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """ test for name"""
        form = CollaborateForm({
            'name':'',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(),msg="Name field is empty")
        
    def test_email_is_required(self):
        """ test for email"""
        form = CollaborateForm({
            'name':'testname',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(),msg="email field is empty")

    def test_message_is_required(self):
        """ test for message"""
        form = CollaborateForm({
            'name':'testname',
            'email': 'test@gmail.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(),msg="message field is empty")
        