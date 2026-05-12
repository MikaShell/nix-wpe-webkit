import re

with open("Source/WebKit/UIProcess/Launcher/glib/BubblewrapLauncher.cpp", "r") as f:
    content = f.read()

insertion = """    // Nix Directories
    sandboxArgs.appendVector(Vector<CString>({ "--ro-bind", "@storeDir@", "@storeDir@" }));
    sandboxArgs.appendVector(Vector<CString>({ "--ro-bind-try", "/run/current-system", "/run/current-system" }));
    sandboxArgs.appendVector(Vector<CString>({ "--ro-bind-try", "@driverLink@/lib", "@driverLink@/lib" }));
    sandboxArgs.appendVector(Vector<CString>({ "--ro-bind-try", "@driverLink@/share", "@driverLink@/share" }));

"""

pattern = r'(        sandboxArgs\.append\("--unshare-ipc"\);\n    }\n)'
replacement = r"\1" + insertion
content, count = re.subn(pattern, replacement, content)
assert count == 1, f"Expected 1 match, got {count}"

with open("Source/WebKit/UIProcess/Launcher/glib/BubblewrapLauncher.cpp", "w") as f:
    f.write(content)
