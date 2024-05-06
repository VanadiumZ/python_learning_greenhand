# def max_in_list(data):

#     max_value = None

#     for item in data:
#         if isinstance(item, (int, float)):
#             if max_value is None or item > max_value:
#                 max_value = item

#         elif isinstance(item, (list, tuple, set)):
#             item_max = max_in_list(item)

#             if item_max is not None:
#                 if max_value is None or item_max > max_value:
#                     max_value = item_max

#     return max_value


# print(max_in_list(["15.5", 7, [(9,2),-2]]))
# print(max_in_list(['a',('b','c')]))
# print(max_in_list([5, {16, 2}]))


# # 实现min_in_list_2函数。输入一个数组，
# # 计算数组中所有出现过的整数或者浮点数中第二小的值以及该值对应的索引。
# # 数组中元素只可能是整数、浮点数或者字符串；
# # 若数组中包括的整数和浮点数的个数小于2，则返回None；
# # 若数组中第二小的数出现多次，则返回第一次出现时的索引；
# # 若第二小的数和最小的数相等，则顺序在前的为最小的数。


# def min_in_list_2(data):
#     num_list = [item for item in data if isinstance(item, (int,float))]

#     if len(num_list) < 2:
#         return None
    
#     num_list.sort()

#     sec_min = num_list[1]
    
#     if sec_min > num_list[0]:
#         return (sec_min, data.index(sec_min))
#     elif sec_min == num_list[0]:
#         data.copy().remove(sec_min)
#         loc = data.index(num_list[0]) + 1
#         return (sec_min, loc)
    
# print(min_in_list_2([10,-0.2]))
# print(min_in_list_2(["15.5", 7, 9, 2, -2, 2]))
# print(min_in_list_2(['a','b','c']))
# print(min_in_list_2([5, 2, 2]))


# 动态规划——这想法也太妙了！！！
# def word_cut(string, dictionary):
#     if not string:
#         return ([], 0)
    
#     n = len(string)
#     paths = {i: [] for i in range(n+1)}
#     dp = [0] * (n + 1)

#     for i in range(1,n+1):
#         for j in range(i):
#             word = string[j: i]
#             if word in dictionary:
#                 score = dp[j] + dictionary[word]
#                 if score > dp[i]:
#                     dp[i] = score
#                     paths[i] = paths[j].copy() + [word]

#     if not paths[n]:
#         return(None, 0)
    
#     return (paths[n], dp[n])

# # print(word_cut("abcabc", {"a": 1, "b": 1, "c": 1}))
# print(word_cut("南京市长江大桥", {"南京": 10, "南京市": 12, "市长": 10, "长江": 10, "大桥": 10, "长江大桥": 25, "江大桥": 1}))


# def sorted_with_weird_order(string_list, order):

#     indexes = {i: order.index(i) for i in order}
    
#     def compare_string(s):
#         char_order = [indexes[i] for i in s]

#     return sorted(string_list, key=compare_string)

# print(sorted_with_weird_order(['', 'ab', 'a'], 'abcdefghijklmnopqrstuvwxyz'))
# print(sorted_with_weird_order(['c', 'b', 'a'], 'acbdefghijklmnopqrstuvwxyz'))
# '''采用面向对象方法实现宠物店管理：
# 有一个父类 Animal，具有属性 name 和方法 speak()。其中，speak() 方法打印出 "I am an animal."

# 有两个子类：Dog 和 Cat。它们继承自 Animal 类，并且都具有一个额外的方法 play()。其中，Dog 类的speak()方法输出"I am a Dog."，
# play()方法输出"Dog {NAME} is playing."; Cat类似。
# 现在，有一个 PetShop 类，管理所有宠物的实例。该类具有以下方法：
# add_pet(pet:Animal)：将一个宠物实例添加到宠物店中。
# show_pets()：显示所有添加到宠物店中的宠物的名称和类型（狗或猫）。
# '''

# class Animal(object):
#     def __init__(self, name):
#         self.__name = name

#     def speak(self):
#         print("I am an animal.")

# class Dog(Animal):
#     def __init__(self, name):
#         super(Dog, self).__init__(name)
#         self.__species = 'Dog'

#     def speak(self):
#         print("I am a Dog.")

#     def play(self):
#         print(f"Dog {self._Animal__name} is playing.")

# class Cat(Animal):
#     def __init__(self, name):
#         super(Cat, self).__init__(name)
#         self.__species = 'Cat'

#     def speak(self):
#         print("I am a Cat.")

#     def play(self):
#         print(f"Cat {self._Animal__name} is playing.")

# class PetShop(object):
#     def __init__(self):
#         self.__pets = []

#     def add_pet(self, pet):
#         self.__pets.append(pet)

