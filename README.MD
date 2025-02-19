Simple Prototyping
==================

This is a project created for a presentation on simple prototyping, held at the Sibiu Web Meetup on 21st of March 2024. 
The recording should be available on the [Sibiu Web Meetup YouTube channel](https://www.youtube.com/@sibiuwebmeetup).

The purpose of this project is to show how to create a simple prototype without needing to know any technologies
outside the standard library of your programming language of choice.
For this particular project, I chose Python, but the same principles can be applied to any other language.
The example presented is the back-end implementation of a phonebook application. An example of a simple front-end
implementation was presented in a previous Sibiu Web Meetup.

How to use this project
-----------------------

To run this project, you need Python installed on your machine. 
You can download it from the [official website](https://www.python.org/downloads/).

I recommend using a virtual environment. To create one, using your favorite terminal, run the following commands 
in the project's root folder:

```bash
python -m venv .venv
```

Then, activate the virtual environment. Depending on your operating system and the terminal type, 
the command will be different:

```bash
source .venv/Scripts/activate
```
or 
```bash
.venv/Scripts/activate
```
or
```bash
.venv/bin/activate
```

To run the master branch of the project, run the following command:

```bash
python main.py
```

The `main` will run all the usecases of the application and will print the results in the console. 
The result is something like this:
```
All contacts: []
New contact:  ContactOutput(id='c4eb', name='Adi Shamir', phone='7890', email='adi@adi.com')
Search result:  [ContactOutput(id='c4eb', name='Adi Shamir', phone='7890', email='adi@adi.com')]
Search result:  [ContactOutput(id='c4eb', name='Adi Shamir', phone='7890', email='adi@adi.com')]
Export: [{"id": "c4eb", "name": "Adi Shamir", "phone": "7890", "email": "adi@adi.com"}]
Updated contact: ContactOutput(id='c4eb', name='Adi Shamir', phone='0007890', email='adi@adi.com')
Imported: [(ContactOutput(id='c4eb', name='Adi Shamir', phone='7890', email='adi@adi.com'), ContactOutput(id='c4eb', name='Adi Shamir', phone='0007890', email='adi@adi.com'))]
Imported selected: [ContactOutput(id='c4eb', name='Adi Shamir', phone='7890', email='adi@adi.com')]
Deleted: True
```


The prototyping phase is complete. The next step is to add a REST API layer. This is implemented on another branch
of this project. To switch to that branch, run the following command:

```bash
git checkout rest-api
```
The README file on the `rest-api` branch will contain instructions on how to run the project with the REST API layer.

License
-------
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)][CreativeCommonsLicence]
<br />
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][CreativeCommonsLicence]

[CreativeCommonsLicence]: http://creativecommons.org/licenses/by-nc-sa/4.0/