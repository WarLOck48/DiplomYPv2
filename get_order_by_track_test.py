
#Мельников Александр, 11-я когорта - Финальный проект. Инженер по тестированию плюс

import requests
from Configuration import URL_SERVICE, CREATE_ORDER_PATH, GET_ORDER_PATH
from data import order_payload, headers

def test_order_creation():
    track_number = create_order()
    order_response = get_info_order(track_number)
    assert order_response.status_code == 200
