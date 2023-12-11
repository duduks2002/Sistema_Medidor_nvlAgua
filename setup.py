import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "includes": ["matplotlib", "serial", "csv"],
    "zip_include_packages": ["encodings", "PySide6"],
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="MEDIDOR DE NIVEL DE AGUA",
    version="0.3",
    description="Le a saida serial do sensor e mostra no grafico se está foi alterado o estado do sensor de 0 para vazio e 1 para cheio",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],)