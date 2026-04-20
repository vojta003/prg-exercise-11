from sorting import random_numbers


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, uco):
        if self.scores[uco] >= 90:
            return "A"
        elif self.scores[uco] >= 80:
            return "B"
        elif self.scores[uco] >= 70:
            return "C"
        elif self.scores[uco] >= 60:
            return "D"
        elif self.scores[uco] >= 50:
            return "E"
        else:
            return "F"

    def find(self, body):
        result = []
        for i, sek in enumerate(self.scores):
            if sek == body:
                count = i
                result.append(count)
        return result

    def get_sorted(self):
        scores = self.scores.copy()
        for max_index in range(len(self.scores)):
            for hod in range(0, len(self.scores) - 1 - max_index):
                if self.scores[hod] > self.scores[hod + 1]:
                    self.scores[hod], self.scores[hod + 1] = self.scores[hod + 1], self.scores[hod]
        return self.scores

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    pocet = results.count()
    print(f"Počet lidí na testu je {pocet}")
    for i in range(results.count()):
        body = results.get_by_index(i)
        znamka = results.get_grade(i)
        print(f"Student {i}: {body} points – {znamka}")
    stopro = results.find(100)
    print(f"Počet žáku se  100 body je {stopro}")
    print(f"Zarovnané od nejhoršího po nejlepší: {results.get_sorted()}")

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    pocet = random_results.count()
    print(f"Počet lidí na testu je {pocet}")
    for i in range(random_results.count()):
        body = random_results.get_by_index(i)
        znamka = random_results.get_grade(i)
        print(f"Student {i}: {body} points – {znamka}")
    stopro = random_results.find(100)
    print(f"Počet žáku se  100 body je {stopro}")
    print(f"Zarovnané od nejhoršího po nejlepší: {random_results.get_sorted()}")






if __name__ == "__main__":
    main()




