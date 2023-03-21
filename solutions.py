## Questions...

"""
1. Create a zoo.py file first. Define the hours() function, which prints the string &#39;Open 9-5 daily&#39;.
Then, use the interactive interpreter to import the zoo module and call its hours() function.
2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
3. Using the interpreter, explicitly import and call the hours() function from zoo.
4. Import the hours() function as info and call it.
5. Create a plain dictionary with the key-value pairs &#39;a&#39;: 1, &#39;b&#39;: 2, and &#39;c&#39;: 3, and print it out.
6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the
same order as plain?
7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list
dict_of_lists[&#39;a&#39;] and append the value &#39;something for a&#39; to it in one assignment. Print
dict_of_lists[&#39;a&#39;].
"""

#Answers..

#---------------------------------------------------------------------------------------------#

#1
import zoo
zoo.hours()



#---------------------------------------------------------------------------------------------#

#2
import zoo
zoo.hours()



#---------------------------------------------------------------------------------------------#

#3
from zoo import hours
hours()

#---------------------------------------------------------------------------------------------#

#4
from zoo import hours as info
info()


#---------------------------------------------------------------------------------------------#

#5
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)


#---------------------------------------------------------------------------------------------#

#6
from collections import OrderedDict

fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)



#---------------------------------------------------------------------------------------------#

#7
from collections import defaultdict

dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])


#---------------------------------------------------------------------------------------------#



