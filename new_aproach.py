import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import json
from pathlib import Path
import texts 
import os

p = Path(__file__).parent / "source_files" / "hello.txt"
p_ = Path(__file__).parent / "source_files" 
if p.exists():
    print("the file exists, stepping into processing...")

df = pd.read_json(p, lines=True)
while True:
    print(texts.menu)
    choice = input("insert you option: ")
    os.system("cls")

    match choice:
        case "1":
            print(df.head())
            input()
            os.system("cls")

        case "2":
            print(df.tail())
            input()
            os.system("cls")

        case "3":
            while True:
                print(texts.info_menu)
                choice_info = input("insert your option: ")
                
                match choice_info:
                    case "1":
                        print(df.dtypes)
                        input()
                        os.system("cls")

                    case "2":
                        print(df.index)
                        input()
                        os.system("cls")

                    case "3":
                        print(df.describe())
                        input()
                        os.system("cls")
                    
                    case "0":
                        break

                    case _:
                        print("invalid option")
        case "4":
            print(df.dtypes)
            column = input("insert the column you want to isolate: ")
            data = df.loc[df[column].notna()]
            print(data)
            save = input("Do you want to save this data? (y/n): ")
            if save == "y":
                data.to_json(p_ / f"{column} not null.txt", orient="records", lines=True)

        case "5":
            print(df.dtypes)
            column = input("insert the column you want to filter: ")
            value = float(input("insert the value (rows must contain values grater than this): "))
            data = df.loc[df[column]>value]
            print(data)
            save = input("Do you eant to save this data? (y/n)")
            if save == "y":
                data.to_json(p_ / f"{column} column grater than {value}.txt", orient="records", lines=True)

        case "0":
            break

        case _:
            print("Invalid option")

