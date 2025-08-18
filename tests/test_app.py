import pytest
from app import app  # imports your Dash app instance


@pytest.mark.parametrize("component_id", ["header", "graph", "region-picker"])
def test_component_presence(dash_duo, component_id):
    """Check that each required component is present."""
    dash_duo.start_server(app)
    element = dash_duo.wait_for_element(f"#{component_id}", timeout=10)
    assert element is not None
