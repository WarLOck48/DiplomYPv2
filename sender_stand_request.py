import Configuration
import requests
import data


# Функция создания заказа
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body)


# Функция по запоминанию трека
def get_order_track():
    track_response = create_order(data.order_body)
    return track_response.json()["track"]


# Функция получения заказа по треку

def get_order_info_by_track():
    track = get_order_track()
    par = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO_BY_TRACK_PATH, params=par)
