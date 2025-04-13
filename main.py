import os
import argparse
from dotenv import load_dotenv
from settings import Settings
import yaml


def export_envs(environment: str = "dev") -> None:
    env_file_map = {"dev": ".env.dev", "test": ".env.test", "prod": ".env.prod"}

    env_file = env_file_map.get(environment)
    if not env_file:
        raise ValueError(
            f"Unsupported environment: '{environment}'. Choose from {list(env_file_map.keys())}"
        )

    if not os.path.exists(env_file):
        raise FileNotFoundError(f"The environment file '{env_file}' does not exist.")

    with open("secrets.yaml", "r") as file:
        secret = yaml.safe_load(file)
        os.environ["SECRET"] = secret["application"]["password"]

    load_dotenv(dotenv_path=env_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("SECRET: ", settings.SECRET)
