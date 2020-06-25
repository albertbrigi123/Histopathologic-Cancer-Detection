import dash_bootstrap_components as dbc

def Navbar():
     navbar = dbc.NavbarSimple(
           children=[
              dbc.NavItem(dbc.NavLink("Adatok bemutatása", href="/aboutdata", style={'font-size' : '0.9em'})),
              dbc.NavItem(dbc.NavLink("Osztályozók összehasonlítása", href="/classifiers",style={'font-size' : '0.9em'})),
              dbc.NavItem(dbc.NavLink("Képosztályozás", href="/classification",style={'font-size' : '0.9em'})),
           ],    
          brand="Főoldal",
          brand_href="/home",
          sticky="top",
        )
     return navbar