import pandas as pd

class Database:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        data = pd.read_csv(self.file_path)
        print("Base de datos cargada correctamente.")
        print(f"Filas: {data.shape[0]}, Columnas: {data.shape[1]}")
        return data