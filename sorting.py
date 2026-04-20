import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]
values = random_numbers(10)  # 10 čísel v rozsahu 0–100
#print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

def selection_sort(seznam):
    print(seznam)
    for min_index in range(len(seznam)):
        min_hod = seznam[min_index]
        min_ind = min_index
        for i in range(min_index, len(seznam)):
            if seznam[i] < min_hod:
                min_index = i
                min_hod = seznam[i]
        seznam[min_ind],seznam[min_index] = seznam[min_index], seznam[min_ind]
    print(seznam)

value = selection_sort(random_numbers(20))
print(value)


def bubble_sort(hodnoty):
    print(hodnoty)
    plt.ion()
    plt.show()
    for max_index in range(len(hodnoty)):
        for hod in range(0, len(hodnoty) - 1 - max_index ):
            if hodnoty[hod] > hodnoty[hod + 1]:
                hodnoty[hod],hodnoty[hod + 1] = hodnoty[hod + 1], hodnoty[hod]
            index_highlight1 = hod
            index_highlight2 = hod + 1
            colors = ["steelblue"] * len(hodnoty)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(hodnoty)), hodnoty, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
    plt.ioff()
    plt.show()
    print(hodnoty)

value = bubble_sort(random_numbers(20))
print(value)




