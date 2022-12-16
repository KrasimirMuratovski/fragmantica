# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from fragmantica.designers.models import Designer
# from fragmantica.notes.models import Note
# from fragmantica.perfumes.models import Perfume
#
# UserModel = get_user_model()
#
#
# class PerfumeDetailsViewTest(TestCase):
#
# 	def test_perfume__when_one_note__expect(self):
# 		des = Designer(
# 			name='test_designer',
# 			photo='https://fimgs.net/mdimg/perfume/375x500.17.jpg',
# 			since=2020,
# 			description='description'
# 			        )
#
# 		des.save()
# 		sample_note=Note(name='Test note',
# 		  image='https://fimgs.net/mdimg/sastojci/t.75.jpg?1650660089',
# 		  category='citrus',
# 		  description='description')
# 		sample_note.save()
#
# 		Perfume.objects.all().delete()
# 		instance = Perfume(name='Diorr',
# 							   released=1990,
# 							   image='https://fimgs.net/mdimg/perfume/375x500.17256.jpg',
# 							   designer=des,
# 							   # note=note.set(),
# 							   perfume_category='Unisex')
#
# 		instance.save()
# 		instance.note.add(sample_note)
# 		instance.save()
# 		print(instance.note.name)
# 		print(instance.note)

# 	self.assertEqual(self.VALID_USER_DATA['username'], response.context['user'].username)
