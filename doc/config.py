from django.conf import settings
import os, json

def get():
    config_path = "%s/config.json" % settings.BASE_DIR
    print "[DEBUG] Config file path: %s" % config_path

    config_file = open(config_path, "rw+").read()
    print "[DEBUG] Config file: %s" % config_file

    json_config = json.loads(config_file)
    return json_config
