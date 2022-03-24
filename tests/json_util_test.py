from datetime import date, datetime
import unittest
import uuid

from nsj_gcf_utils.json_util import json_dumps, json_loads


class JsonUtilTest(unittest.TestCase):

    def test_json_loads_dict(self):
        texto = """{
            "id": "74dd6e30-8d62-4a9c-bb8b-78c9b7bd7006",
            "pubsub_message_id": "2428659124732084",
            "tenant": "nasajon",
            "rpa_id": "BUG",
            "received_data": {
                "outro": "dado"
            },
            "status": 200,
            "return": {
                "file_url": "http://www.google.com.br"
            },
            "created_at": "2021-06-14T23:28:00"
        }"""

        dicio = json_loads(texto)

        self.assertEquals(dicio['id'], uuid.UUID(
            "74dd6e30-8d62-4a9c-bb8b-78c9b7bd7006"))
        self.assertEquals(dicio['pubsub_message_id'], '2428659124732084')
        self.assertEquals(dicio['tenant'], 'nasajon')
        self.assertEquals(dicio['rpa_id'], 'BUG')
        self.assertEquals(dicio['received_data']['outro'], 'dado')
        self.assertEquals(dicio['status'], 200)
        self.assertEquals(dicio['return']['file_url'],
                          'http://www.google.com.br')
        self.assertEquals(dicio['created_at'],
                          datetime(2021, 6, 14, 23, 28, 0))

    def test_json_dumps_dict(self):
        lista = [{"a": 1}, {"a": 2}, {
            "c": {"b": uuid.UUID('142aa381-2e16-4061-bb0c-1f433b097d0c'), "data_hora": datetime(2022, 3, 24, 20, 3, 23), "so_data": date(2022, 3, 24)}}]
        val = json_dumps(lista)

        self.assertEquals(
            val, '[{"a": 1}, {"a": 2}, {"c": {"b": "142aa381-2e16-4061-bb0c-1f433b097d0c", "data_hora": "2022-03-24T20:03:23", "so_data": "2022-03-24"}}]')

    def test_json_dumps_obj(self):
        class A:
            def __init__(self) -> None:
                self.codigo = "JOSE"
                self.nome = 'Jose'
                self.doc = None

            def print(self):
                print(self.codigo, self.nome, self.doc)

        a = A()
        val = json_dumps(a)

        self.assertEquals(
            val, '{"codigo": "JOSE", "nome": "Jose", "doc": null}')

    def test_json_dumps_obj_to_dict(self):
        class B:
            def __init__(self) -> None:
                self.codigo = "JOSE"
                self.nome = 'Jose'
                self.doc = None

            def print(self):
                print(self.codigo, self.nome)

            def to_dict(self):
                return {'a': 1}

        b = B()
        val = json_dumps(b)

        self.assertEquals(
            val, '{"a": 1}')

    def test_json_dumps_obj(self):
        class A:
            def __init__(self) -> None:
                self.codigo = "JOSE"
                self.nome = 'Jose'
                self.doc = None

            def print(self):
                print(self.codigo, self.nome, self.doc)

        a = [A(), A()]
        val = json_dumps(a)

        self.assertEquals(
            val, '[{"codigo": "JOSE", "nome": "Jose", "doc": null}, {"codigo": "JOSE", "nome": "Jose", "doc": null}]')

    def test_json_loads_obj(self):
        class A:
            def __init__(self) -> None:
                self.codigo = "JOSE"
                self.nome = 'Jose'
                self.doc = None

            def print(self):
                print(self.codigo, self.nome, self.doc)

        texto = '{"codigo": "JOSE", "nome": "Jose", "doc": null}'
        obj = json_loads(texto, A)

        self.assertEquals(obj.__class__, A)
        self.assertEquals(obj.codigo, 'JOSE')
        self.assertEquals(obj.nome, 'Jose')
        self.assertIsNone(obj.doc)

    def test_json_loads_obj_list(self):
        class A:
            def __init__(self) -> None:
                self.codigo = "JOSE"
                self.nome = 'Jose'
                self.doc = None

            def print(self):
                print(self.codigo, self.nome, self.doc)

        texto = '[{"codigo": "JOSE", "nome": "Jose", "doc": null}, {"codigo": "JUR", "nome": "Jurema", "doc": "123456"}]'
        obj_list = json_loads(texto, A)

        self.assertEquals(obj_list.__class__, list)

        self.assertEquals(obj_list[0].codigo, 'JOSE')
        self.assertEquals(obj_list[0].nome, 'Jose')
        self.assertIsNone(obj_list[0].doc)

        self.assertEquals(obj_list[1].codigo, 'JUR')
        self.assertEquals(obj_list[1].nome, 'Jurema')
        self.assertEquals(obj_list[1].doc, '123456')


if __name__ == '__main__':
    unittest.main()
