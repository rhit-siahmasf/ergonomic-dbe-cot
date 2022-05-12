import pandas as pd
from abc import ABC, abstractmethod
import pickle as p
import os


class TableManager(ABC):

    @abstractmethod
    def get_tableA_score(self, score_1, score_2, score_3):
        pass

    @abstractmethod
    def get_tableB_score(self, score_1, score_2, score_3):
        pass

    @abstractmethod
    def get_tableC_score(self, score_1, score_2):
        pass

    @abstractmethod
    def create_table(self, table):
        pass


class RebaTableManager(TableManager):

    def __init__(self):
        self.tableA = self.create_table(1)
        self.tableB = self.create_table(2)
        self.tableC = self.create_table(3)

    def get_tableA_score(self, neck_score, trunk_score, leg_score):
        computed_value = self.tableA[trunk_score][neck_score]
        computed_value = computed_value[str(leg_score)]
        return computed_value

    def get_tableB_score(self, lower_score, upper_score, wrist_score):
        computed_value = self.tableB[upper_score][lower_score]
        computed_value = computed_value[str(wrist_score)]
        return computed_value

    def get_tableC_score(self, score_a, score_b):
        computed_value = self.tableC[score_b][score_a]
        print("Table C: " + str(computed_value))
        return computed_value

    def create_table(self, table):
        real_path = os.path.dirname(os.path.realpath(__file__))
        match table:
            case 1:
                file_dir = os.path.join(real_path, 'tables/REBA-TableA.json')
                return pd.read_json(file_dir)
            case 2:
                file_dir = os.path.join(real_path, 'tables/REBA-TableB.json')
                return pd.read_json(file_dir)
            case 3:
                file_dir = os.path.join(real_path, 'tables/REBA-TableC.json')
                return pd.read_json(file_dir)
            case default:
                return


class RulaTableManager(TableManager):

    def __init__(self):
        self.tableA = self.create_table(1)
        self.tableB = self.create_table(2)
        self.tableC = self.create_table(3)

    def get_tableA_score(self, neck_score, trunk_score, leg_score):
        pass

    def get_tableB_score(self, posture_score, neck_score, legs_score):
        computed_value = self.tableB[posture_score][neck_score]
        computed_value = computed_value[str(legs_score)]
        return computed_value

    def get_tableC_score(self, upper_score, lower_score):
        pass

    def create_table(self, table):
        real_path = os.path.dirname(os.path.realpath(__file__))
        match table:
            case 1:
                file_dir = os.path.join(real_path, 'tables/RULA-TableA.json')
                return pd.read_json(file_dir)
            case 2:
                file_dir = os.path.join(real_path, 'tables/RULA-TableA.json')
                return pd.read_json(file_dir)
            case 3:
                file_dir = os.path.join(real_path, 'tables/RULA-TableA.json')
                return pd.read_json(file_dir)
            case default:
                return


