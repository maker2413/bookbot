from stats import word_count

def main():
    book = 'books/frankenstein.txt'
    with open(book) as f:
        file_contents = f.read()
        print(f"--- Begin report of {book} ---")
        wc = word_count(file_contents)
        cc = character_count(file_contents)
        sorted_cc = dict_to_list(cc)

        book_report(wc, sorted_cc)
        print("--- End report ---")

def character_count(book_content):
    count = {}
    book_content = book_content.lower()
    for i in range(0, len(book_content)):
        if book_content[i].isalpha():
            if book_content[i] in count:
                count[book_content[i]] += 1
            else:
                count[book_content[i]] = 1

    return count

def book_report(word_count, character_count):
    print(f"{word_count} words found in the document")
    print("")
    for char in character_count:
        print(f"The '{char['char']}' character was found {char['count']} times")

def dict_to_list(dictionary):
    list_of_dict = []
    for d in dictionary:
        list_of_dict.append({"char": d, "count": dictionary[d]})

    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

def sort_on(dictionary):
    return dictionary["count"]

main()
