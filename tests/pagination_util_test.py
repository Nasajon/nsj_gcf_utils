import unittest

from nsj_gcf_utils.pagination_util import page_body, PaginationException


class PaginationUtilTest(unittest.TestCase):
    def test_first_page(self):
        result_test = [
            {'id': 0, 'nome': 'teste0'},
            {'id': 1, 'nome': 'teste1'},
            {'id': 2, 'nome': 'teste2'},
            {'id': 3, 'nome': 'teste3'},
            {'id': 4, 'nome': 'teste4'},
            {'id': 5, 'nome': 'teste5'},
            {'id': 6, 'nome': 'teste6'},
            {'id': 7, 'nome': 'teste7'},
            {'id': 8, 'nome': 'teste8'},
            {'id': 9, 'nome': 'teste9'},
            {'id': 10, 'nome': 'teste10'},
            {'id': 11, 'nome': 'teste11'},
            {'id': 12, 'nome': 'teste12'},
            {'id': 13, 'nome': 'teste13'},
            {'id': 14, 'nome': 'teste14'},
            {'id': 15, 'nome': 'teste15'},
            {'id': 16, 'nome': 'teste16'},
            {'id': 17, 'nome': 'teste17'},
            {'id': 18, 'nome': 'teste18'},
            {'id': 19, 'nome': 'teste19'}
        ]

        result = page_body(
            'http://url_base/clientes',
            10,
            None,
            None,
            result_test,
            'id'
        )

        self.assertIsNone(result['prev'])
        self.assertEqual(
            result['next'], 'http://url_base/clientes?after=9&limit=10')
        self.assertEqual(len(result['result']), 10)
        self.assertEqual(result['result'][0]['id'], 0)
        self.assertEqual(result['result'][9]['id'], 9)

    def test_after_9_page(self):
        result_test = [
            {'id': 10, 'nome': 'teste10'},
            {'id': 11, 'nome': 'teste11'},
            {'id': 12, 'nome': 'teste12'},
            {'id': 13, 'nome': 'teste13'},
            {'id': 14, 'nome': 'teste14'},
            {'id': 15, 'nome': 'teste15'},
            {'id': 16, 'nome': 'teste16'},
            {'id': 17, 'nome': 'teste17'},
            {'id': 18, 'nome': 'teste18'},
            {'id': 19, 'nome': 'teste19'},
            {'id': 20, 'nome': 'teste19'}
        ]

        result = page_body(
            'http://url_base/clientes',
            10,
            9,
            None,
            result_test,
            'id'
        )

        self.assertEqual(
            result['prev'], 'http://url_base/clientes?before=9&limit=10')
        self.assertEqual(
            result['next'], 'http://url_base/clientes?after=19&limit=10')
        self.assertEqual(len(result['result']), 10)
        self.assertEqual(result['result'][0]['id'], 10)
        self.assertEqual(result['result'][9]['id'], 19)

    def test_before_9_page(self):
        result_test = [
            {'id': 0, 'nome': 'teste0'},
            {'id': 1, 'nome': 'teste1'},
            {'id': 2, 'nome': 'teste2'},
            {'id': 3, 'nome': 'teste3'},
            {'id': 4, 'nome': 'teste4'},
            {'id': 5, 'nome': 'teste5'},
            {'id': 6, 'nome': 'teste6'},
            {'id': 7, 'nome': 'teste7'},
            {'id': 8, 'nome': 'teste8'},
            {'id': 9, 'nome': 'teste9'},
        ]

        result = page_body(
            'http://url_base/clientes',
            10,
            None,
            9,
            result_test,
            'id'
        )

        self.assertEqual(
            result['prev'], 'http://url_base/clientes?before=0&limit=10')
        self.assertEqual(
            result['next'], 'http://url_base/clientes?after=9&limit=10')
        self.assertEqual(len(result['result']), 10)
        self.assertEqual(result['result'][0]['id'], 0)
        self.assertEqual(result['result'][9]['id'], 9)

    def test_last_page(self):
        result_test = [
            {'id': 10, 'nome': 'teste10'},
            {'id': 11, 'nome': 'teste11'},
            {'id': 12, 'nome': 'teste12'},
            {'id': 13, 'nome': 'teste13'}
        ]

        result = page_body(
            'http://url_base/clientes',
            10,
            9,
            None,
            result_test,
            'id'
        )

        self.assertEqual(
            result['prev'], 'http://url_base/clientes?before=9&limit=10')
        self.assertIsNone(result['next'])
        self.assertEqual(len(result['result']), 4)
        self.assertEqual(result['result'][0]['id'], 10)
        self.assertEqual(result['result'][-1]['id'], 13)

    def test_last_before_page(self):
        result_test = [
            {'id': 0, 'nome': 'teste0'},
            {'id': 1, 'nome': 'teste1'},
            {'id': 2, 'nome': 'teste2'},
            {'id': 3, 'nome': 'teste3'},
        ]

        result = page_body(
            'http://url_base/clientes',
            10,
            None,
            3,
            result_test,
            'id'
        )

        self.assertIsNone(result['prev'])
        self.assertEqual(
            result['next'], 'http://url_base/clientes?after=3&limit=10')
        self.assertEqual(len(result['result']), 4)
        self.assertEqual(result['result'][0]['id'], 0)
        self.assertEqual(result['result'][-1]['id'], 3)

    def test_last_before_page(self):
        result_test = [
            {'id': 0, 'nome': 'teste0'},
            {'id': 1, 'nome': 'teste1'},
            {'id': 2, 'nome': 'teste2'},
            {'id': 3, 'nome': 'teste3'},
        ]

        with self.assertRaises(PaginationException):
            page_body(
                base_url='http://url_base/clientes',
                limit=10,
                current_after=3,
                current_before=1,
                result=result_test,
                id_field='id'
            )


if __name__ == '__main__':
    unittest.main()
