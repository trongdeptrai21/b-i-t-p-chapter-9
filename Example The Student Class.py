"""
Author: Le Trong
Date: 29/10/2021
Problem:
Rrsources to manage a student's name and test scores.
"""
from functools import reduce

class student(object):
    """đại diện cho một sinh viên."""

    def __init__(self, name, number):
        """Tất cả các điểm số đều là 0."""
        self._name = name
        self._scores = []
        for count in range(number):
            self._scores.append(0)
    def getName(self):
        """Trả về tên của học sinh."""
        return self._name

    def getScores(self):
        """Trả về tên của học sinh."""
        return  self._scores

    def setScore(self, i, score):
        """Đặt lại điểm thứ i, đếm từ 1."""
        self._scores[i - 1] = score

    def getScore(self, i):
        """ Trả về điểm thứ i, đếm từ 1."""
        return self._scores[i-1]

    def getAverage(self):
        """ Giữ lại điểm số trung bình."""
        sum = reduce(lambda x, y: x + y, self._scores)
        return sum / len(self._scores)

    def getHighScore(self):
        """Trả về điểm cao nhất."""
        return max(self.scores)

    def __str__(self):
        """Trả về đại diện chuỗi của học sinh. """
        return "Name: " + self._name + "\nScores: " + \
            " ".join(map(str, self._scores))

if __name__ == '__main__':

    student_a = student("Lê Trọng", 5)
    print("Name: ", student_a.getName())
    print("Score: ", student_a.getScores())
    print("Score in i: ", student_a.getScore(2))

    student_a.setScore(1, 9.0)
    print("Score in i: ", student_a.getScore(1))

    print("====="*10)
    print(student_a)