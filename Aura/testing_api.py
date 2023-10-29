import json
import os
import re
import shutil
import time
import os.path
from config import email, password, file_path, frame_id

import requests

# Put Aura email/password here


# You can get your frame id by going to app.auraframes.com
# Log in there and click on "View Photos" underneath your frame
# Then grab the ID from the URL: https://app.auraframes.com/frame/<FRAME ID HERE>


# Main download function
def download_photos_from_aura(email, password, frame_id):
    # define URLs and payload format
    login_url = "https://api.pushd.com/v5/login.json"
    frame_url = f"https://api.pushd.com/v5/frames/{frame_id}/assets.json?side_load_users=false"
    login_payload = {
        # "identifier_for_vendor": "does-not-matter",
        # "client_device_id": "does-not-matter",
        # "app_identifier": "com.pushd.Framelord",
        # "locale": "en",
        "user": {
            "email": email,
            "password": password
        }
    }

    # make login request with credentials
    s = requests.Session()
    r = s.post(login_url, json=login_payload)

    if r.status_code != 200:
        print("Login Error: Check your credentials")
        return 0

    print("Login Success")
    print(json.dumps(r.json(), indent=4,))
    result = r.json
    print(result)

def main():
    download_photos_from_aura(email, password, frame_id)


if __name__ == "__main__":
    main()
