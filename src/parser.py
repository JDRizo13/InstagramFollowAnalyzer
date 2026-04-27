import json
import zipfile
from pathlib import Path


def load_json_from_zip(zip_path: str, target_filename: str):
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        for file_name in zip_file.namelist():
            if file_name.endswith(target_filename):
                with zip_file.open(file_name) as file:
                    return json.load(file)

    raise FileNotFoundError(f"Could not find {target_filename} inside the ZIP.")


def extract_followers(zip_path: str):
    followers = set()

    with zipfile.ZipFile(zip_path, "r") as zip_file:
        for file_name in zip_file.namelist():
            if "followers" in file_name and file_name.endswith(".json"):
                with zip_file.open(file_name) as file:
                    data = json.load(file)

                for item in data:
                    username = item["string_list_data"][0]["value"]
                    followers.add(username.lower())

    return followers


def extract_following(zip_path: str):
    data = load_json_from_zip(zip_path, "following.json")

    following = set()

    for item in data["relationships_following"]:
        username = item["string_list_data"][0]["value"]
        following.add(username.lower())

    return following