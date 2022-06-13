# used in concepts of  'Loose Coupling', 'Dependency Injection', 'Interference'
# there are 4 ways of implementing polymorphism
# i) duck typing  ii) operator overloading  iii) method overloading  iv) method overriding


# DUCK TYPING
# Example 1:
print()
class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class laptop:

    def code(self,ide):
        ide.execute(self)

ide=PyCharm

lap1=laptop()
lap1.code(ide)


# Example 1:
print()
class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class PyCharm:

    def execute(self):
        print("Spell Check")
        print("Conventional Check")
        print("Compiling")
        print("Running")

class laptop:

    def code(self,ide):
        ide.execute(self)

ide=PyCharm

lap1=laptop()
lap1.code(ide)