
from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from fragmantica.designers.models import Designer
from fragmantica.perfumes.models import Perfume

UserModel = get_user_model()

# TODO
# def create_perfumes_for_user(user, count=5):
#     result = [Perfume(
#         name=f'Perfume {i + 1}',
#         released=2000 + i,
#         image=f'https://pets.com/{i + 1}.jpg',
#         designer=Designer(name='Dior', photo=f'https://pets.com/{i + 1}.jpg', since=1990, description='text description'),
#         # note='Wood',
#         # award='',
#         perfume_category='unisex',
#
#     ) for i in range(count)]
#
#     [p.save() for p in result]
#
#     return result

class UserDetailsViewTests(TestCase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@fragmantica.com',
        'password': 'st_ro#ng',
    }

    def _create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        return user

    def assertEmpty(self, collection):
        return self.assertEqual(0, len(collection), 'It is not empty')

    def test_user_details__when_owner__expect_is_owner_true(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['is_owner'])

    def test_user_details__when_not_owner__expect_is_owner_false(self):
        profile_user = self._create_user_and_login({
            'username': self.VALID_USER_DATA['username'] + '1',
            'email': self.VALID_USER_DATA['email'] + '1',
            'password': self.VALID_USER_DATA['password'],
        })

        self._create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': profile_user.pk}))

        self.assertFalse(response.context['is_owner'])


    def test_user_details__when_no_perfumes__expect_empty_comments(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEmpty(response.context['user_perfumes'])



	# # TODO
    # def test_user_details__when_perfumes_and_no_comments__expect_perfumes_and_no_comments(self):
    #     user = self._create_user_and_login(self.VALID_USER_DATA)
	#
    #     create_perfumes_for_user(user, count=5)
	#
    #     response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))
	#
    #     self.assertEqual(5, len(response.context['user_perfumes']))
    #     self.assertEmpty(response.context['user_comments'])
    #     self.assertEqual(0, response.context['user_comments'])
	#















    # def test_user_details__when_not_owner__expect_is_owner_false(self):
    #     profile_user = self._create_user_and_login({
    #         'username': self.VALID_USER_DATA['username'] + '1',
    #         'email': self.VALID_USER_DATA['email'] + '1',
    #         'password': self.VALID_USER_DATA['password'],
    #     })
    #
    #     self._create_user_and_login(self.VALID_USER_DATA)
    #
    #     response = self.client.get(reverse_lazy('details user', kwargs={'pk': profile_user.pk}))
    #
    #     self.assertFalse(response.context['is_owner'])

    # def test_user_details__when_owner__expect_is_owner_true(self):
    # 	user = UserModel.objects.create_user(**self.VALID_USER_DATA)
    #
    # 	self.client.login(**self.VALID_USER_DATA)
    # 	response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))
    #
    # 	self.assertTrue(response.context['is_owner'])