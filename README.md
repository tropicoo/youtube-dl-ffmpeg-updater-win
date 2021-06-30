# youtube-dl and ffmpeg binaries updater for Windows OS

Updates youtube-dl.exe and ffmpeg binaries (ffmpeg.exe, ffplay.exe and ffprobe.exe) from Codex FFmpeg builds (https://www.gyan.dev/ffmpeg/builds)
with their latest versions.

## Example output
```
> python updater.py -f -p win64 -v3

2021-07-01 00:19:47,985 updater     Updater                   __init__                DEBUG    Initializing Updater
2021-07-01 00:19:47,985 managers    TaskManager               __init__                DEBUG    Initializing TaskManager
2021-07-01 00:19:47,985 updater     Updater                   run                     INFO     Starting force update
2021-07-01 00:19:47,985 abstract    YTDLApiClient             __init__                DEBUG    Initializing YTDLApiClient
2021-07-01 00:19:47,985 abstract    YTDLUpdaterTask           __init__                DEBUG    Initializing YTDLUpdaterTask
2021-07-01 00:19:47,985 ytdl        YTDLWebUpdater            __init__                DEBUG    Initializing YTDLWebUpdater
2021-07-01 00:19:47,985 ytdl        YTDLSubprocessUpdater     __init__                DEBUG    Initializing YTDLSubprocessUpdater
2021-07-01 00:19:47,985 abstract    CodexFFAPIClient          __init__                DEBUG    Initializing CodexFFAPIClient
2021-07-01 00:19:47,985 abstract    CodexFfmpegUpdaterTask    __init__                DEBUG    Initializing CodexFfmpegUpdaterTask
2021-07-01 00:19:47,985 extractor   ZipStreamExtractor        __init__                DEBUG    Initializing ZipStreamExtractor
2021-07-01 00:19:47,985 ytdl        YTDLUpdaterTask           _update                 INFO     Updating youtube-dl.exe
2021-07-01 00:19:47,985 ytdl        YTDLWebUpdater            update                  INFO     Updating by youtube-dl web updater
2021-07-01 00:19:47,985 abstract    CodexFfmpegUpdaterTask    _update                 INFO     Updating FFmpeg binaries from codex
2021-07-01 00:19:47,985 codexffmpeg CodexFFAPIClient          zipped_chunks_generator DEBUG    GET https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
2021-07-01 00:19:47,985 codexffmpeg CodexFFAPIClient          zipped_chunks_generator DEBUG    Start download ffmpeg-release-essentials.zip
2021-07-01 00:19:48,892 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    Skip ffmpeg-4.4-essentials_build/
2021-07-01 00:19:48,892 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    Skip ffmpeg-4.4-essentials_build/bin/
2021-07-01 00:19:48,892 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    Write file C:\youtube-dl\ffmpeg.exe
2021-07-01 00:19:52,363 utils       YTDLWebUpdater            get_stdout              DEBUG    Command "C:\youtube-dl\youtube-dl.exe --version" exited with returncode 0
2021-07-01 00:19:52,363 ytdl        YTDLWebUpdater            _print_version          INFO     youtube-dl updated to version 2021.06.06
2021-07-01 00:19:52,363 abstract    YTDLApiClient             close_session           DEBUG    Close client session
2021-07-01 00:19:59,302 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    Write file C:\youtube-dl\ffplay.exe
2021-07-01 00:20:01,677 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    Write file C:\youtube-dl\ffprobe.exe
2021-07-01 00:20:03,739 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    All ffbinaries updated, done zip stream process
2021-07-01 00:20:03,739 abstract    CodexFFAPIClient          close_session           DEBUG    Close client session
2021-07-01 00:20:03,739 updater     Updater                   run                     INFO     Force update finished
```

## Requirements
Python 3.7+.

## Installation
```
git clone https://github.com/tropicoo/youtube-dl-ffmpeg-updater-win.git
pip3 install -r requirements.txt
```

## Usage
```
> python updater.py -h

usage: updater.py [-h] [-c {ytdl,ffmpeg,all}] [-d DESTINATION] [-p {win32,win64}] [-f] [-ff-src {codex}] [-v [{0,1,2,3}]]

youtube-dl & ffmpeg binaries updater for windows os

optional arguments:
  -h, --help            show this help message and exit
  -c {ytdl,ffmpeg,all}, --component {ytdl,ffmpeg,all}
                        updater components to update, default all
  -d DESTINATION, --destination DESTINATION
                        youtube-dl directory path, default C:\youtube-dl
  -p {win32,win64}, --platform {win32,win64}
                        ffmpeg binaries os platform, default win64
  -f, --force           perform force update
  -ff-src {codex}, --ffmpeg-source {codex}
                        ffmpeg binaries source, currently supported only from codex
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
