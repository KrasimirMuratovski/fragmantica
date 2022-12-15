from django.test import TestCase
from django.urls import reverse


class NoteListViewTests(TestCase):
	#
	# def assertCollectionEmpty(self, collection, message=None):
	# 	return self.assertEqual(0, len(collection), message)

	def test_awards_list_view__when_no_awards__expect_empty_list(self):
		response = self.client.get(reverse('list awards'))

		# # self.assertCollectionEmpty(response.context['notes_count'])
		# self.assertCollectionEmpty(response.context['awards_list'])

		# self.assertEqual(0, len(response.context['awards_list']))


		self.assertEqual(0, response.context['awards_count'])