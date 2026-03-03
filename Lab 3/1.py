def num_1():
    print(len(set(input("Enter a set numebrs Task_1: ").split())))
def num_2():
    print(len(set(input("Enter a one set of numbers Task_2: ").split()) & set(input("Enter a second set of numbers Task_2: ").split())))
def num_3():
    print(*sorted(set(map(int,input("Enter a one set of numbers Task_3: ").split())) & set(map(int,input("Enter a second set of numbers Task_3: ").split()))))
def num_4():
    numbers = input("Enter a sequence of numbers Task_4: ").split()
    seen = set()
    for num in numbers:
        if num in seen:
            print("YES")
        else:
            print("NO")
            seen.add(num)
def num_5():
    n =int(input("Enter a number of lines Task_5: "))
    unique_words = set()
    for i in range(n):
        line_words = input(f"Enter line {i+1} Task_5: ").split()
        unique_words.update(line_words)
    print("Total unique words:", len(unique_words))
def num_6():
    n = int(input("Enter the numbers of employees Task_6: "))
    surnames_count = {}
    for i in range(n):
        name = input(f"Enter the surname of employee {i+1} Task_6: ")
        surnames_count[name] = surnames_count.get(name, 0) + 1
    total_duplicates = 0
    for count in surnames_count.values():
        if count > 1:
            total_duplicates += count 
    print("Total of employees with duplicate surnames:", total_duplicates)
def num_7():
    words = input("Enter a text Task_7: ").split()
    word_counts = {}
    result = []
    for word in words:
        count = word_counts.get(word,0)
        result.append(str(count))
        word_counts[word] = count + 1
    print("Word appearance counts:", " ".join(result))
def num_8():
    n = int(input("Enter a number of synonyms Task_8: "))
    synonyms = {}
    for i in range(n):
        word1, word2 = input(f"Enter synonym pair {i+1} Task_8: ").split()
        synonyms[word1] = word2
        synonyms[word2] = word1
    search_word = input("Enter a word to find its synonym Task_8: ")
    print("The synonym is:", synonyms[search_word])
def num_9():
    n = int(input("Enter a number of lines Task_9: "))
    votes = {}
    for i in range(n):
        line = input(f"Enter record {i+1} Task_9:").split()
        name = line[0]
        count = int(line[1])
        votes[name] = votes.get(name, 0) + count
    sorted_candidates = sorted(votes.keys())
    print("Candidates and their total votes:")
    for name in sorted_candidates:
        print(name, votes[name])
def num_10():
    ACTION_CODES = {
        'read': 'R',
        'write': 'W',
        'execute': 'X'
    }
    n = int(input("Enter a number of files Task_10: "))
    file_permissions = {}
    for i in range(n):
        line = input(f"Enter file info {i+1} Task_10: ").split()
        filename = line[0]
        file_permissions[filename] = set(line[1:])
    m = int(input("Enter number of queries Task_10: "))
    print("\nQuery results:")
    for i in range(m):
        query = input(f"Enter query {i+1} Task_10: ").split()
        operation = query[0]
        filename = query[1]
        needed_code = ACTION_CODES[operation]
        if needed_code in file_permissions.get(filename, set()):
            print("OK")
        else:
            print("Access denied")
def main():
    num_1()
    num_2()
    num_3()
    num_4()
    num_5()
    num_6()
    num_7()
    num_8()
    num_9()
    num_10()
if __name__ == "__main__":
    main()