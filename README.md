## Automated API testing

### Automated tests for Pet Store public API (https://petstore.swagger.io/)
#### Tests scenarios:

* Successful registration
* Registration with error
* User consult successful
* User consult error
* User consult successful
* Valid user update

#### Http methods used: GET, POST, PUT

### Project configure:
1. python -m venv env
2. env/Scripts/activate
3. In project root type "pip install -e ."
4. In project root type "pip install -r requirements.txt"
5. In project root type "pytest"