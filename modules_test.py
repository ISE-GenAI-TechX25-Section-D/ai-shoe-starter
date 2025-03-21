#############################################################################
# modules_test.py
#
# This file contains tests for modules.py.
#
# You will write these tests in Unit 2.
#############################################################################

import unittest
from streamlit.testing.v1 import AppTest
from modules import display_profile, display_post, display_activity_summary, display_genai_advice, display_recent_workouts
from unittest.mock import patch

# Write your tests below

class TestDisplayProfile(unittest.TestCase):
    """Tests the display_profile function."""

    @patch('modules.get_user_profile')
    @patch('streamlit.markdown')
    @patch('streamlit.image')
    def test_profile_exists(self, mock_image, mock_markdown, mock_get_user_profile):
        """Tests display_profile exists.""" 
        mock_get_user_profile.return_value = {
            'full_name': 'John Doe',
            'username': 'johndoe',
            'date_of_birth': '1990-01-01',
            'profile_image': 'https://example.com/profile.jpg',
            'friends': ['friend1', 'friend2'],
        }

        display_profile('user1')

        mock_get_user_profile.assert_called_once_with('user1')
        mock_markdown.assert_any_call('## John Doe')
        mock_markdown.assert_any_call('### @johndoe')
        mock_markdown.assert_any_call('#### 1990-01-01')
        mock_image.assert_called_once_with('https://example.com/profile.jpg')

    @patch('modules.get_user_profile')
    @patch('streamlit.error')
    def test_profile_not_found(self, mock_error, mock_get_user_profile):
        """Tests display_profile when profile not found."""
        mock_get_user_profile.side_effect = ValueError('User user_1 not found')

        display_profile('user1')

        mock_get_user_profile.assert_called_once_with('user1')
        mock_error.assert_called_once_with('User user_1 not found')


class TestDisplayPost(unittest.TestCase):
    """Tests the display_post function."""

    def test_foo(self):
        """Tests foo."""
        pass


class TestDisplayActivitySummary(unittest.TestCase):
    """Tests the display_activity_summary function."""

    def test_foo(self):
        """Tests foo."""
        pass


class TestDisplayGenAiAdvice(unittest.TestCase):
    """Tests the display_genai_advice function."""

    def test_foo(self):
        """Tests foo."""
        pass


class TestDisplayRecentWorkouts(unittest.TestCase):
    """Tests the display_recent_workouts function."""

    def test_foo(self):
        """Tests foo."""
        pass


if __name__ == "__main__":
    unittest.main()
