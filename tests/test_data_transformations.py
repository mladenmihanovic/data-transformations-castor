import unittest
import pandas as pd
from src.data_transformations import map_user_guids_to_user_ids, transform_date

class TestDataTransformations(unittest.TestCase):


    def test_map_user_guids_to_user_ids(self):

        df = pd.DataFrame({
            'user_id': ['1a1', '2a2', '3a3', '4a4'],
            'manager_id': ['2a2', '3a3', '1a1', '2a2']
        })

        result_df = map_user_guids_to_user_ids(df)
        
        self.assertEqual(result_df['user_id'].min(), 1)
        self.assertEqual(result_df['user_id'].max(), 4)
        self.assertEqual(int(result_df.iloc[3]['manager_id']), 2) 

    def test_transform_date(self):

        df = pd.DataFrame({
            'date_column': ['2023-01-01', '2023-02-01', '2023-03-01']
        })

        result_df = transform_date(
            df,
            'date_column',
            '%Y-%m-%d',
            '%d/%m/%Y'
        )
        
        expected_dates = ['01/01/2023', '01/02/2023', '01/03/2023']
        self.assertTrue(all(result_df['date_column'] == expected_dates))

if __name__ == '__main__':
    unittest.main() 