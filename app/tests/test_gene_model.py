import unittest

from app.models.gene import GeneAutoComplete


class GeneModelTest(unittest.TestCase):
    def test_gene_found(self):
        print("test_gene_found")
        response = GeneAutoComplete().search('brc', 'homo_sapiens')
        self.assertEqual(type(response), dict)
        self.assertEqual(type(response['results']), list)

    def test_gene_lookup_field_validation(self):
        print("test_gene_lookup_field_validation")
        response = GeneAutoComplete().search('br', 'ddd')
        self.assertEqual(response['message'], 'Lookup field must be bigger than 3 characters.')
        self.assertEqual(response['status'], 400)

        self.assertEqual(type(response), dict)

    def test_gene_no_result(self):
        print("test_gene_no_result")
        response = GeneAutoComplete().search('bseredtfgyhujr')
        self.assertEqual(response.get('results', []), [])
        self.assertEqual(response.get('status', 200), 200)
        self.assertEqual(type(response), dict)


if __name__ == "__main__":
    unittest.main()
