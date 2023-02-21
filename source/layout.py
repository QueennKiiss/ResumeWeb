import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from source import images


def professional_page_content() -> html.Div:
    return html.Div(
        id="professional", className="page_container", children=[html.H1("Professional Background"), html.Div(
            className="prof_content_container", children=[dbc.Row(
                [dbc.Col(html.H3("Nanopohtonics"), width=2), dbc.Col(html.H3("Doctorate"), width=4), dbc.Col(),
                    dbc.Col(), dbc.Col(), dbc.Col(html.H3("Post-doctorate")), dbc.Col(), dbc.Col(),
                    dbc.Col(html.H3("Post-doctorate")), dbc.Col(html.H3("Circontrol")), dbc.Col(), ]
                ), dbc.Row(
                [dbc.Col(html.H5("2010")), dbc.Col(html.H5("2011")), dbc.Col(html.H5("2012")),
                    dbc.Col(html.H5("2013")), dbc.Col(html.H5("2014")), dbc.Col(html.H5("2015")),
                    dbc.Col(html.H5("2016")), dbc.Col(html.H5("2017")), dbc.Col(html.H5("2018")),
                    dbc.Col(html.H5("2019")), dbc.Col(html.H5("2020")), dbc.Col(html.H5("2021")),
                    dbc.Col(html.H5("2022")), ]
                ), dbc.Row(
                [dbc.Col(), dbc.Col(), dbc.Col(), dbc.Col(), dbc.Col(), dbc.Col(), ]
                )]
            )]
        )


def about_page_content() -> html.Div:
    return html.Div(
        id="about_page", className="page_container", children=[html.H1("About Me"), dcc.Markdown(
            '''
                I am a technology enthusiast and motivated physicist/electronic
                engineer looking for a professional career change.
                Last 7 years I have been working in a R&D environment and I have
                participated in several projects with
                national and international collaborations.
                Within the multidisciplinary atmosphere I have been involved,
                the main activities I have performed have been:

                * Management of electronic laboratory equipment for the test and
                validation of prototypes or minimum viable
                products.
                * Design and development of software to remotely control electronic
                systems, perform automation and validation
                test and create user-friendly interfaces.
                * Software (or script) development for data acquisition, data
                processing and data analysis.
                * Reporting of issues, results and documentation to the group managers.
                *  Communication of the main conclusions to the scientific community
                 by oral presentation in international
                conferences and/or by published papers in relevant journals of the
                field.

                Regarding my knowledge of different technologies, I have wide
                experience in programming languages like MATLAB,
                Python, C/C++ and LabVIEW and in electrical simulators SPICE-based.
                In addition, I have large practice in
                handling diverse electronic equipment such as oscilloscopes, wave
                generators, arbitrary function generator,
                voltage/current source, analyzers and detectors included in test rigs.
                '''
            )]
        )


def educational_page_content(app: Dash) -> html.Div:
    def _card_content(header: str, title: str, text: str, years: str, image: str):
        content = [dbc.CardHeader(header, class_name="card-header"), dbc.CardBody(
            [html.H5(title, className="card-title"), html.P(
                text, className="card-text", ), html.H6(years, className="card_years")]
            ), html.Div(
            html.Img(
                className="uni_logo", src=app.get_asset_url(image), ), className="uni_logo_container"
            ), ]
        return content

    doctorate = _card_content(
        '2017', 'Electronic engineering and telecommunication Ph.D.', "Universidad autonoma de Barcelona", "2013-2017",
        image=images.UAB_LOGO
        )
    master_elect = _card_content(
        "2013", "Master in micro and nanoelectronics", "Universidad autonoma de Barcelona", "2012-2013",
        image=images.UAB_LOGO
        )
    master_phys = _card_content(
        "2012", "Master in Physics instrumentation", "Universidad de Valladolid", "2011-2012", image=images.UVA_LOGO
        )
    grade = _card_content(
        "2009", "Bachelor in Physics", "Universidad de Salamanca", "2003-2009", image=images.USAL_LOGO
        )

    row_1 = dbc.Row(
        [dbc.Col(dbc.Card(doctorate, color="info", outline=True)),
            dbc.Col(dbc.Card(master_elect, color="info", outline=True)),
            dbc.Col(dbc.Card(master_phys, color="info", outline=True)),
            dbc.Col(dbc.Card(grade, color="info", outline=True)),

            ], className="mb-4", )

    cards = html.Div([row_1])
    return html.Div(
        id="educational_page", className="page_container", children=[html.H1("Educational Background"), cards, ]
        )


