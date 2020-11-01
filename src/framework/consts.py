from pathlib import Path

SERVER_RUNNING_BANNER = """
+----------------------------------------+
|             SERVER WORKS!              |
+----------------------------------------+

Visit http://{host}:{port}

..........................................
"""

DIR_STATIC = (Path(__file__).parent.parent / "static").resolve()

DIR_ASSETS = (DIR_STATIC / "assets").resolve()
# _this_file_path = Path(__file__).resolve()
#
# DIR_FRAMEWORK = _this_file_path.parent.resolve()
#
# DIR_SRC = DIR_FRAMEWORK.parent.resolve()
#
# DIR_REPO = DIR_SRC.parent.resolve()
#
# DIR_STATIC = (DIR_REPO / "static").resolve()
