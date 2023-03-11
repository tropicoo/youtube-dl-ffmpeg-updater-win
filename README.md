## youtube-dl and ffmpeg binaries updater for Windows OS

Updates `youtube-dl.exe` and ffmpeg binaries (`ffmpeg.exe`, `ffplay.exe`
and `ffprobe.exe`) from Codex FFmpeg builds (https://www.gyan.dev/ffmpeg/builds)
with their latest versions.

## Requirements

[Python 3.10+](https://www.python.org/downloads)

## TODO
 - Replace `youtube-dl` with `yt-dlp`

## Installation

```
git clone https://github.com/tropicoo/youtube-dl-ffmpeg-updater-win.git
pip3 install -r requirements.txt
```

## Usage

```
> python updater.py --force --platform win64 --verbose 3

2023-03-11 18:04:31 main        core.main                 main                    INFO     Starting main app
2023-03-11 18:04:31 updater     Updater                   __init__                INFO     Initializing Updater version 0.3
2023-03-11 18:04:31 managers    TaskManager               __init__                DEBUG    Initializing TaskManager
2023-03-11 18:04:31 updater     Updater                   run                     INFO     Starting force update
2023-03-11 18:04:31 abstract    CodexFFAPIClient          __init__                DEBUG    Initializing CodexFFAPIClient
2023-03-11 18:04:31 abstract    CodexFfmpegUpdaterTask    __init__                DEBUG    Initializing CodexFfmpegUpdaterTask
2023-03-11 18:04:31 extractor   ZipStreamExtractor        __init__                DEBUG    Initializing ZipStreamExtractor
2023-03-11 18:04:31 abstract    YTDLApiClient             __init__                DEBUG    Initializing YTDLApiClient
2023-03-11 18:04:31 abstract    YTDLUpdaterTask           __init__                DEBUG    Initializing YTDLUpdaterTask
2023-03-11 18:04:31 ytdl        YTDLWebUpdater            __init__                DEBUG    Initializing YTDLWebUpdater
2023-03-11 18:04:31 ytdl        YTDLSubprocessUpdater     __init__                DEBUG    Initializing YTDLSubprocessUpdater
2023-03-11 18:04:31 abstract    CodexFfmpegUpdaterTask    _update                 INFO     Updating FFmpeg binaries from codex
2023-03-11 18:04:31 codexffmpeg CodexFFAPIClient          zipped_chunks_generator DEBUG    GET https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
2023-03-11 18:04:31 codexffmpeg CodexFFAPIClient          zipped_chunks_generator DEBUG    Start download ffmpeg-release-essentials.zip
2023-03-11 18:04:31 ytdl        YTDLUpdaterTask           _update                 INFO     Updating youtube-dl.exe
2023-03-11 18:04:31 ytdl        YTDLWebUpdater            update                  INFO     Updating by youtube-dl web updater
2023-03-11 18:04:32 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    Skip ffmpeg-6.0-essentials_build/
2023-03-11 18:04:32 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    Skip ffmpeg-6.0-essentials_build/bin/
2023-03-11 18:04:32 extractor   ZipStreamExtractor        _write_file             DEBUG    Write file C:\youtube-dl\ffmpeg.exe
2023-03-11 18:04:34 utils       YTDLWebUpdater            get_stdout              DEBUG    Command "C:\youtube-dl\youtube-dl.exe --version" exited with returncode 0
2023-03-11 18:04:34 ytdl        YTDLWebUpdater            _print_version          INFO     youtube-dl updated to version 2021.12.17
2023-03-11 18:04:34 abstract    YTDLApiClient             close_session           DEBUG    Close client session
2023-03-11 18:05:46 extractor   ZipStreamExtractor        _write_file             DEBUG    Write file C:\youtube-dl\ffplay.exe
2023-03-11 18:05:47 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffmpeg.exe -version" exited with returncode 0
2023-03-11 18:05:47 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffmpeg.exe successfully validated
2023-03-11 18:06:43 extractor   ZipStreamExtractor        _write_file             DEBUG    Write file C:\youtube-dl\ffprobe.exe
2023-03-11 18:06:43 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffplay.exe -version" exited with returncode 0
2023-03-11 18:06:43 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffplay.exe successfully validated
2023-03-11 18:07:30 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffprobe.exe -version" exited with returncode 0
2023-03-11 18:07:30 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffprobe.exe successfully validated
2023-03-11 18:07:30 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    All ffbinaries updated, done zip stream process
2023-03-11 18:07:30 abstract    CodexFFAPIClient          close_session           DEBUG    Close client session
2023-03-11 18:07:30 updater     Updater                   run                     INFO     Force update finished
2023-03-11 18:07:30 main        core.main                 main                    INFO     Exiting main app
```

## Help

```
> python updater.py --help

 Usage: updater.py [OPTIONS]

╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --component      -c         [all|ffmpeg|ytdl]        updater components to update, default all [default: all]                       │
│ --destination    -d         PATH                     youtube-dl directory path [default: C:\youtube-dl]                             │
│ --platform       -p         [win32|win64]            ffmpeg binaries os platform [default: win64]                                   │
│ --force          -f                                  perform force update                                                           │
│ --ffmpeg-source  -fsrc      [codex|ffbinaries]       ffmpeg binaries source; currently, only "codex" is supported [default: codex]  │
│ --verbose        -v         INTEGER RANGE [0<=x<=3]  log level 0-3 [default: 2]                                                     │
│ --help                                               Show this message and exit.                                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Misc

Easily run as batch file `youtube-dl updater.bat` on Windows.

```
:: Content of the file "youtube-dl updater.bat"

@echo off

python3 <absolute_path_to_updater.py> --platform win64 --verbose 3

pause
```
