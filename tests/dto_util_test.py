import unittest

from nsj_gcf_utils.dto_util import convert_to


class DTOUtilTest(unittest.TestCase):

    def test_convert_to_obj(self):
        class A:
            def __init__(self) -> None:
                self.codigo = "JOSE"
                self.nome = 'Jose'
                self.doc = None

            def print(self):
                print(self.codigo, self.nome, self.doc)

        class B:
            def __init__(self) -> None:
                self.codigo = "JOAO"
                self.nome = 'Joao'
                self.doc = '456'
                self.endereco = 'Rua A'

            def print(self):
                print(self.codigo, self.nome, self.doc, self.endereco)

        a = A()
        b = convert_to(a, B)

        self.assertEqual(b.__class__, B)
        self.assertEquals(b.codigo, 'JOSE')
        self.assertEquals(b.nome, 'Jose')
        self.assertIsNone(b.doc)
        self.assertEquals(b.endereco, 'Rua A')

    def test_convert_to_list(self):
        class A:
            def __init__(self) -> None:
                self.codigo = "JOSE"
                self.nome = 'Jose'
                self.doc = None

            def print(self):
                print(self.codigo, self.nome, self.doc)

        class B:
            def __init__(self) -> None:
                self.codigo = "JOAO"
                self.nome = 'Joao'
                self.doc = '456'
                self.endereco = 'Rua A'

            def print(self):
                print(self.codigo, self.nome, self.doc, self.endereco)

        a_list = [A(), A()]
        b_list = convert_to(a_list, B)

        self.assertEquals(a_list.__class__, b_list.__class__)
        self.assertEquals(len(a_list), len(b_list))
        for b in b_list:
            self.assertEqual(b.__class__, B)
            self.assertEquals(b.codigo, 'JOSE')
            self.assertEquals(b.nome, 'Jose')
            self.assertIsNone(b.doc)
            self.assertEquals(b.endereco, 'Rua A')


if __name__ == '__main__':
    unittest.main()
