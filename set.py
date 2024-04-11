from cx_Freeze import setup,Executable
setup(name="HOTEL",version="1.0",author="Abhinav",description="hi",
      executables=[Executable("home.py",icon="icon.ico",shortcutName="hotel",shortcutDir="DesktopFolder")])
