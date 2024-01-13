import json

import grafanalib._gen
import grafanalib.core
import requests


def get_api_key(json_path="/Users/mtm/pdev/taylormonacelli/hereville/resp_token.json"):
    with open(json_path, "r") as file:
        data = json.load(file)

    key = data.get("key")
    return key


def get_dashboard_json(dashboard, overwrite=False, message="Updated by grafanlib"):
    """
    get_dashboard_json generates JSON from grafanalib Dashboard object

    :param dashboard - Dashboard() created via grafanalib
    """

    # grafanalib generates json which need to pack to "dashboard" root element
    return json.dumps(
        {
            "dashboard": dashboard.to_json_data(),
            "overwrite": overwrite,
            "message": message,
        },
        sort_keys=True,
        indent=2,
        cls=grafanalib._gen.DashboardEncoder,
    )


def upload_to_grafana(json_str, server, api_key, verify=True):
    """
    upload_to_grafana tries to upload dashboard to grafana and prints response

    :param json - dashboard json generated by grafanalib
    :param server - grafana server name
    :param api_key - grafana api key with read and write privileges
    """

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    resp = requests.post(
        f"http://{server}/api/dashboards/db",
        data=json_str,
        headers=headers,
        verify=verify,
    )
    # TODO: add error handling

    if resp.status_code != 200:
        raise ValueError(
            f"Request failed with status code {resp.status_code}: {resp.content.decode('utf-8')}"
        )

    formatted_json = json.dumps(json.loads(resp.content.decode("utf-8")), indent=2)

    with open("resp.json", "w") as resp_file:
        resp_file.write(formatted_json)


grafana_api_key = get_api_key()
grafana_server = "127.0.0.1:3000"

my_dashboard = grafanalib.core.Dashboard(title="My awesome dashboard", uid="abifsd")
my_dashboard_json = get_dashboard_json(my_dashboard, overwrite=True)
upload_to_grafana(my_dashboard_json, grafana_server, grafana_api_key)
