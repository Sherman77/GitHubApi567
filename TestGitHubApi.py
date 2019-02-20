"""Test for SSW567_HomeWork_Week 4
    Xiaomeng Xu"""

import unittest
from SSW567_HW4_Xiaomeng_Xu import get_repository, get_commit


class TestGitHubApi(unittest.TestCase):
    """Autotest cases"""
    def test_get_repository_01(self):
        """Tests for get_repository()"""
        output = ['Dev', 'GitHubApi567', 'SSW555_TeamPrj', 'SSW567', 'Triangle567'] #Excepted result
        self.assertEqual(get_repository('Sherman77'), output)
        self.assertEqual(get_repository('sherman77'), output)

    def test_get_repository_02(self):
        """Tests for get_repository()"""
        output = ['hellogitworld', 'helloworld', 'Mocks', 'Project1', 'threads-of-life'] #Excepted result
        self.assertEqual(get_repository('richkempinski'), output)
        self.assertEqual(get_repository('Richkempinski'), output)

    def test_get_repositopry_03(self):
        """Tests for get_repository()"""
        id = 'Sherman897978698'
        self.assertRaises(ValueError, get_repository, id)

    def test_get_commit_01(self):
        """Tests for get_commit()"""
        id = 'Sherman77'
        self.assertEqual(get_commit(id, 'Dev'), 3)
        self.assertEqual(get_commit(id, 'Triangle567'), 10)
        self.assertEqual(get_commit(id, 'SSW567'), 1)




if __name__ == '__main__':
    print('Running unit test')
    unittest.main(exit = False, verbosity = 2)
