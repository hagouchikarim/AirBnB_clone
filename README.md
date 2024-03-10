# AirBnB clone - The console - Morocco

Welcome to the AirBnB Clone Console! This is the first step towards building the AirBnB clone project, a full web application that mimics some functionalities of the popular accommodation rental platform, Airbnb.

## Content:

* [1 Introduction](#1-Introduction)
* [2 Installation](#2-Installation)
* [3 Usage](#3-Usage)
* [4 Testing](#4-Testing)
* [5 Authors](#5-Authors)
* [6 License](#6-license)

# ``1-Introduction``
Team project to build a clone of [AirBnB](https://www.airbnb.com/).


## ``2-Installation``
1.  Clone This GitHub Repository To Your Local Machine.

`git clone https://github.com/hagouchikarim/AirBnB_clone`

2.  Jump to directory of project.

`cd AirBnB-Clone` 

3.  Execute the console.py

`./console.py`

### Execution 

Interactive mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Non Interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## ``3-Usage``

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```

* create

> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*

```bash
(hbnb) create BaseModel
503d1313-743a-4c33-8927-b652d81e2d65
$
```

* show

> *Deletes an instance of a given class with a given ID.*
> *Update the file.json*

```bash
(hbnb) show BaseModel 57262839-51d7-4a9a-93e2-35ed8e91d823
[BaseModel] (503d1313-743a-4c33-8927-b652d81e2d65) {'id': '503d1313-743a-4c33-8927-b652d81e2d65', 'created_at': datetime.datetime(2024, 2, 10, 0, 38, 25, 496645), 'updated_at': datetime.datetime(2024, 2, 10, 0, 38, 25, 496650)}
(hbnb)
(hbhb)
```

* all

> *Prints all string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*

```bash
(hbnb) all
[BaseModel] (503d1313-743a-4c33-8927-b652d81e2d65) {'id': '503d1313-743a-4c33-8927-b652d81e2d65', 'created_at': datetime.datetime(2024, 2, 10, 0, 38, 25, 496645), 'updated_at': datetime.datetime(2024, 2, 10, 0, 38, 25, 496650)}
(hbnb) all BaseModel
[BaseModel] (503d1313-743a-4c33-8927-b652d81e2d65) {'id': '503d1313-743a-4c33-8927-b652d81e2d65', 'created_at': datetime.datetime(2024, 2, 10, 0, 38, 25, 496645), 'updated_at': datetime.datetime(2024, 2, 10, 0, 38, 25, 496650)}
```
* destroy

>*Deletes an instance of a given class with a given ID.*
>*Update the file.json*

```bash
(hbnb) destroy
** class name missing **
(hbnb) destroy BaseModel
** instance id missing **
(hbnb) destroy BaseModel 503d1313-743a-4c33-8927-b652d81e2d65
(hbnb) all
[]
```

* count 

> *Prints the number of instances of a given class.*

```bash
(hbnb) create User
ef8595de-6a2c-496a-af6d-d96f33b389f3
(hbnb) create User
feb9c2f0-6b4f-4dcd-b3ed-2faebc4ccbab
(hbnb) create User
edbc4a23-714a-4364-a52f-ac041042e4b0
(hbnb) User.count()
3
```

## ``4-Testing``

* unittest module
* File extension ``` .py ```
* Files and folders star with ```test_```
* Organization:for ```models/base.py```, unit tests in: ```tests/test_models/test_base.py```
* Execution command: ```python3 -m unittest discover tests```
* or: ```python3 -m unittest tests/test_models/test_base.py```

### run TEST interactive mode

```bash
echo "python3 -m unittest discover tests" | bash
```

### run TEST non-interactive mode

To run the tests in non-interactive mode, and discover all the test, you can use the command:

```bash
python3 -m unittest discover tests
```

## ``5-Authors``

-   [Karim ElHagouchi](https://github.com/hagouchikarim/)
-   [Lyte Yassine Ennaour](https://github.com/yas19sin/)



