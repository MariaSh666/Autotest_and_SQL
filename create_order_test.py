# Шульгина Мария 10-я когорта -  Финальный проект. Инженер по тестированию
import configuration
import requests
import data


def create_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                         json=order_body)


def retrieve_order(track_number):
    order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(order_url)
    return response


def test_order_creation():
    response = create_new_order(data.order_body)
    track_number = response.json()["track"]
    print("Order created. Track number:", track_number)


    order_response = retrieve_order(track_number)
    assert order_response.status_code == 200, f"Error: {order_response.status_code}"
    order_data = order_response.json()
    print("Order data:")
    print(order_data)
