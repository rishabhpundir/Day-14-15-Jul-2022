# TYPES OF INHERITANCE

# 1. SINGLE INHERITANCE

# class Single_Parent:
#     def __init__(self):
#         print('Single Parent')

# class Child(Single_Parent):
#     pass

# child_obj = Child()
# child_obj


# ------------------------------------------------------------------------


# 2. MULTIPLE INHERITANCE

# class Father:
#     def father_func(self):
#         print("Haanikaarak Baapu ke sapne!")

# class Mother:
#     def mother_func(self):
#         print("Filmy Maa ke dialogues!")

# class Sister:
#     def sister_func(self):
#         print("Sarcastic behen ke opinions!")


# class Son(Father, Mother, Sister):
#     pass

# son_obj = Son()
# son_obj.father_func()
# son_obj.mother_func()
# son_obj.sister_func()


# ------------------------------------------------------------------------


# 3. MULTILEVEL INHERITANCE

# class Greatgrandfather:
#     def greatgrandfather_func(self):
#         print("The Original Baapu!")

# class Grandfather(Greatgrandfather):
#     def grandfather_func(self):
#         print("Classy Babaji!")

# class Father(Grandfather):
#     def father_func(self):
#         print("Haanikaarak Baapu!")

# class Son(Father):
#     def son_func(self):
#         print("Naalaayak Beta!")

# son_obj = Son()
# son_obj.greatgrandfather_func()
# son_obj.grandfather_func()
# son_obj.father_func()
# son_obj.son_func()


# ------------------------------------------------------------------------


# 4. HIERARCICHAL INHERITANCE

# class Parents:
#     def parents_func(self):
#         print("Bacche hai ya raakshasho ki sena = Parents!")

# class ElderSon(Parents):
#     def elder_son_func(self):
#         print("Expectations carrying gadha = Elder Son!")

# class MiddleSon(Parents):
#     def middle_son_func(self):
#         print("Do I even exist for you people = Middle Son!")

# class YoungestDaughter(Parents):
#     def youngest_daughter_func(self):
#         print("Where's my new Hello Kitty school bag = Youngest Daughter!")
    

# elder_son_obj = ElderSon()
# middle_son_obj = MiddleSon()
# youngest_daughter_obj = YoungestDaughter()

# elder_son_obj.parents_func()
# elder_son_obj.elder_son_func()
# middle_son_obj.parents_func()
# middle_son_obj.middle_son_func()
# youngest_daughter_obj.parents_func()
# youngest_daughter_obj.youngest_daughter_func()


# ------------------------------------------------------------------------


# 5. HYBRID HERITANCE

# class Grandfather:
#     def grandfather_func(self):
#         print("Dada ne kaha Ayaashi chhod do...")

# class Father(Grandfather):
#     def father_func(self):
#         print("Baap ne kaha ghar chhod do...")

# class Mother:
#     def mother_func(self):
#         print("Maa ne kaha sharaab chhod do...")

# class Brother(Mother):
#     def brother_func(self):
#         print("Bhai ne kaha gussa karna chhod do...")

# class Devdaas(Father, Brother):
#     def devdaas_func(self):
#         print("Ab toh lagta hai Saansey bhi saath chhod dengi...")

# devdaas_obj = Devdaas()
# devdaas_obj.grandfather_func()
# devdaas_obj.father_func()
# devdaas_obj.mother_func()
# devdaas_obj.brother_func()
# devdaas_obj.devdaas_func()


# ------------------------------------------------------------------------