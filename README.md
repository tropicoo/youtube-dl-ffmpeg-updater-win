youtube-dl and ffmpeg binaries updater for Windows OS
=====================================================
Updates youtube-dl.exe and ffmpeg binaries (ffmpeg.exe, ffplay.exe and ffprobe.exe) 
with latest versions.

```
> python updater.py -f -p x64 -v3
2019-10-12 02:23:27,775 updater   MainProcess              Updater               __init__               DEBUG    Initializing <__main__.Updater object at 0x041B6FD0>
2019-10-12 02:23:27,776 managers  MainProcess              UpdaterProcessManager __init__               DEBUG    Initializing <core.managers.UpdaterProcessManager object at 0x041B6FB0>
2019-10-12 02:23:27,778 updater   MainProcess              Updater               run                    INFO     Performing force update
2019-10-12 02:23:27,780 updater   MainProcess              Updater               run                    INFO     Starting update
2019-10-12 02:23:28,015 api       BaseManager-1            FFBinariesAPIClient   __init__               DEBUG    Initializing <core.api.FFBinariesAPIClient object at 0x04184B70>
2019-10-12 02:23:28,019 procs     MainProcess              FFUpdaterProcess      __init__               DEBUG    Initializing <FFUpdaterProcess(FFUpdaterProcess-2, initial)>
2019-10-12 02:23:28,019 managers  MainProcess              UpdaterProcessManager start_processes        INFO     Starting <FFUpdaterProcess(FFUpdaterProcess-2, initial)>
2019-10-12 02:23:28,022 api       MainProcess              YouTubeDLAPIClient    __init__               DEBUG    Initializing <core.api.YouTubeDLAPIClient object at 0x041D61F0>
2019-10-12 02:23:28,022 procs     MainProcess              YTDLUpdaterProcess    __init__               DEBUG    Initializing <YTDLUpdaterProcess(YTDLUpdaterProcess-3, initial)>
2019-10-12 02:23:28,022 managers  MainProcess              UpdaterProcessManager start_processes        INFO     Starting <YTDLUpdaterProcess(YTDLUpdaterProcess-3, initial)>
2019-10-12 02:23:28,242 procs     YTDLUpdaterProcess-3     YTDLUpdaterProcess    _update                INFO     Updating youtube-dl.exe
2019-10-12 02:23:28,242 api       YTDLUpdaterProcess-3     YouTubeDLAPIClient    _request               DEBUG    GET https://yt-dl.org/latest/youtube-dl.exe
2019-10-12 02:23:28,244 procs     FFUpdaterProcess-2       FFUpdaterProcess      _update                INFO     Updating ffbinaries
2019-10-12 02:23:28,477 procs     FFUpdaterProcess-2       FFCompUpdaterProcess  __init__               DEBUG    Initializing <FFCompUpdaterProcess(FFCompUpdaterProcess-2:2, initial)>
2019-10-12 02:23:28,478 extractor FFUpdaterProcess-2       ZipExtractor          __init__               DEBUG    Initializing <core.extractor.ZipExtractor object at 0x043454B0>
2019-10-12 02:23:28,481 procs     FFUpdaterProcess-2       FFCompUpdaterProcess  __init__               DEBUG    Initializing <FFCompUpdaterProcess(FFCompUpdaterProcess-2:3, initial)>
2019-10-12 02:23:28,481 extractor FFUpdaterProcess-2       ZipExtractor          __init__               DEBUG    Initializing <core.extractor.ZipExtractor object at 0x043455B0>
2019-10-12 02:23:28,483 procs     FFUpdaterProcess-2       FFCompUpdaterProcess  __init__               DEBUG    Initializing <FFCompUpdaterProcess(FFCompUpdaterProcess-2:4, initial)>
2019-10-12 02:23:28,484 extractor FFUpdaterProcess-2       ZipExtractor          __init__               DEBUG    Initializing <core.extractor.ZipExtractor object at 0x04345690>
2019-10-12 02:23:28,723 api       BaseManager-1            FFBinariesAPIClient   _request               DEBUG    GET https://ffbinaries.com/api/v1/version/latest
2019-10-12 02:23:28,931 api       BaseManager-1            FFBinariesAPIClient   _request               DEBUG    GET https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-win-64.zip
2019-10-12 02:23:28,931 api       BaseManager-1            FFBinariesAPIClient   _request               DEBUG    GET https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-win-64.zip
2019-10-12 02:23:28,932 api       BaseManager-1            FFBinariesAPIClient   _request               DEBUG    GET https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffplay-4.2-win-64.zip
2019-10-12 02:23:34,359 extractor FFCompUpdaterProcess-2:3 ZipExtractor          extract                INFO     [ffplay-4.2-win-64.zip] Extracting ffplay.exe to C:\youtube-dl\ffplay.exe
2019-10-12 02:23:34,812 extractor FFCompUpdaterProcess-2:3 ZipExtractor          extract                DEBUG    [ffplay-4.2-win-64.zip] Skipping __MACOSX/
2019-10-12 02:23:34,813 extractor FFCompUpdaterProcess-2:3 ZipExtractor          extract                DEBUG    [ffplay-4.2-win-64.zip] Skipping __MACOSX/._ffplay.exe
2019-10-12 02:23:35,983 extractor FFCompUpdaterProcess-2:4 ZipExtractor          extract                INFO     [ffmpeg-4.2-win-64.zip] Extracting ffmpeg.exe to C:\youtube-dl\ffmpeg.exe
2019-10-12 02:23:36,404 extractor FFCompUpdaterProcess-2:2 ZipExtractor          extract                INFO     [ffprobe-4.2-win-64.zip] Extracting ffprobe.exe to C:\youtube-dl\ffprobe.exe
2019-10-12 02:23:36,438 extractor FFCompUpdaterProcess-2:4 ZipExtractor          extract                DEBUG    [ffmpeg-4.2-win-64.zip] Skipping __MACOSX/
2019-10-12 02:23:36,438 extractor FFCompUpdaterProcess-2:4 ZipExtractor          extract                DEBUG    [ffmpeg-4.2-win-64.zip] Skipping __MACOSX/._ffmpeg.exe
2019-10-12 02:23:36,862 extractor FFCompUpdaterProcess-2:2 ZipExtractor          extract                DEBUG    [ffprobe-4.2-win-64.zip] Skipping __MACOSX/
2019-10-12 02:23:36,862 extractor FFCompUpdaterProcess-2:2 ZipExtractor          extract                DEBUG    [ffprobe-4.2-win-64.zip] Skipping __MACOSX/._ffprobe.exe
2019-10-12 02:23:38,673 updater   MainProcess              Updater               run                    INFO     Update finished
```

Requirements
------------
Python 3.6+, requests, ffbinaries-api-client.

Installation
------------
```
git clone https://github.com/tropicoo/youtube-dl-ffmpeg-updater-win.git
pip3 install requests ffbinaries-api-client
```

Usage
-----
```
> python updater.py -h
usage: updater.py [-h] [-d DESTINATION] [-p {x32,x64}] [-f] [-v [{0,1,2,3}]]

youtube-dl & ffmpeg binaries updater for windows os

optional arguments:
  -h, --help            show this help message and exit
  -d DESTINATION, --destination DESTINATION
                        youtube-dl directory path, default C:\youtube-dl
  -p {x32,x64}, --platform {x32,x64}
                        ffmpeg binaries os platform, default x32
  -f, --force           force update
  -v [{0,1,2,3}], --verbose [{0,1,2,3}]
                        log level 0-3, default 2
```
