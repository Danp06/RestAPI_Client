import requests
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/new_pet', methods=['GET'])
def person():
    return render_template('new_pet.html')


@app.route('/pet_detail', methods=['POST'])
def pet_detail():
    api_url = "https://petstore.swagger.io/v2/pet"
    id = request.form['id']
    name = request.form['name']
    new_data = {
                    "id": id,
                    "category": {
                        "id": 0,
                        "name": "string"
                    },
                    "name": name,
                    "photoUrls": [
                        "string"
                    ],
                    "tags": [
                        {
                            "id": 0,
                            "name": "string"
                        }
                    ],
                    "status": "available"
                }
    response = requests.post(api_url, json=new_data)
    return render_template('pet_detail.html', value=(id, name))


@app.route('/pet', methods=['GET'])
def pets(status: str = "pending"):
    url2 = "https://petstore.swagger.io/v2/pet/findByStatus?status={0}".format(status)
    response = requests.get(url2)
    data_pets = [(i['id'], i['name'], i['status']) for i in response.json()]
    return render_template('pets.html', value=data_pets)


@app.route('/pet_update/<id_pet>', methods=['GET'])
def pet_update(id_pet):
    return render_template('pet_update.html', value=id_pet)


@app.route('/pet_update_detail', methods=['POST'])
def pet_update_detail():
    api_url_update = "https://petstore.swagger.io/v2/pet"
    id = request.form['id']
    name = request.form['name']
    status = request.form['status']
    update_data = {
                        "id": id,
                        "category": {
                            "id": 0,
                            "name": "string"
                        },
                        "name": name,
                        "photoUrls": [
                            "string"
                        ],
                        "tags": [
                            {
                                "id": 0,
                                "name": "string"
                            }
                        ],
                        "status": status
                    }
    response = requests.put(api_url_update, json=update_data)
    return render_template('pet_detail.html', value=(id, name, status))


@app.route('/pet_delete/<id_pet>', methods=['GET'])
def pet_delete(id_pet):
    api_url = "https://petstore.swagger.io/v2/pet/{0}".format(id_pet)
    response = requests.delete(api_url)
    return render_template('pet_detail.html', value="Delete successfully")


@app.route('/order', methods=['GET'])
def order():
    return render_template('order.html')


@app.route('/place_order/<id_pet>', methods=['GET'])
def place_order(id_pet):
    api_url_order = "https://petstore.swagger.io/v2/store/order"
    order = {
        "id": 0,
        "petId": id_pet,
        "quantity": 0,
        "shipDate": "2022-04-06T05:30:35.777Z",
        "status": "placed",
        "complete": "true"
    }
    response = requests.post(api_url_order, json=order)
    return render_template('place_order.html', value=order)


@app.route('/find_order', methods=['POST'])
def find_order():
    order_id = request.form['id']
    api_url_find_order = "https://petstore.swagger.io/v2/store/order/{0}".format(order_id)
    response = requests.get(api_url_find_order)
    order_find = response.json()
    return render_template('find_order.html', value=order_find)


@app.route('/order_delete', methods=["POST"])
def order_delete():
    order_id = request.form['id']
    delete_url = "https://petstore.swagger.io/v2/store/order/{0}".format(order_id)
    response = requests.delete(delete_url)
    return render_template('order_delete.html')


@app.route('/inventory', methods=["GET"])
def inventory():
    url_inventario = "https://petstore.swagger.io/v2/store/inventory"
    response = requests.get(url_inventario)
    inventory_info = response.json()
    return render_template('inventory.html', value=inventory_info)


@app.route('/user', methods=['GET'])
def user():
    return render_template('user.html')


@app.route('/new_user', methods=['GET'])
def new_user():
    return render_template('new_user.html')


@app.route('/get_user', methods=['GET'])
def get_user():
    username = request.form['username']
    url_get_user = "https://petstore.swagger.io/v2/user/{0}".format(username)
    response = requests.get(url_get_user)
    body = [(i['id'], i['name'], i['username']) for i in response.json()]
    return render_template('get_user.html', value=body)


@app.route('/user_detail', methods=['POST'])
def create_user():
    url = 'https://petstore.swagger.io/v2/user'
    id = request.form['id']
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    model_user = {
        "id": id,
        "username": username,
        "name": name,
        "lastName": lastname,
        "email": email,
        "password": password,
        "phone": "3123456789",
        "userStatus": 0
    }
    response = requests.post(url, json=model_user)
    return render_template('user_detail.html', value=(username))


@app.route('/update_user', methods=['POST'])
def update_user():
    id = request.form['id']
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    url_update = "https://petstore.swagger.io/v2/user/{0}".format(username)
    model_user = {
        "id": id,
        "username": username,
        "name": name,
        "lastName": lastname,
        "email": email,
        "password": password,
        "phone": "3123456789",
        "userStatus": 0
        }

    response = requests.put(url_update, json=model_user)
    return render_template('update_user.html', value='done')


@app.route('/delete_user', methods=['POST'])
def delete_user():
    username = request.form['username']
    url = "https://petstore.swagger.io/v2/user/{0}".format(username)
    response = requests.delete(url)
    return render_template('delete_user.html', value='Usuario Eliminado')


'''
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
    
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
'''
if __name__ == '__main__':
    app.run()
