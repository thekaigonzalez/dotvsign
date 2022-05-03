import json
import pathlib

import requests

from vsign.parserVersions import parse_v1, parse_v2, parse_v3

from termcolor import cprint


class VSign:
    """
    The base class for storing, reading, and writing VSign.

    This is the official class.
    """

    def __init__(self, url, support_url="https://github.com") -> None:
        """
        support_url = Download URL
        url = The URL to read version info from (latest)

        
        """
        self.url = url
        self.parser = "v3"
        self.dlurl = support_url

    def validate_vsign(self) -> bool:
        return pathlib.Path(".vsign").exists()

    def get_local_version(self):
        f = open(".vsign", "r")

        v = f.read()

        f.close()

        return v

    def get_web_latest_version(self):
        return json.loads(requests.get(
            self.url).text)["tag_name"]  #TODO: allow multiple formats

    def set_spec(self, ver):
        self.parser = ver

    def compare_vsign(self):
        if (self.parser == "v1"):
            if (parse_v1(self.get_local_version()) < parse_v1(
                    self.get_web_latest_version())):
                print("This version is not up to date!")
                cprint("you can get the latest versions here: " + self.dlurl,
                       "white",
                       attrs=["dark"])
        elif (self.parser == "v2"):
            if (parse_v2(self.get_local_version()) != parse_v2(
                    self.get_web_latest_version())):
                print("This version is not up to date!")
                cprint("you can get the latest versions here: " + self.dlurl,
                       "white",
                       attrs=["dark"])
        elif self.parser == "v3":
            if (parse_v3(self.get_local_version()) < parse_v3(
                    self.get_web_latest_version())):
                print("This version is not up to date!")
                cprint("you can get the latest versions here: " + self.dlurl,
                       "white",
                       attrs=["dark"])

    def get_integer_local(self):
        if (self.parser == "v3"): return parse_v3(self.get_local_version())