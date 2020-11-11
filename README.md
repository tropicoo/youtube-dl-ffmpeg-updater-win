# youtube-dl and ffmpeg binaries updater for Windows OS

Updates youtube-dl.exe and ffmpeg binaries (ffmpeg.exe, ffplay.exe and ffprobe.exe) 
with their latest versions.

### INFO Level
```
> python updater.py -f -p win64

Updater               Starting force update
YTDLUpdaterProcess    Updating youtube-dl.exe
FFUpdaterProcess      Updating ffbinaries
ZipExtractor          [ffplay-4.2.1-win-64.zip] Extracting ffplay.exe to C:\youtube-dl\ffplay.exe
ZipExtractor          [ffmpeg-4.2.1-win-64.zip] Extracting ffmpeg.exe to C:\youtube-dl\ffmpeg.exe
ZipExtractor          [ffprobe-4.2.1-win-64.zip] Extracting ffprobe.exe to C:\youtube-dl\ffprobe.exe
YTDLUpdaterProcess    youtube-dl updated to version 2019.11.22
Updater               Update finished
```

### DEBUG Level
```
> python updater.py -f -p win64 -v3

2019-11-24 00:23:56,897 procs     FFUpdaterProcess-2       FFCompUpdaterProcess  __init__               DEBUG    Initializing <FFCompUpdaterProcess name='FFCompUpdaterProcess-2:3' parent=35808 initial>
2019-11-24 00:23:56,897 extractor FFUpdaterProcess-2       ZipExtractor          __init__               DEBUG    Initializing <core.extractor.ZipExtractor object at 0x035AD580>
2019-11-24 00:23:56,902 procs     FFUpdaterProcess-2       FFCompUpdaterProcess  __init__               DEBUG    Initializing <FFCompUpdaterProcess name='FFCompUpdaterProcess-2:4' parent=35808 initial>
2019-11-24 00:23:56,902 extractor FFUpdaterProcess-2       ZipExtractor          __init__               DEBUG    Initializing <core.extractor.ZipExtractor object at 0x035AD610>
2019-11-24 00:23:57,145 api       BaseManager-1            FFBinariesAPIClient   __make_request         DEBUG    GET https://ffbinaries.com/api/v1/version/latest
2019-11-24 00:23:57,312 api       BaseManager-1            FFBinariesAPIClient   __make_request         DEBUG    GET https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2.1/ffmpeg-4.2.1-win-64.zip
2019-11-24 00:23:57,312 api       BaseManager-1            FFBinariesAPIClient   __make_request         DEBUG    GET https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2.1/ffprobe-4.2.1-win-64.zip
2019-11-24 00:23:57,314 api       BaseManager-1            FFBinariesAPIClient   __make_request         DEBUG    GET https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2.1/ffplay-4.2.1-win-64.zip
2019-11-24 00:24:04,415 extractor FFCompUpdaterProcess-2:4 ZipExtractor          extract                INFO     [ffplay-4.2.1-win-64.zip] Extracting ffplay.exe to C:\youtube-dl\ffplay.exe
2019-11-24 00:24:04,621 extractor FFCompUpdaterProcess-2:3 ZipExtractor          extract                INFO     [ffprobe-4.2.1-win-64.zip] Extracting ffprobe.exe to C:\youtube-dl\ffprobe.exe
2019-11-24 00:24:04,831 extractor FFCompUpdaterProcess-2:2 ZipExtractor          extract                INFO     [ffmpeg-4.2.1-win-64.zip] Extracting ffmpeg.exe to C:\youtube-dl\ffmpeg.exe
2019-11-24 00:24:05,104 extractor FFCompUpdaterProcess-2:4 ZipExtractor          extract                DEBUG    [ffplay-4.2.1-win-64.zip] Skipping __MACOSX/
2019-11-24 00:24:05,104 extractor FFCompUpdaterProcess-2:4 ZipExtractor          extract                DEBUG    [ffplay-4.2.1-win-64.zip] Skipping __MACOSX/._ffplay.exe
2019-11-24 00:24:05,299 extractor FFCompUpdaterProcess-2:3 ZipExtractor          extract                DEBUG    [ffprobe-4.2.1-win-64.zip] Skipping __MACOSX/
2019-11-24 00:24:05,299 extractor FFCompUpdaterProcess-2:3 ZipExtractor          extract                DEBUG    [ffprobe-4.2.1-win-64.zip] Skipping __MACOSX/._ffprobe.exe
2019-11-24 00:24:05,492 extractor FFCompUpdaterProcess-2:2 ZipExtractor          extract                DEBUG    [ffmpeg-4.2.1-win-64.zip] Skipping __MACOSX/
2019-11-24 00:24:05,493 extractor FFCompUpdaterProcess-2:2 ZipExtractor          extract                DEBUG    [ffmpeg-4.2.1-win-64.zip] Skipping __MACOSX/._ffmpeg.exe
2019-11-24 00:24:07,058 procs     YTDLUpdaterProcess-3     YTDLUpdaterProcess    _print_version         INFO     youtube-dl updated to version 2019.11.22
2019-11-24 00:24:07,073 updater   MainProcess              Updater               run                    INFO     Update finished
```

## Requirements
Python 3.7+, requests, ffbinaries-api-client.

## Installation
```
git clone https://github.com/tropicoo/youtube-dl-ffmpeg-updater-win.git
pip3 install -r requirements.txt
```

## Usage
```
> python updater.py -h
usage: updater.py [-h] [-d DESTINATION] [-p {win32,win64}] [-f] [-ff-src {ffbinaries}] [-v [{0,1,2,3}]]

youtube-dl & ffmpeg binaries updater for windows os

optional arguments:
  -h, --help            show this help message and exit
  -d DESTINATION, --destination DESTINATION
                        youtube-dl directory path, default C:\youtube-dl
  -p {win32,win64}, --platform {win32,win64}
                        ffmpeg binaries os platform, default win32
  -f, --force           force update
  -ff-src {ffbinaries}, --ffmpeg-source {ffbinaries}
                        ffbinaries source
  -v [{0,1,2,3}], --verbose [{0,1,2,3}]
                        log level 0-3, default 2
```

## Misc
Easily run as batch file on Windows.

```
:: Content of file "youtube-dl updater.bat"

@echo off

python3 <absolute_path_to_updater.py> -f -p win64 -v3

pause
```
