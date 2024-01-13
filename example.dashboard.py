import grafanalib.core

dashboard = grafanalib.core.Dashboard(
    title="Python generated example dashboard",
    description="Example dashboard using the Random Walk and default Prometheus datasource",
    tags=["example"],
    timezone="browser",
    panels=[
        grafanalib.core.TimeSeries(
            title="Random Walk",
            dataSource="default",
            targets=[
                grafanalib.core.Target(
                    datasource="grafana",
                    expr="example",
                ),
            ],
            gridPos=grafanalib.core.GridPos(h=8, w=16, x=0, y=0),
        ),
        grafanalib.core.GaugePanel(
            title="Random Walk",
            dataSource="default",
            targets=[
                grafanalib.core.Target(
                    datasource="grafana",
                    expr="example",
                ),
            ],
            gridPos=grafanalib.core.GridPos(h=4, w=4, x=17, y=0),
        ),
        grafanalib.core.TimeSeries(
            title="Prometheus http requests",
            dataSource="prometheus",
            targets=[
                grafanalib.core.Target(
                    expr="rate(prometheus_http_requests_total[5m])",
                    legendFormat="{{ handler }}",
                    refId="A",
                ),
            ],
            unit=grafanalib.core.OPS_FORMAT,
            gridPos=grafanalib.core.GridPos(h=8, w=16, x=0, y=10),
        ),
    ],
).auto_panel_ids()
