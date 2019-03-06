"""Test for SSW567_HomeWork 05a
    Xiaomeng Xu"""

import unittest
from SSW567_HW4_Xiaomeng_Xu import get_repository, get_commit
import unittest.mock

class TestGitHubApi(unittest.TestCase):
    """Autotest cases"""

    @unittest.mock.patch('requests.get')
    def test_get_repository_01(self, mockedReq):
        """Tests for get_repository() with Mock"""
        mockedReq.return_value.json.return_value = [{"name":'Dev'}, {"name": 'GitHubApi567'}]   #Excepted result
        self.assertEqual(get_repository('Sherman77'), ['Dev', 'GitHubApi567'])

    @unittest.mock.patch('requests.get')
    def test_get_repository_02(self, mockedReq):
        """Tests for get_repository() with Mock"""
        mockedReq.return_value.json.return_value = [{"name":'hellogitworld'}, {"name":'helloworld'}, {"name":'Mocks'}, {"name":'Project1'}, {"name":'threads-of-life'}] #Excepted result
        self.assertEqual(get_repository('richkempinski'), ['hellogitworld', 'helloworld', 'Mocks', 'Project1', 'threads-of-life'])

    @unittest.mock.patch('requests.get')
    def test_get_commit_01(self, mockedReq):
        """Tests for get_commit() with Mock"""
        mockedReq.return_value.json.return_value = [{"sha":1},{"sha":2}, {"sha":3},{"sha":4},{"sha":5}, {"sha":6}]
        commits = get_commit('Sherma77', 'sha')
        self.assertEqual(commits, 6)
        

if __name__ == '__main__':
    print('Running unit test')
    unittest.main(exit = False, verbosity = 2)
