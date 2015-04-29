#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    env = os.environ.get("LK_ENV", None)
    if env:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.%s" % os.environ["LK_ENV"])
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
