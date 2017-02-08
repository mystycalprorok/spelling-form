"""
Spelling Form tests
"""

from django import test

from .utils import convert_number_to_text


class AcceptanceTests(test.TestCase):

    def test_print_number_on_page(self):
        response = self.client.post('/home/',
                                    {'number': '009839482000938428347238'})
        self.assertEqual(200, response.status_code)
        self.assertTrue(
            ('dziewięć tryliardów osiemset trzydzieści dziewięć trylionów '
             'czterysta osiemdziesiąt dwa biliardy dźiewięćset trzydzieści '
             'osiem miliardów czterysta dwadzieścia osiem milionów trzysta '
             'czterdzieści siedem tysięcy dwieście trzydzieści osiem')
             in response.rendered_content
        )


class NumberSpellingTests(test.TestCase):

    def test_1(self):
        self.assertEqual(
            convert_number_to_text('1'),
            'jeden'
        )

    def test_10(self):
        self.assertEqual(
            convert_number_to_text('10'),
            'dziesięć'
        )

    def test_11(self):
        self.assertEqual(
            convert_number_to_text('11'),
            'jedenaście'
        )

    def test_120(self):
        self.assertEqual(
            convert_number_to_text('120'),
            'sto dwadzieścia'
        )

    def test_01999(self):
        self.assertEqual(
            convert_number_to_text('01999'),
            'jeden tysiąc dźiewięćset dziewięćdziesiąt dziewięć'
        )

    def test_145009019987(self):
        self.assertEqual(
            convert_number_to_text('145009019987'),
            ('sto czterdzieści pięć miliardów dziewięć milionów dziewiętnaście '
             'tysięcy dźiewięćset osiemdziesiąt siedem')
        )

    def test_99820982000929832398(self):
        self.assertEqual(
            convert_number_to_text('99820982000929832398'),
            ('dziewięćdziesiąt dziewięć trylionów osiemset dwadzieścia '
             'biliardów dźiewięćset osiemdziesiąt dwa biliony '
             'dźiewięćset dwadzieścia dziewięć milionów osiemset trzydzieści '
             'dwa tysiące trzysta dziewięćdziesiąt osiem')
        )
