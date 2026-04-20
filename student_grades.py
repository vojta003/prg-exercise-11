from itertools import count


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, uco):
        if self.scores[uco] >= 90:
            return "Žák má {self.scores[uco]} bodů a známku A"
        elif self.scores[uco] >= 80:
            return "Žák má {self.scores[uco]} bodů a známku B"
        elif self.scores[uco] >= 70:
            return "Žák má {self.scores[uco]} bodů a známku C"
        elif self.scores[uco] >= 60:
            return "Žák má {self.scores[uco]} bodů a známku D"
        elif self.scores[uco] >= 50:
            return "Žák má {self.scores[uco]} bodů a známku E"
        else:
            return "Žák má {self.scores[uco]} bodů a známku F"

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
        print(scores)
        print(self.scores)

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    pocet = results.count()
    print(f"Počet lidí na testu je {pocet}")
    znamky = results.get_grade(results)
    inde = results.get_by_index(results)
    print(znamky)
    print(inde)
    stopro = results.find(100)
    print(f"Počet žáku se  100 body je {stopro}")
    rada = results.get_sorted()
    print(f"Zarovnané od nejhoršího po nejlepší: {rada}")






if __name__ == "__main__":
    main()




