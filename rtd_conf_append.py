# Appended to scientific-python-lectures/conf.py by the Read the Docs build
# (post_create_environment). Kept in a separate file to avoid shell quoting
# issues in .readthedocs.yaml job commands.
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
extensions.append("fix_target_notes_crash")
