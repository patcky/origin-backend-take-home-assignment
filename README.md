# Netsuite-Mybox ETL-job

This job aims to group many different tasks to upload models from mybox to netsuite via API. It is grouped as a single job in order to reuse common code between jobs, as the netsuite api client.

## Instalation

To run this project locally, you need to have installed [Vagrant](https://www.vagrantup.com/downloads) and [VirtualBox](https://www.virtualbox.org/).

Additionaly, you must `git clone` this repository to your machine, if you want to make any changes to the code.

## Usage

### Running the project

To **run this project locally**, in a Vagrant container, navigate to the folder that contains the project through your Terminal and call `vagrant up`. This should run the project's virtual-machine. To open the shell on it, run `vagrant ssh`.

Once the shell is open, you may use `make run/{task}` to **activate the virtual environment**. Note that the job will only run the specified task, not all the avaliable tasks.

### Running tests

Once inside the image's shell, run `make test`.

For code formating, run `make format_code`.

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

# Technical debt

Adapt models to Django's format
- Include validation in the serializers to not accept the request if the car and home fields are not in the request;
- Add more tests, preferably for each class/method in the serializers, views, models and services
- Add token authentication
- Add data persistence (DB logic)