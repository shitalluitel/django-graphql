import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dummy_settings")
    from django.core.management import execute_from_command_line  # noqa

    args = sys.argv + ["test"]
    execute_from_command_line(args)
