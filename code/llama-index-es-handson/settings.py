from dotenv import dotenv_values


class Settings:
    @staticmethod
    def config() -> dict[str, str | None]:
        config_env = dotenv_values(".env")
        return config_env
