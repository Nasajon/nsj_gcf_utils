import unittest

from nsj_gcf_utils.dto_util import convert_to


class DTOUtilTest(unittest.TestCase):

    def test_json_dumps_obj(self):
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

        self.assertEquals(b.codigo, 'JOSE')
        self.assertEquals(b.nome, 'Jose')
        self.assertIsNone(b.doc)
        self.assertEquals(b.endereco, 'Rua A')


if __name__ == '__main__':
    unittest.main()
