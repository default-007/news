import unittest
from models import sources,articles

Sources = sources.Sources
Articles = articles.Articles

class SourcesTest(unittest.TestCase):
    
    '''
    Test class to test the behaviour of the sources class
    
    '''
    def setUp(self):
        
        '''
        Set up method that will run before every Test
        
        '''
        
        self.new_sources = Sources('nbc-news','NBC NEWS','Eliud Kipchoge breaks a record','nbcnews.com','general','USA','eng')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources, Sources))
        
    def test_to_check_instance_variables(self):
        self.assertEqual(self.new_sources.id,'nbc-news')
        self.assertEqual(self.new_sources.name,'NBC NEWS')
        self.assertEqual(self.new_sources.description,'Eliud Kipchoge breaks a record')
        self.assertEqual(self.new_sources.url,'nbcnews.com')
        self.assertEqual(self.new_sources.category,'general')
        self.assertEqual(self.new_sources.country,'USA')
        self.assertEqual(self.new_sources.language,'eng')
        
class ArticlesTest(unittest.TestCase):
    
    '''
    
     Test class to test the behaviour of the articles class
     
    '''
    
    def setUp(self):
        
        '''
        
        Set up method that will run before every Test
        
        '''
        
        self.new_articles = Articles('kbc','Jane Gichuru','bodies in likoni accident found','the bodies of the two victims in likoni found yesterday','kbc.co.ke','likoni.jpeg','2019-10-12T10:46:00Z')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles, Articles))
        
    
        
        
        
        
if __name__ == '__main__':
    unittest.main()