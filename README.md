# Insurance Quote API

This job aims to group many different tasks to upload models from mybox to netsuite via API. It is grouped as a single job in order to reuse common code between jobs, as the netsuite api client.

## Instalation

To run this project locally, you need to have installed [Vagrant](https://www.vagrantup.com/downloads) and [VirtualBox](https://www.virtualbox.org/).

Additionaly, you must `git clone` this repository to your machine, if you want to make any changes to the code.

## Usage

### Running the project

To **run this project locally**, in a Vagrant container, navigate to the folder that contains the project through your Terminal and call `vagrant up`. This should run the project's virtual-machine. To open the shell on it, run `vagrant ssh`.

Once the shell is open, navigate to the `/vagrant` folder and use the command `source venv3.8/bin/activate` if you want to **activate the virtual environment**. Note that if you don't do that and try to make changes on the code, you might get dependency and python version conflicts or other errors.

To install all dependencies on the virtual environment, run `pip3 install -r requirements.txt`.

### Running tests

Once inside the image's shell, run `python manage.py test`. (Warning: tests are still incomplete at the moment)

### Django commands

Just some useful Django commands for anyone working on this project:

#### Create new Django app

`python manage.py startapp your_app_name`

#### Start Django development server (local)

`python manage.py runserver 0.0.0.0:8000`

#### Create database migrations file

`python manage.py makemigrations`

#### Run migrations

`python manage.py migrate`

## Support

If any doubts/bugs/existential angst come from using this project, please contact me ([Pat](https://github.com/patcky)).

## Contributing

If you feel like contributing to this project, just open a PR, tag me and I will review and integrate any relevant changes.

Thanks! (:

## License

This job manages sensitive internal data, therefore all usage must be previously approved by Loft Brasil Ltda.

## Authors

Currently, the only person who worked on this project is me (Pat).

# Strategy and technical decisions 

I was planning to write about all the technical decisions I made along the project here, but due to lack of time, I am leaving this as a technical debt too. If you have any questions about this topic or about the code, please ask me directly and I will gladly answer.

# Technical debt

- Adapt models' structures to Django's format
- Include validation in the serializers to not accept the request if the `car` and `home` fields are not in the request;
- Add more tests, preferably for each class/method in the serializers, views, models and services
- Add token authentication
- Take credentials off the settings file
- Add data persistence (DB logic)
- Write strategy and technical decisions