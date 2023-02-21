"""
Module containing all the methods to implement callbacks
"""

from dash import Dash, ctx
from dash.dependencies import Input, Output
from source import layout as ly


def show_resume_content(app: Dash) -> None:
    """ callback to show the main content of the resume """
    @app.callback(
        Output('main_page', 'children'),
        Input('view_resume button', 'n_clicks'),
        prevent_initial_call=True)
    def inner_show_resume_content(view_resume_btn_clicks: int):
        if view_resume_btn_clicks > 0:
            return ly.resume_content(app)


def modify_navlink_style(app: Dash) -> None:
    """ callback to modify the style of the tabs in the navlink when press any"""
    @app.callback(
        Output('content_section', 'children'),
        Output('navitem_about', 'style'),
        Output('navitem_professional', 'style'),
        Output('navitem_educational', 'style'),
        Output('navitem_skills', 'style'),
        Output('navitem_contact', 'style'),
        Input('link_professional', 'n_clicks'),
        Input('link_about', 'n_clicks'),
        Input('link_educational', 'n_clicks'),
        Input('link_skills', 'n_clicks'),
        Input('link_contact', 'n_clicks'),
        prevent_initial_call=True,
        )
    def inner_modify_navlink_style(
            professional_click: int, about_click: int, educational_click: int,
            skills_click: int, contact_click: int
            ):
        button_id = ctx.triggered_id if not None else 'No clicks yet'
        pressed_tab_style = {
            'background': 'white',
            # 'border-top': '2px solid darkcyan',
            # 'border-left': '2px solid darkcyan',
            # 'border-bottom': '2px solid darkcyan',
            # 'border-right': '2px solid white',
            }
        if button_id == 'link_about':
            return ly.about_page_content(), pressed_tab_style, {}, {}, {}, {}
        if button_id == 'link_professional':
            return ly.professional_page_content(), {}, pressed_tab_style, {}, {}, {}
        if button_id == 'link_educational':
            return ly.educational_page_content(app), {}, {}, pressed_tab_style, {}, {}
        if button_id == 'link_skills':
            return ly.skills_page_content(), {}, {}, {}, pressed_tab_style, {}
        if button_id == 'link_contact':
            return ly.contact_page_content(app), {}, {}, {}, {}, pressed_tab_style
