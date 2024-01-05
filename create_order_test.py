#Мельников Александр, 12-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


def test_create_and_get_order_info():
    response_create = sender_stand_request.create_order(data.CREATE_ORDER_BODY)
    track = response_create.json().get('track')
    response_get_info = sender_stand_request.get_order_info(track)
    assert response_get_info.status_code == data.OK_STATUS
