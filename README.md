# youtube-dl and ffmpeg binaries updater for Windows OS

Updates `youtube-dl.exe` and ffmpeg binaries (`ffmpeg.exe`, `ffplay.exe`
and `ffprobe.exe`) from Codex FFmpeg builds (https://www.gyan.dev/ffmpeg/builds)
with their latest versions.

## Requirements

[Python 3.10+](https://www.python.org/downloads)

## Installation

```
git clone https://github.com/tropicoo/youtube-dl-ffmpeg-updater-win.git
pip3 install -r requirements.txt
```

## Usage

```bash
> python updater.py --force --platform win64 --verbose 3

2021-07-01 19:52:08,937 updater     Updater                   __init__                DEBUG    Initializing Updater
2021-07-01 19:52:08,938 managers    TaskManager               __init__                DEBUG    Initializing TaskManager
2021-07-01 19:52:08,938 updater     Updater                   run                     INFO     Starting force update
2021-07-01 19:52:08,938 abstract    CodexFFAPIClient          __init__                DEBUG    Initializing CodexFFAPIClient
2021-07-01 19:52:08,938 abstract    CodexFfmpegUpdaterTask    __init__                DEBUG    Initializing CodexFfmpegUpdaterTask
2021-07-01 19:52:08,938 extractor   ZipStreamExtractor        __init__                DEBUG    Initializing ZipStreamExtractor
2021-07-01 19:52:08,938 abstract    YTDLApiClient             __init__                DEBUG    Initializing YTDLApiClient
2021-07-01 19:52:08,938 abstract    YTDLUpdaterTask           __init__                DEBUG    Initializing YTDLUpdaterTask
2021-07-01 19:52:08,938 ytdl        YTDLWebUpdater            __init__                DEBUG    Initializing YTDLWebUpdater
2021-07-01 19:52:08,939 ytdl        YTDLSubprocessUpdater     __init__                DEBUG    Initializing YTDLSubprocessUpdater
2021-07-01 19:52:08,939 abstract    CodexFfmpegUpdaterTask    _update                 INFO     Updating FFmpeg binaries from codex
2021-07-01 19:52:08,939 codexffmpeg CodexFFAPIClient          zipped_chunks_generator DEBUG    GET https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
2021-07-01 19:52:08,939 codexffmpeg CodexFFAPIClient          zipped_chunks_generator DEBUG    Start download ffmpeg-release-essentials.zip
2021-07-01 19:52:08,942 ytdl        YTDLUpdaterTask           _update                 INFO     Updating youtube-dl.exe
2021-07-01 19:52:08,942 ytdl        YTDLWebUpdater            update                  INFO     Updating by youtube-dl web updater
2021-07-01 19:52:09,840 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    Skip ffmpeg-4.4-essentials_build/
2021-07-01 19:52:09,841 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    Skip ffmpeg-4.4-essentials_build/bin/
2021-07-01 19:52:09,841 extractor   ZipStreamExtractor        _write_file             DEBUG    Write file C:\youtube-dl\ffmpeg.exe
2021-07-01 19:52:11,660 utils       YTDLWebUpdater            get_stdout              DEBUG    Command "C:\youtube-dl\youtube-dl.exe --version" exited with returncode 0
2021-07-01 19:52:11,660 ytdl        YTDLWebUpdater            _print_version          INFO     youtube-dl updated to version 2021.06.06
2021-07-01 19:52:11,660 abstract    YTDLApiClient             close_session           DEBUG    Close client session
2021-07-01 19:52:19,764 extractor   ZipStreamExtractor        _write_file             DEBUG    Write file C:\youtube-dl\ffplay.exe
2021-07-01 19:52:20,350 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffmpeg.exe -version" exited with returncode 0
2021-07-01 19:52:20,350 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffmpeg.exe successfully validated
2021-07-01 19:52:21,999 extractor   ZipStreamExtractor        _write_file             DEBUG    Write file C:\youtube-dl\ffprobe.exe
2021-07-01 19:52:22,531 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffplay.exe -version" exited with returncode 0
2021-07-01 19:52:22,531 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffplay.exe successfully validated
2021-07-01 19:52:24,479 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffprobe.exe -version" exited with returncode 0
2021-07-01 19:52:24,479 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffprobe.exe successfully validated
2021-07-01 19:52:24,479 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    All ffbinaries updated, done zip stream process
2021-07-01 19:52:24,479 abstract    CodexFFAPIClient          close_session           DEBUG    Close client session
2021-07-01 19:52:24,480 updater     Updater                   run                     INFO     Force update finished
```

## Misc

Easily run as batch file `youtube-dl updater.bat` on Windows.

```
:: Content of file "youtube-dl updater.bat"

@echo off

python3 <absolute_path_to_updater.py> --platform win64 --verbose 3

pause
```

## Help

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
