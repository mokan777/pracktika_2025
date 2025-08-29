from data_processor import GraphicStatistics

file_path = "BigmacPrice.csv"  # загруженный файл

stats = GraphicStatistics(file_path)
stats.show_histogram()
