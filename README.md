# Adopt a Pet

Imagine you are looking to add a new furry friend to your family! On the pet adoption website, you browse through the categories of animals and select the one you’re interested in, which brings you to another page that contains a list of available pets. Then, you continue your search by further clicking on an individual pet to view its profile page.

Every time you navigate to a different webpage, your browser is making a request to the web server. Thanks to routing, the server knows exactly which endpoint should handle the request and can return the correct HTML page to display.

## Installation

Create an environment

Create a project folder and a venv folder within:

```bash
mkdir project
cd project
python3 -m venv project
```

Install Flask

Within the activated environment, install Flask:
```bash
pip install Flask
```
Activate the venv
```bash
source bin/activate
```
## Usage
```python
flask run
http://localhost:5000/
# Navigate through links of different animals
# Choose the animal type you like
# Click the link of animal in order to get more info about that particular animal  
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
