youtube-dl and ffmpeg binaries updater for Windows OS
=====================================================
Updates youtube-dl.exe and ffmpeg binaries (ffmpeg.exe, ffplay.exe and ffprobe.exe) 
with latest versions.

```
> python updater.py -f -p x64
2019-10-11 02:43:48,734 updater   MainProcess            Updater                   __init__   DEBUG    Initializing <__main__.Updater object at 0x02EEE1D0>
2019-10-11 02:43:48,734 managers  MainProcess            UpdaterProcessManager     __init__   DEBUG    Initializing <core.managers.UpdaterProcessManager object at 0x03574F50>
2019-10-11 02:43:48,736 updater   MainProcess            Updater                   run        INFO     Starting update
2019-10-11 02:43:48,739 updater   MainProcess            Updater                   run        INFO     Performing force update
2019-10-11 02:43:48,995 api       BaseManager-1          FFBinariesAPIClient       __init__   DEBUG    Initializing <core.api.FFBinariesAPIClient object at 0x0436F490>
2019-10-11 02:43:48,998 procs     MainProcess            FFUpdaterProcess          __init__   DEBUG    Initializing <FFUpdaterProcess(FFUpdaterProcess-2, initial)>
2019-10-11 02:43:48,998 managers  MainProcess            UpdaterProcessManager     start_processes INFO     Starting <FFUpdaterProcess(FFUpdaterProcess-2, initial)>
2019-10-11 02:43:49,002 api       MainProcess            YouTubeDLAPIClient        __init__   DEBUG    Initializing <core.api.YouTubeDLAPIClient object at 0x03595070>
2019-10-11 02:43:49,002 procs     MainProcess            YTDLUpdaterProcess        __init__   DEBUG    Initializing <YTDLUpdaterProcess(YTDLUpdaterProcess-3, initial)>
2019-10-11 02:43:49,003 managers  MainProcess            UpdaterProcessManager     start_processes INFO     Starting <YTDLUpdaterProcess(YTDLUpdaterProcess-3, initial)>
2019-10-11 02:43:49,276 procs     FFUpdaterProcess-2     FFUpdaterProcess          _update    INFO     Updating ffbinaries
2019-10-11 02:43:49,295 procs     YTDLUpdaterProcess-3   YTDLUpdaterProcess        _update    INFO     Updating youtube-dl.exe
2019-10-11 02:43:49,295 api       YTDLUpdaterProcess-3   YouTubeDLAPIClient        _request   DEBUG    GET https://yt-dl.org/latest/youtube-dl.exe
2019-10-11 02:43:49,508 procs     FFUpdaterProcess-2     FFComponentUpdaterProcess __init__   DEBUG    Initializing <FFComponentUpdaterProcess(FFComponentUpdaterProcess-2:2, initial)>
2019-10-11 02:43:49,509 extractor FFUpdaterProcess-2     ZipExtractor              __init__   DEBUG    Initializing <core.extractor.ZipExtractor object at 0x03F3FD30>
2019-10-11 02:43:49,514 procs     FFUpdaterProcess-2     FFComponentUpdaterProcess __init__   DEBUG    Initializing <FFComponentUpdaterProcess(FFComponentUpdaterProcess-2:3, initial)>
2019-10-11 02:43:49,515 extractor FFUpdaterProcess-2     ZipExtractor              __init__   DEBUG    Initializing <core.extractor.ZipExtractor object at 0x03F3FE30>
2019-10-11 02:43:49,518 procs     FFUpdaterProcess-2     FFComponentUpdaterProcess __init__   DEBUG    Initializing <FFComponentUpdaterProcess(FFComponentUpdaterProcess-2:4, initial)>
2019-10-11 02:43:49,519 extractor FFUpdaterProcess-2     ZipExtractor              __init__   DEBUG    Initializing <core.extractor.ZipExtractor object at 0x03F3FEF0>
2019-10-11 02:43:49,788 api       BaseManager-1          FFBinariesAPIClient       _request   DEBUG    GET https://ffbinaries.com/api/v1/version/latest
2019-10-11 02:43:49,952 api       BaseManager-1          FFBinariesAPIClient       _request   DEBUG    GET https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffmpeg-4.2-win-64.zip
2019-10-11 02:43:49,952 api       BaseManager-1          FFBinariesAPIClient       _request   DEBUG    GET https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffprobe-4.2-win-64.zip
2019-10-11 02:43:49,952 api       BaseManager-1          FFBinariesAPIClient       _request   DEBUG    GET https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2/ffplay-4.2-win-64.zip
2019-10-11 02:43:58,547 extractor FFComponentUpdaterProcess-2:2 ZipExtractor              extract    INFO     Extracting ffprobe.exe to C:\youtube-dl\ffprobe.exe
2019-10-11 02:43:58,582 extractor FFComponentUpdaterProcess-2:3 ZipExtractor              extract    INFO     Extracting ffmpeg.exe to C:\youtube-dl\ffmpeg.exe
2019-10-11 02:43:58,637 extractor FFComponentUpdaterProcess-2:4 ZipExtractor              extract    INFO     Extracting ffplay.exe to C:\youtube-dl\ffplay.exe
2019-10-11 02:43:58,979 extractor FFComponentUpdaterProcess-2:2 ZipExtractor              extract    DEBUG    Skipping __MACOSX/
2019-10-11 02:43:58,980 extractor FFComponentUpdaterProcess-2:2 ZipExtractor              extract    DEBUG    Skipping __MACOSX/._ffprobe.exe
2019-10-11 02:43:59,006 extractor FFComponentUpdaterProcess-2:3 ZipExtractor              extract    DEBUG    Skipping __MACOSX/
2019-10-11 02:43:59,006 extractor FFComponentUpdaterProcess-2:3 ZipExtractor              extract    DEBUG    Skipping __MACOSX/._ffmpeg.exe
2019-10-11 02:43:59,054 extractor FFComponentUpdaterProcess-2:4 ZipExtractor              extract    DEBUG    Skipping __MACOSX/
2019-10-11 02:43:59,055 extractor FFComponentUpdaterProcess-2:4 ZipExtractor              extract    DEBUG    Skipping __MACOSX/._ffplay.exe
2019-10-11 02:44:07,903 updater   MainProcess            Updater                   run        INFO     Update finished
```

Requirements
------------
Python 3, requests.

Installation
------------
```
git clone https://github.com/tropicoo/youtube-dl-ffmpeg-updater-win.git
pip3 install requests
```

Usage
-----
> Default platform is x32

> Default destination (extract) directory is C:\youtube-dl
```
> python updater.py -h
usage: updater.py [-h] [-d EXTRACT_PATH] [-p {x32,x64}] [-f]

youtube-dl & ffmpeg binaries updater for windows

optional arguments:
  -h, --help            show this help message and exit
  -d EXTRACT_PATH, --destination EXTRACT_PATH
                        youtube-dl directory path
  -p {x32,x64}, --platform {x32,x64}
                        ffmpeg binaries os platform
  -f, --force           force update
```
