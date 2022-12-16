from django.core.exceptions import ValidationError
from django.test import TestCase
from fragmantica.designers.models import Designer

class DesignerModelTest(TestCase):

    def test_designerFormSve_when_smaller_year_shouldRaise(self):
        des = Designer(
            name='test_designer',
            photo=f'https://test_designer.com/sample_img.jpg',
            since=1600,
            description='description'
        )


        form = ProfileForm(data)
        self.assertFalse(form.is_valid())


    def test_designerCreate_when_bigger_year_shouldRaise(self):
        des = Designer(
            name='test_designer',
            photo=f'https://test_designer.com/sample_img.jpg',
            since=2029,
            description='description'
        )

        try:
            des.full_clean()
            des.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)

    def test_profileCreate_when_in_allowed_range_year_shouldCreate(self):
        des = Designer(
            name='test_designer',
            photo='https://fimgs.net/mdimg/perfume/375x500.17.jpg',
            since=2020,
            description='description'
        )
        des.full_clean()
        des.save()

        self.assertIsNotNone(des)

