from settings import Settings


def test_basic_settings():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "MyAppTest"
    assert settings.SECRET == "Secret"
