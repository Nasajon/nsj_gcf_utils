import unittest

from nsj_gcf_utils.exception import ERPException
from nsj_gcf_utils.rest_error_util import format_error_body


class RestErrorUtilTest(unittest.TestCase):

    def test_format_tuple(self):
        error = ('00', 'msg')
        formated = format_error_body(error)

        self.assertEquals(formated[0]['code'], '00')
        self.assertEquals(formated[0]['message'], 'msg')

    def test_format_erpexception(self):
        error = ERPException('00', 'msg')
        formated = format_error_body(error)

        self.assertEquals(formated[0]['code'], '00')
        self.assertEquals(formated[0]['message'], 'msg')

    def test_format_list_tuple(self):
        error = [('00', 'msg'), ('01', 'msg1')]
        formated = format_error_body(error)

        self.assertEquals(formated[0]['code'], '00')
        self.assertEquals(formated[0]['message'], 'msg')
        self.assertEquals(formated[1]['code'], '01')
        self.assertEquals(formated[1]['message'], 'msg1')

    def test_format_list_erpexception(self):
        error = [ERPException('00', 'msg'), ERPException('01', 'msg1')]
        formated = format_error_body(error)

        self.assertEquals(formated[0]['code'], '00')
        self.assertEquals(formated[0]['message'], 'msg')
        self.assertEquals(formated[1]['code'], '01')
        self.assertEquals(formated[1]['message'], 'msg1')

    def test_format_str(self):
        formated = format_error_body('msg')

        self.assertEquals(formated[0]['code'], None)
        self.assertEquals(formated[0]['message'], 'msg')

    def test_format_exception(self):
        error = Exception('msg')
        formated = format_error_body(error)

        self.assertEquals(formated[0]['code'], None)
        self.assertEquals(formated[0]['message'], 'msg')

    def test_format_list_str(self):
        error = ['msg', 'msg1']
        formated = format_error_body(error)

        self.assertEquals(formated[0]['code'], None)
        self.assertEquals(formated[0]['message'], 'msg')
        self.assertEquals(formated[1]['code'], None)
        self.assertEquals(formated[1]['message'], 'msg1')

    def test_format_list_exception(self):
        error = [Exception('msg'), Exception('msg1')]
        formated = format_error_body(error)

        self.assertEquals(formated[0]['code'], None)
        self.assertEquals(formated[0]['message'], 'msg')
        self.assertEquals(formated[1]['code'], None)
        self.assertEquals(formated[1]['message'], 'msg1')


if __name__ == '__main__':
    unittest.main()
