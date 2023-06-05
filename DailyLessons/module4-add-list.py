# Method is specific type of function. Method is "owned" by the data it works for
# If there's no data, there's no method.
book_ratings = [7, 9, 5, 6, 8]
book_ratings.append(4)   # .append is a method, belongs to book_ratings variable
print(book_ratings)

# can not call append by itself
book_ratings = [7, 9, 5, 6, 8]
book_ratings.insert(1, 10)  # 1 is the index in which value 10 is inserted
print(book_ratings)