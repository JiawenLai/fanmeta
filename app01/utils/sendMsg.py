import requests
import json
from ReadYaml import read_yaml


def send(map_id, p_x, p_y, start_time, finish_time):
    config = read_yaml("../config.yaml")
    channel_id = config["channel_id"]
    token = config["token"]
    nonce = config["nonce"]
    url = config["newtest_url"]+"/api/message/send"
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
    print(response.text)
    print(response.request.headers)
    print(json.dumps(response.request.body))


send(1, 10, 20, "2022/09/29 23:59:00", "2023/07/31 22:00:00")
