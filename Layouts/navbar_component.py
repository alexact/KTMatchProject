import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[

            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="KTMath",
    brand_href="#",
    color="primary",
    dark=True,
)