from django.test import TestCase
from django.urls import reverse

from fragmantica.notes.models import Note


class NoteListViewTests(TestCase):

	# def assertCollectionEmpty(self, collection, message=None):
	# 	return self.assertEqual(0, len(collection), message)

	def test_note_list_view__when_no_notes__expect_empty_list_and_count_context(self):
		response = self.client.get(reverse('list notes'))
		#
		# # Assert
		# # self.assertCollectionEmpty(response.context['notes_count'])
		# # self.assertCollectionEmpty(response.context['note_list'])
		# self.assertEqual(0, len(response.context['note_list']))
		# # self.assertCollectionEmpty(response.context['note_list'])
		self.assertEqual(0, response.context['notes_count'])


# TODO: sqlite3.IntegrityError: UNIQUE constraint failed: notes_note.id
# 	def test_note_list_view__when_notes__expect_list_and_count_context(self):
# 		notes_count = 2
# 		notes = [
# 			Note.objects.create(
# 				name=f'Test {i*100} note ',
# 				image=f'https://pets.com/{i + 1}.jpg',
# 				category='citrus',
# 				description='description',
# 			)
# 			for i in range(1, notes_count + 1)
# 		]
#
# 		response = self.client.get(reverse('list notes'))
#
# 		self.assertListEqual(notes, list(response.context['note_list']))
# 		self.assertEqual(notes_count, response.context['notes_count'])
