import allure
import requests
import os
from allure_commons.types import AttachmentType


def get_url_video(session_id: str):
    API_BROWSERSTACK = os.getenv('API_BROWSERSTACK')
    session = requests.Session()
    session.auth = (os.getenv('LOGIN'), os.getenv('KEY'))
    response = session.get(
        f'{API_BROWSERSTACK}/sessions/{session_id}.json')
    return response.json().get('automation_session').get('video_url')


def add_video(session_id: str, name: str):
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + get_url_video(session_id) \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, name, AttachmentType.HTML, '.html')