def skills_page_content() -> html.Div:
    return html.Div(
        id="skills_page", className="page_container", children=[html.H1("Skills"), ]
        )


def create_contact_field(app: Dash, icon: images, field_text: str) -> html.Div:
    return html.Div(
        className="contact_field", children=[html.Img(
            className="contact_icon", src=app.get_asset_url(icon), ), html.P(field_text), ]
        )


def contact_page_content(app: Dash) -> html.Div:
    return html.Div(
        id="contact_page", className="page_container",
        children=[html.H1("Contact"), create_contact_field(app, images.CONTACT_ICON, "679 156 142"),
            create_contact_field(app, images.HOME_ICON, "Sant Cugat del Valles"),
            create_contact_field(app, images.GMAIL_ICON, "mmaestroizquierdo@gmail.com"),
            create_contact_field(app, images.GITHUB_ICON, "https://github.com/QueennKiiss"), create_contact_field(
                app, images.LINKEDIN_ICON, "https://www.linkedin.com/in/marcosmaestroizquierdo/"
                ), ], )


def content_bar(app: Dash) -> html.Div:
    """ Contains the layer of the content"""
    div = html.Div(
        id="content_section", className="content_container", children=[# professional_page_content(),
            about_page_content(), # educational_page_content(),
            # skills_page_content(),
            # contact_page_content(app),
            ]
        )
    return div


def sidebar(app: Dash) -> html.Div:
    """ Contains the layer of the left sidebar"""
    div = html.Div(
        className="sidebar_container", children=[html.Img(
            className="profile_photo image", src=app.get_asset_url(images.USER_PROFILE), ), dbc.Nav(
            [dbc.NavItem(
                id="navitem_about", className="navitem about", children=dbc.NavLink(
                    id="link_about", className="navlink_text about", children=html.H4("About me", className="text"),
                    href="#about_page", external_link=True, n_clicks=0, )
                ), dbc.NavItem(
                id="navitem_professional", className="navitem professional", style={}, children=dbc.NavLink(
                    id="link_professional", className="navlink_text professional",
                    children=html.H4("Professional", className="text"), active="exact", href="#professional_page",
                    external_link=True, n_clicks=0
                    ), ), dbc.NavItem(
                id="navitem_educational", className="navitem educational", children=dbc.NavLink(
                    id="link_educational", className="navlink_text educational",
                    children=html.H4("Educational", className="text"), href="#educational_page", external_link=True,
                    n_clicks=0
                    )
                ), dbc.NavItem(
                id="navitem_skills", className="navitem skills", children=dbc.NavLink(
                    id="link_skills", className="navlink_text skills", children=html.H4("Skills", className="text"),
                    href="#skills_page", external_link=True, n_clicks=0
                    )
                ), dbc.NavItem(
                id="navitem_contact", className="navitem contact", children=dbc.NavLink(
                    id="link_contact", className="navlink_text contact", children=html.H4("Contact", className="text"),
                    href="#contact_page", external_link=True, n_clicks=0, )
                ), ], vertical=True, pills=True, fill=True, ), ]
        )
    return div


def resume_content(app: Dash) -> html.Div:
    return html.Div(
        className="resume_content_container", children=[sidebar(app), content_bar(app)]
        )


def cover_page(app: Dash) -> html.Div:
    return html.Div(
        className="cover_page_container", children=[html.Div(
            className="cover_page_section_left", children=[html.Div(
                [html.H3("Hi there"), html.H1("I'M MARCOS"), html.H5("SOFTWARE ENGINEER"), dcc.Markdown(
                    '''
                             I am a technology enthusiast and motivated physicist/electronic
                             engineer looking for a professional career change.
                             Last 7 years I have been working in a R&D environment
                             and I have participated in several projects with national
                             and international collaborations.
                             '''
                    ), ], className="headers_container"
                ), html.Div(
                html.Button(
                    id='view_resume button', className='view_resume_button', children='View Resume', n_clicks=0, ),
                className="button_container"
                ), ]
            ), html.Div(
            className="cover_page_section right", children=[html.Img(
                className="cover_profile_photo image", # src=app.get_asset_url(images.USER_PROFILE),
                src=app.get_asset_url(images.COVER_PHOTO), ), ], ), ], )


def main_layout(app: Dash) -> html.Div:
    """ Contains the outer layer of the layout"""
    div = html.Div(
        id='main_page', className="main_body_container", children=[cover_page(app), # resume_content(app),
            ]
        )

    return div
