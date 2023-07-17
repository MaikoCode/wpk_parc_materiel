# Parc Materiel

Parc Materiel is a Django project used for managing equipment.

## Installation

### Prerequisites

Before you continue, ensure you have met the following requirements:

* You have installed Python3. You can verify it with the command `python3 --version`.
* You have installed Pip for package management. Verify it with `pip3 --version`.
* It's recommended to use a virtual environment for project isolation. 

### Installing Parc Materiel

To install Parc Materiel, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/parc-materiel.git
    ```
    Replace `yourusername` with your Github username and `parc-materiel` with the name of your repository.

2. Navigate to the cloned project directory:
    ```bash
    cd parc-materiel
    ```

3. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. Install the project dependencies from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

### Running Parc Materiel

To run Parc Materiel, follow these steps:

1. Apply the migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. Start the Django development server:
    ```bash
    python manage.py runserver
    ```
   Now, you can navigate to `http://127.0.0.1:8000/` in your web browser to see the project running.

## Using Parc Materiel

Parc Materiel allows you to manage equipment in an organization. 

Here's how to use it:

1. Navigate to the home page at `http://127.0.0.1:8000/`.
2. You will see a list of equipment already in the system.
3. You can add, update or delete equipment as needed using the corresponding buttons.

## Contributing to Parc Materiel

To contribute to Parc Materiel, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contact

If you want to contact me you can reach me at `<your_email>@<email_provider>.com`.

## License

This project uses the following license: [<license_name>](<link>).
