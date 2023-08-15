import numpy as np
import pandas as pd


class ScoreStudent:
    '''Nhap danh sach gom ID va cau tra loi.
    Tinh diem cua hoc sinh.
    '''

    def __init__(self):
        self.path = ''
        self.data = None
        self.numOfQuestion = 25
        self.validNum = 0
        self.invalidNum = 0
        self.questionList = list(map(str, range(1, self.numOfQuestion + 1)))
        self.answer_key = ['B', 'A', 'D', 'D', 'C', 'B', 'D', 'A', 'C', 'C', 'D',
                           'B', 'A', 'B', 'A', 'C', 'B', 'D', 'A', 'C', 'A', 'A', 'B', 'D', 'D']

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

    def _check_ID(self, id):
        # Kiem tra id cua hoc sinh co dung dinh dang khong
        if len(id) != 9 or id[0] != 'N':
            return False
        if all([x.isnumeric() for x in id[1:]]):
            return True
        return False

    def _check_line_error(self, line):
        '''Kiem tra 1 line:
        1. ID co dung dinh dang.
        2. Co du 25 cau tra loi khong.
        '''
        line = line.split(',')
        lineLength = len(line)
        if (lineLength != self.numOfQuestion + 1) and (not self._check_ID(line[0])):
            return f'does not contain exactly {self.numOfQuestion + 1} values and N# is invalid'
        if lineLength != self.numOfQuestion + 1:
            return f'does not contain exactly {self.numOfQuestion + 1} values'
        if not self._check_ID(line[0]):
            return 'N# is invalid'
        return 'No errors'

    def analyseData(self):
        # Phan tich nguyen bang du lieu
        if self.data is None:
            return
        print('\n**** ANALYZING ****\n')
        lineList = self.data.split('\n')
        validLine = []
        for line in lineList:
            check = self._check_line_error(line)
            if check == 'No errors':
                self.validNum += 1
                line = line.split(',')
                validLine.append(line)
            else:
                self.invalidNum += 1
                print('Invalid line of data:', check)
                print(line, '\n')

        if self.invalidNum == 0:
            print('No errors found!')

        if self.validNum != 0:
            columns = ['ID']
            columns.extend(self.questionList)
            # Tao dataframe gom ID va cau tra loi cua cac hoc sinh dung dinh dang
            self.df = pd.DataFrame(validLine, columns=columns)

    def _check_answer_1_student(self, studentAnswer):
        # Cham diem 1 hoc sinh
        score = 0
        for index in range(self.numOfQuestion):
            if not studentAnswer[index]:
                continue
            elif studentAnswer[index] == self.answer_key[index]:
                score += 4
            elif studentAnswer[index] != self.answer_key[index]:
                score -= 1
        return score

    def _scoring_students(self):
        # Cham diem tat ca hoc sinh cua class
        if self.df is None:
            return
        # Them cot Score vao self.df, la diem cua hoc sinh sau khi cham
        self.df['Score'] = self.df.loc[:, self.questionList].apply(
            self._check_answer_1_student, axis=1)

    def report(self):
        # In report
        if self.validNum == 0:
            return
        self._scoring_students()

        print('\n**** REPORT ****\n')
        # Report so valid lines va invalid lines
        print(f'Total valid lines of data: {self.validNum}')
        print(f'Total invalid lines of data: {self.invalidNum}\n')
        # Report cac tinh toan ve diem cua hoc sinh:
        print(f"Mean (average) score: {round(self.df['Score'].mean(), 2)}")
        print(f"Highest score: {round(self.df['Score'].max(), 2)}")
        print(f"Lowest score: {round(self.df['Score'].min(), 2)}")
        print(
            f"Range of scores: {round(self.df['Score'].max() - self.df['Score'].min(), 2)}")
        print(f"Median score: {round(self.df['Score'].median(), 2)}")

    def save_score(self):
        if self.validNum == 0:
            return
        with open(self.path + '_grades.txt', 'w') as file:
            self.df.apply(lambda line: file.write(
                f'{line.ID},{line.Score}\n'), axis=1)


if __name__ == '__main__':
    score = ScoreStudent()
    score.inputData()
    score.analyseData()
    score.report()
    score.save_score()
