def sort_odd_and_even(a):
    if not isinstance(a, list):
        return None
    
    if not all(isinstance(n, int) for n in a):
        return None
    
    odd = []
    even = []
    output = []

    if (isinstance(n, int) for n in a):
        for n in a:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        
        even.sort()
        odd.sort(reverse=True)
        
        return odd + even

    if len(a) == 0:
        return a 
    


def password_check(a):

    if isinstance(a, list):
        return False
    
    if len(str(a)) < 6 or len(str(a)) > 12:
        return False
    
    count_num = 0
    count_lower = 0 
    count_upper = 0
    for i in a:
        if i.isdigit():
            count_num += 1
        if i.islower():
            count_lower += 1
        if i.islower():
            count_upper += 1

    if count_num < 1 or count_lower < 1 or count_upper < 1:
        return False
    
    special = "$#@"
    count_s = 0
    for i in a:
        if i in special:
            count_s += 1

    if count_s < 1:
        return False
    
    return True

def recursive_digit_sum(a):
    # check the type of input
    if not isinstance(a, int):
        return False
    
    else:
        while a > 9:
            b = 0
            alist = list(str(a))
            for i in alist:
                b += int(i)
            a = b
        return a
    
print(recursive_digit_sum(32))
print(recursive_digit_sum(678))
print(recursive_digit_sum(88888888888888))
print(recursive_digit_sum("a"))


def reverse_words(a):

    word_list = a.split(" ")
    rev_list  =[]

    while len(word_list) > 0:
        word = word_list.pop(0)
        rev_list.append(word[::-1])

    return " ".join(rev_list)

print(reverse_words('Hello World'))
print(reverse_words('python package'))
print(reverse_words('Renmin University of China'))


def is_divisible(a):

    # check the type of the input
    if not isinstance(a, int):
        return None
    elif isinstance(a, int):
        a_list = list(str(a))
        b = 0
        for i in a_list:
            try:
                b += int(i)
            except:
                pass

    if a % b == 0:
        return 'Yes'
    else:
        return 'No'
 
    
print(is_divisible(123))
print(is_divisible("-1.0f"))
print(is_divisible(-102))
print(is_divisible(10))
    
def max_in_list(data):
    max_value = None

    for item in data:
        
        if isinstance(item, (int, float)):
            if max_value is None or item > max_value:
                max_value = item

        elif isinstance(item, (tuple, list, set)):
            item_max = max_in_list(item)
            if item_max is not None and (max_value is None or item_max > max_value):
                max_value = item_max
    return max_value

print(max_in_list([10,-0.2]))
print(max_in_list(["15.5", 7, [(9,2),-2]]))
print(max_in_list(['a',('b','c')]))
print(max_in_list([5, {16, 2}]))



def min_in_list_2(data):
    num_list = [item for item in data if isinstance(item, (int,float))]

    if len(num_list) < 2:
        return None
    
    num_list.sort()

    sec_min = num_list[1]
    
    if sec_min > num_list[0]:
        return (sec_min, data.index(sec_min))
    elif sec_min == num_list[0]:
        data.copy().remove(sec_min)
        loc = data.index(num_list[0]) + 1
        return (sec_min, loc)


print(min_in_list_2([10,-0.2]))
print(min_in_list_2(["15.5", 7, 9, 2, -2, 2]))
print(min_in_list_2(['a','b','c']))
print(min_in_list_2([5, 2, 2]))

# 动态规划——这想法也太妙了！！！
def word_cut(string, dictionary):
    if not string:
        return ([], 0)
    
    n = len(string)
    paths = {i: [] for i in range(n+1)}
    dp = [0] * (n + 1)

    for i in range(1, n+1):
        for j in range(i):
            word = string[j: i]
            if word in dictionary:
                score = dp[j] + dictionary[word]
                if score > dp[i]:
                    dp[i] = score
                    paths[i] = paths[j].copy() + [word]

    if not paths[n]:
        return(None, 0)
    
    return (paths[n], dp[n])





def sorted_with_weird_order(string_list, order):
    if not 0 <= len(string_list) <= 100000:
        return None
    for string in string_list:
        if not 0 <= len(string) <=100000:
            return None
        
    # create an idex for the order(you should set the character as key and the index as value)
    order_index = {char: index for index, char  in enumerate(order)}

    # define a function for comparison
    # compare the orders in the order_index 
    # use subtraction
    def compare(s1, s2):
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                return order_index[c1] - order_index[c2]
        return len(s1) - len(s2)
    
    def sort_key(s):
        return compare(s, string_list[0])
    
    return sorted(string_list, key=sort_key)

# print(sorted_with_weird_order(['', 'ab', 'a'], 'acbdefghijklmnopqrstuvwxyz'))
print(sorted_with_weird_order(['c', 'b', 'a'], 'acbdefghijklmnopqrstuvwxyz'))




class Animal(object):
    def __init__(self, name):
        self.__name = name

    def speak(self):
        print("I am an animal.")

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.__species = 'Dog'

    def speak(self):
        print("I am a Dog.")

    def play(self):
        print(f"Dog {self._Animal__name} is playing.")

class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.__species = 'Cat'

    def speak(self):
        print("I am a Cat.")

    def play(self):
        print(f"Cat {self._Animal__name} is playing.")

class PetShop(object):
    def __init__(self):
        self.__pets = []

    def add_pet(self, pet):
        self.__pets.append(pet)

    def show_pets(self):
        for pet in self._PetShop__pets:
            if isinstance(pet, Dog):
                print(f"{pet._Animal__name} is Dog.")
            elif isinstance(pet, Cat):
                print(f"{pet._Animal__name} is Cat.")

def testing_PetShop(pet_dict):
    pet_shop = PetShop()
    for species, name in pet_dict.items():
        species = species.split("_")
        if species[0] == "Dog":
            dog = Dog(name)
            dog.speak()
            dog.play()
            pet_shop.add_pet(dog)
        elif species[0] == "Cat":
            cat = Cat(name)
            cat.speak()
            cat.play()
            pet_shop.add_pet(cat)
        else:
            print("Incorrect dict keys!")
    pet_shop.show_pets()

testing_PetShop({"Dog_1":"Tom", "Dog_2":"Bob", "Cat":"Lucy"})