from moon.config import Settings, get_settings


def test_settings_defaults():
    settings = get_settings()

    assert isinstance(settings, Settings)
    assert settings.app_name == "Moon MCP Server"
    assert settings.host == "0.0.0.0"
    assert settings.port == 8000