#     def show_pets(self):
#         for pet in self._PetShop__pets:
#             if isinstance(pet, Dog):
#                 print(f"{pet._Animal__name} is Dog.")
#             elif isinstance(pet, Cat):
#                 print(f"{pet._Animal__name} is Cat.")

# def testing_PetShop(pet_dict):
#     pet_shop = PetShop()
#     for species, name in pet_dict.items():
#         species = species.split("_")
#         if species[0] == "Dog":
#             dog = Dog(name)
#             dog.speak()
#             dog.play()
#             pet_shop.add_pet(dog)
#         elif species[0] == "Cat":
#             cat = Cat(name)
#             cat.speak()
#             cat.play()
#             pet_shop.add_pet(cat)
#         else:
#             print("Incorrect dict keys!")
#     pet_shop.show_pets()

# testing_PetShop({"Dog_1":"Tom", "Dog_2":"Bob", "Cat":"Lucy"})

# def sorted_with_weird_order(string_list, order):
#     # 创建一个映射，将order中的每个字符映射到其在order中出现的索引
#     order_index = {char: index for index, char in enumerate(order)}
    
#     # 定义一个比较函数，用于比较两个字符串在order中的顺序
#     def compare(s1, s2):
#         # 遍历两个字符串的字符，直到找到一个不同的字符或其中一个字符串结束
#         for c1, c2 in zip(s1, s2):
#             if c1 != c2:
#                 return order_index[c1] - order_index[c2]
#         return len(s1) - len(s2)
    
#     # 定义一个函数，用于生成排序的键
#     def sort_key(s):
#         return compare(s, string_list[0])
    
#     # 使用自定义的比较函数对string_list进行排序
#     return sorted(string_list, key=sort_key)

# # print(sorted_with_weird_order(['c', 'b', 'a'], 'acbdefghijklmnopqrstuvwxyz'))
# print(sorted_with_weird_order(['', 'ab', 'a'], 'abcdefghijklmnopqrstuvwxyz'))
# # print(sorted_with_weird_order(['c', 'b', 'a'], 'abcdefghijklmnopqrstuvwxyz'))
# print(sorted_with_weird_order(['aa', 'aa','', 'pain', 'red'], 'zyxwvutsrqponmlkjihgfedbca'))



# def sorted_with_weird_order(string_list, order):
#     value_dict = {char: i for i, char in enumerate(order)}
#     def get_str_value(string, value_dict, length):
#         value = 0
#         for i, letter in enumerate(string):
#             value += value_dict[letter] * (27 ** (length - i))
#         return value
#     max_length = max([len(string) for string in string_list])
#     string_list.sort(key=lambda x: get_str_value(x, value_dict, max_length))
#     return string_list
# # print(sorted_with_weird_order(['c', 'b', 'a'], 'acbdefghijklmnopqrstuvwxyz'))
# # print(sorted_with_weird_order(['', 'ab', 'a'], 'abcdefghijklmnopqrstuvwxyz'))
# # print(sorted_with_weird_order(['c', 'b', 'a'], 'abcdefghijklmnopqrstuvwxyz'))


# def get_value_dict(order: str):
#     value_dict = {letter: i for i, letter in enumerate(order)}
#     return value_dict


# def get_str_value(string: str, value_dict: dict, length: int):
#     value = 0
#     for i, letter in enumerate(string):
#         value += value_dict[letter] * (27 ** (length - i))
#     return value
    
# def sorted_with_weird_order(string_list: list, order: str):
#     value_dict = get_value_dict(order)
#     max_length = max([len(string) for string in string_list])
#     string_list.sort(key=lambda x: get_str_value(x, value_dict, max_length))
#     return string_list



def sorted_with_weird_order(string_list, order):
    # 创建一个映射，将order中的每个字符映射到其在order中出现的索引
    order_index = {char: index for index, char in enumerate(order)}
    
    # 定义一个比较函数，用于比较两个字符串在order中的顺序
    def compare(s1, s2):
        # 遍历两个字符串的字符，直到找到一个不同的字符或其中一个字符串结束
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                return order_index[c1] - order_index[c2]
        return len(s1) - len(s2)
    
    # 定义一个函数，用于生成排序的键
    def sort_key(s):
        return compare(s, string_list[0])
    
    # 使用自定义的比较函数对string_list进行排序
    return sorted(string_list, key=sort_key)


print(sorted_with_weird_order(['ab','cd','ce'], 'cbaedfghijklmnopqrstuvwxyz'))
# print(sorted_with_weird_order(['', 'ab', 'a'], 'abcdefghijklmnopqrstuvwxyz'))
# print(sorted_with_weird_order(['c', 'b', 'a'], 'abcdefghijklmnopqrstuvwxyz'))
