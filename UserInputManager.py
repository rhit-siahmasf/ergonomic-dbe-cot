import pandas as pd
from abc import ABC, abstractmethod
import pickle as p
import os


class TableManager(ABC):

    @abstractmethod
    def get_tableA_score(self):
        pass

    @abstractmethod
    def get_tableB_score(self):
        pass

    @abstractmethod
    def get_tableC_score(self):
        pass

    @abstractmethod
    def create_table(self, file, column):
        pass


class RebaTableManager(TableManager):

    def __init__(self, col_val):
        self.tableA = self.create_table(col_val)
        print(self.tableA)

    def get_tableA_score(self):
        pass

    def get_tableB_score(self):
        pass

    def get_tableC_score(self):
        pass

    def create_table(self, table):
        real_path = os.path.dirname(os.path.realpath(__file__))
        match table:
            case 1:
                file_dir = os.path.join(real_path, 'tables/REBA-TableA.json')
                return pd.read_json(file_dir)
            case 2:
                file_dir = os.path.join(real_path, 'tables/REBA-TableA.json')
                return pd.read_json(file_dir)
            case 3:
                file_dir = os.path.join(real_path, 'tables/REBA-TableA.json')
                return pd.read_json(file_dir)
            case default:
                return


RebaTableManager(1)

