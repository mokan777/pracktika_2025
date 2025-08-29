from data_processor import DataProcessor

if __name__ == "__main__":
    file_path = "var10.csv"  # замени на свой файл
    expected_columns = ['A', 'B', 'C', 'D']
    expected_types = {
        'B': 'str',
        'C': 'float'
    }

    processor = DataProcessor(file_path, expected_columns, expected_types)
    processor.process()
