import json

import unittest
import requests


class BasicTests(unittest.TestCase):
    host = 'http://172.27.0.1:5000'

    def test_gene_api_not_found_page(self):
        print("test_gene_api_not_found_page")
        response = requests.get(self.host + '/api/gene')
        self.assertEqual(response.status_code, 404)
        response = json.loads(response.text)
        self.assertEqual(type(response['message']), str)

    def test_gene_api_found_page(self):
        print("test_gene_api_found_page")
        response = requests.get(self.host + '/api/genes?lookup=BRCA2&species=aotus_nancymaae')
        self.assertEqual(response.status_code, 200)
        response = json.loads(response.text)
        self.assertEqual(type(response['results']), list)

    def test_gene_api_erorr_400_page(self):
        print("test_gene_api_erorr_400_page")
        response = requests.get(self.host + '/api/genes?lookup=BR')
        self.assertEqual(response.status_code, 400)
        response = json.loads(response.text)
        self.assertEqual(type(response['message']), str)

    def test_gene_api_erorr_405_page(self):
        print("test_gene_api_erorr_405_page")
        response = requests.post(self.host + '/api/genes')
        self.assertEqual(response.status_code, 405)
        response = json.loads(response.text)
        self.assertEqual(type(response['message']), str)


if __name__ == "__main__":
    unittest.main()
