import requests
import json
from app01.static.utils.ReadYaml import read_yaml
import os


def send(map_id, p_x, p_y, start_time, finish_time):
    config = read_yaml(os.path.abspath(os.path.dirname(__file__))+"/config.yaml")
    channel_id = config["channel_id"]
    token = config["token"]
    nonce = config["nonce"]
    url = config["newtest_url"]+"api/message/send"
    headers = {
        "Authorization": token
    }
    data = {
        "channel_id": channel_id,
        "content": "{\"type\":\"richText\",\"title\":\"\",\"document\":\"[{\\\"insert\\\":\\\"链接\\\\n\\\"}]\","
                   "\"v2\":\"[{\\\"insert\\\":\\\"链接\\\",\\\"attributes\\\":{\\\"link\\\":\\\"fanmeta://?"
                   "posX=" + str(p_x) + "&posY=" + str(p_y) + "&mapName=" + str(map_id) + "&finishTime=" + finish_time
                   + "&startTime=" + start_time + "\\\"}},"
                                                  "{\\\"insert\\\":\\\"\\\\n\\\"}]\","
                                                  "\"v\":2}",
        "nonce": nonce
    }

    response = requests.post(url=url, data=data, headers=headers)
    print(response.status_code)
