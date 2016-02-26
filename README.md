# ORM Extended (Save)

* Today well be extending our Baby ORM to include save functionality.

##### Objective 1 - practice pseudocoding!

* Pseudocode everything!
* Do not write any real code. Read this entire markdown and pseudo code what you intend on doing to complete the prompts

##### Objective 2 - Save method

* In orm-class.py, you'll take all your code from yesterday's `orm_class.py` file and copy/paste it into today's `orm-class.py` file.
* Your goal is to continue to add to the code you wrote yesterday.
* You want to add a `save` method to `orm-class.py` today.
* You want to be able to take any number or arguments from whatever table is supplied, and either create the row, if it doesn't exist, or update the row, if it does exist. The save method should not take parameters, and is an instance method.

```
user = Users(name="Cassie") # new instance
user.save() # creates new row in table, stores id, returns True on success

cassie = Users.get(name="Cassie") # existing row instance
cassie.hair = "purple"
cassie.save() # updates row, returns True
```

#### Objective 3 - The Create Method

* Inside `orm-class.py`, you'll create a new method on the `Model` class called `create`.
* The create method is a class method. It should do two things: 1 create a new row and 2. return an object which is an instance of a class.

```
user = Users.create(name="Greg") # returns newly created instance of User class
```
* Think about the simplest way you can accomplish this.


***HINT***

* We studied some of these in class but familiarize yourself with the following

```
setattr()
hasattr()
__name__
type(self)
__dict__
**kwargs
```
