[Setup]
AppName=YCDCT99
AppVersion=1.0.0
DefaultDirName={pf}\YCDCT99
DefaultGroupName=YCDCT99
OutputBaseFilename=YCDCT99-Setup
Compression=lzma
SolidCompression=yes
SetupIconFile=icon.ico

[Files]
Source: "dist\ycdct99.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\YCDCT99"; Filename: "{app}\ycdct99.exe"
Name: "{commondesktop}\YCDCT99"; Filename: "{app}\ycdct99.exe"
