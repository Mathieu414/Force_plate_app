from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Aside(
    html.Div(
        [
            dbc.Nav(
                [
                    dbc.NavLink(
                        [
                            html.I(className="fas fa-dumbbell"),
                            html.Span("Force plate app"),
                        ],
                        href="/",
                        active="exact",
                        class_name="pe-3 sidebar-header",
                    ),
                    html.Hr(),
                    dbc.NavLink(
                        [html.I(className="fas fa-user-check"), html.Span("Test")],
                        href="/test",
                        active="exact",
                        class_name="pe-3",
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="fas fa-person-running"),
                            html.Span("Séance"),
                        ],
                        href="/seance",
                        active="exact",
                        class_name="pe-3",
                    ),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        className="sidebar",
    )
)
