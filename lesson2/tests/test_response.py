import requests

from configuration import SERVICE_URL

from src.enums.global_enums import GlobalErrorMessages


def test_getting_posts():
    response = requests.get(url=SERVICE_URL)    
    received_posts = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GlobalErrorMessages.WROND_ELEMENT_COUNT.value