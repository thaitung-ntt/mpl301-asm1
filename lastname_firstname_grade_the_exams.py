import numpy as np
import pandas as pd


class ScoreStudent:
    '''Nhap danh sach gom ID va cau tra loi.
    Tinh diem cua hoc sinh.
    '''

    def __init__(self):
        self.path = ''
        self.data = None

    def inputData(self):
        # Nhap du lieu ID va cau tra loi tu file txt
        try:
            self.path = input(
                'Enter a class file to grade (i.e. class1 for class1.txt): ')
            url = self.path + '.txt'
            with open(url) as file:
                print(f'Successfully opened {url}')
                self.data = file.read()
        except:
            self.data = None
            print('File cannot be found.')


score = ScoreStudent()

score.inputData()
print(score.data)
