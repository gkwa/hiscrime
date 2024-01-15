import grafanalib.core

extraJson = {
    "targets": [
        {
            "cacheDurationSeconds": 300,
            "datasource": {
                "type": "marcusolsson-json-datasource",
                "uid": "PFB9AD6BF627C7A10",
            },
            "fields": [
                {"jsonPath": "$..start_time", "language": "jsonpath", "type": "time"},
                {"jsonPath": "$..import_kwh", "language": "jsonpath", "type": "number"},
            ],
            "method": "GET",
            "queryParams": "",
            "refId": "A",
            "urlPath": "",
        }
    ]
}

dashboard = grafanalib.core.Dashboard(
    title="Python generated example dashboard",
    description="Example dashboard using the Random Walk and default Prometheus datasource",
    tags=["example"],
    timezone="browser",
    panels=[
        grafanalib.core.TimeSeries(
            title="My Test Panel",
            dataSource="My JSON datasource - daily",
            extraJson=extraJson,
            gridPos=grafanalib.core.GridPos(h=8, w=16, x=0, y=0),
        ),
    ],
).auto_panel_ids()
