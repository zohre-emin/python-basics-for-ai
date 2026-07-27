#####################################################################################

### 12.1 Introduction of Project###

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

### 12.2 Class Decleration and Reading Data

class StudentsGraedAnalyzingTool:
    def __init__(self, file):
        self.file = file
        self.df = None

    def reeading_data(self):
        try:
            self.df = pd.read_csv(self.file)
            if self.df.empty:
                raise ValueError("Empty file")

            columns_needed = {"name", "age", "department", "grade"}

            if not columns_needed.issubset(self.df.columns):
                raise ValueError(
                    f"csv file have missing columns."
                    f"Columns: {columns_needed}"
                )
            self.df["not"] = pd.to_numeric(self.df["grade", errors== "raise"])

            print("Data reading is sucsesful")
            print(self.df)
        except FileNotFoundError:
            print(f"Error: {self.file} not found")
        except pd.errors.EmptyDataError:
            print("Empty file")
        except ValueError as error:
            print(f"Error: {error}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def cal_numpy(self):                                                               ### 12.3 Statistical Analysis ###
        try:
            if self.df is None:
                raise ValueError("Upload the data")
            grades = self.df["grade"].to_numpy

            print(f"Avarage: {np.mean(grades)}")
            print(f"Highest Grade: {np.max(grades)}")
            print(f"Lowest Grade: {np.min(grades)}")
            print(f"Standard Daviation: {np.std(grades)}")
        except ValueError as hata:
            print(f"Error: {hata}")
        except Exception as e:
            print(f"Unexpacted error: {e}")

    def pandas_filtering(self):                                                            ### 12.4 Pandas Filtering ###

        try:
            if self.df is None:
                raise ValueError("Read data first")
            print("Pandas filtering results")

            # students with greater then 80 grades
            high_grade = self.df[self.df["grade"] > 80]
            print(f"Students with graeter then 80: {high_grade}")

            # Students from AI department
            ai_students = self.df[self.df["department"] == "Artificial Intelligence"]
            print(f"Students from AI department: {ai_students}")

            #Students older then 22 
            old_students = self.df[self.df["age"] > 22]
            print(f"Students older then 22: {old_students}")
        except ValueError as hata:
            print(f"Error: {hata}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def draw_graph(self):
        try:
            if self.df is None:
                raise ValueError("Read data first")
            plt.figure(figsize=(10, 5))

            plt.bar(self.df["name"], self.df["grade"])
            plt.title("Studet grade table")
            plt.xlabel("Students")
            plt.ylabel("Grades")

            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Erro: {e}")

    def run__program(self):

        self.reeading_data()

        if self.df is None:
            print("Analyze Paused")
            return

        self.cal_numpy()

        self.pandas_filtering()

        self.draw_graph()
        


#  Start

if __name__ == "__main__":
    file = "student_grades.csv"
    sistem = StudentsGraedAnalyzingTool(file)

    sistem.run__program()

