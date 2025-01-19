import unittest
import pymysql

class TestSQLQueries(unittest.TestCase):
    
    def test_select_users(self):
        conn = pymysql.connect(host='localhost', user='root', password='password', db='test')
        cursor = conn.cursor()
        
        # Execute the query
        cursor.execute("SELECT * FROM users WHERE age > 18")
        result = cursor.fetchall()
        
        # Define expected result
        expected_result = [('Alice', 25), ('Bob', 32)]
        
        # Assert equality
        self.assertEqual(result, expected_result)
        
        conn.close()

if __name__ == '__main__':
    unittest.main()

