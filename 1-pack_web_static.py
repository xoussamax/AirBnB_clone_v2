#!/usr/bin/python3
from fabric import task
import os
from datetime import datetime

@task
def do_pack(ctx):
    """Create a .tgz archive from the contents of the web_static folder."""
    if not os.path.exists("versions"):
        os.makedirs("versions")

    dt = datetime.utcnow()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )
    archive_path = os.path.join("versions", archive_name)

    try:
        print("Packing web_static to {}".format(archive_path))
        ctx.run("tar -cvzf {} web_static".format(archive_path))
        size = os.stat(archive_path).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_path, size))
        return archive_path
    except Exception as e:
        print("Error creating archive:", str(e))
        return None
