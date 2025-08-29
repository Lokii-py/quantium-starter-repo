from src.app import app

"""
This function will test the presence of header text in the web browser.
"""
def test_header_presence(dash_duo):
    dash_duo.start_server(app)
    header_element = dash_duo.find_element("h1")

    assert header_element.text == "Soul Foods: Pink Morsel Sales Summary DashBoard"

"""
Check if the graph is working or not.
"""
def test_graph_presence(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.wait_for_element("#sales-line-chart svg", timeout=10)
    
    assert graph.is_displayed()

"""
Check the presence of region picker in the dashboard"""
def test_region_picker_presence(dash_duo):
    dash_duo.start_server(app)
    region = dash_duo.find_element("#region")

    assert region.is_displayed()