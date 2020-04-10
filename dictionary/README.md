# Python Dictionary Tutorial

As a data scientist working in Python, you’ll need to temporarily store data all the time in an appropriate Python data structure to process it. A special data structure which Python provides natively is the dictionary. Its name already gives away how data is stored: a piece of data or values that can be accessed by a key(word) you have at hand.

Most important features by which you can recognize a dictionary are the curly brackets { } and for each item in the dictionary, the separation of the key and value by a colon :


fruit = {"apple" : 5, "pear" : 3, "banana" : 4, "pineapple" : 1, "cherry" : 20}

# Access the `fruit` dictionary directly (without using get) and print the value of "banana"
print(_____["______"])

# Pick one of 5 the fruits and show that both retrieval styles obtain equal results
print(fruit["_____"] == fruit.get("_____"))

As you can try for yourself, the variable fruit below is a valid dictionary, and you can access an item from the dictionary by putting the key between square brackets [ ]. Alternatively, you can also use the .get() method to do the same thing.
