## youtube-dl and ffmpeg binaries updater for Windows OS

Updates `youtube-dl.exe` and ffmpeg binaries (`ffmpeg.exe`, `ffplay.exe`
and `ffprobe.exe`) from Codex FFmpeg builds (https://www.gyan.dev/ffmpeg/builds)
with their latest versions.

## Requirements

[Python 3.10+](https://www.python.org/downloads)

## TODO
 - Replace `youtube-dl` with `yt-dlp` since `youtube-dl` is gone.

## Installation

```
git clone https://github.com/tropicoo/youtube-dl-ffmpeg-updater-win.git
pip3 install -r requirements.txt
```

## Usage

```
> python updater.py --force --platform win64 --verbose 3

2023-03-12 19:38:45 main        core.main                 main                    INFO     Starting main app
2023-03-12 19:38:45 updater     Updater                   __init__                INFO     Initializing Updater version 0.3
2023-03-12 19:38:45 managers    TaskManager               __init__                DEBUG    Initializing TaskManager
2023-03-12 19:38:45 updater     Updater                   run                     INFO     Starting force update
2023-03-12 19:38:45 abstract    CodexFFGithubApiClient    __init__                DEBUG    Initializing CodexFFGithubApiClient
2023-03-12 19:38:45 abstract    CodexFfmpegUpdaterTask    __init__                DEBUG    Initializing CodexFfmpegUpdaterTask
2023-03-12 19:38:45 extractor   ZipStreamExtractor        __init__                DEBUG    Initializing ZipStreamExtractor
2023-03-12 19:38:45 abstract    YTDLApiClient             __init__                DEBUG    Initializing YTDLApiClient
2023-03-12 19:38:45 abstract    YTDLUpdaterTask           __init__                DEBUG    Initializing YTDLUpdaterTask
2023-03-12 19:38:45 youtube_dl  YTDLWebUpdater            __init__                DEBUG    Initializing YTDLWebUpdater
2023-03-12 19:38:45 youtube_dl  YTDLSubprocessUpdater     __init__                DEBUG    Initializing YTDLSubprocessUpdater
2023-03-12 19:38:45 abstract    CodexFfmpegUpdaterTask    _update                 INFO     Updating FFmpeg binaries from codex
2023-03-12 19:38:45 codexffmpeg CodexFFGithubApiClient    _get_latest_tag         DEBUG    GET https://github.com/GyanD/codexffmpeg/releases/latest
2023-03-12 19:38:45 youtube_dl  YTDLUpdaterTask           _update                 INFO     Updating youtube-dl.exe
2023-03-12 19:38:45 youtube_dl  YTDLWebUpdater            update                  INFO     Updating by youtube-dl web updater
2023-03-12 19:38:46 codexffmpeg CodexFFGithubApiClient    zipped_chunks_generator DEBUG    GET https://github.com/GyanD/codexffmpeg/releases/download/6.0/ffmpeg-6.0-essentials_build.zip
2023-03-12 19:38:46 codexffmpeg CodexFFGithubApiClient    zipped_chunks_generator DEBUG    Start download ffmpeg-6.0-essentials_build.zip
2023-03-12 19:38:46 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    Skip ffmpeg-6.0-essentials_build/
2023-03-12 19:38:46 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    Skip ffmpeg-6.0-essentials_build/bin/
2023-03-12 19:38:46 extractor   ZipStreamExtractor        _write_file             DEBUG    Write file C:\youtube-dl\ffmpeg.exe
2023-03-12 19:38:48 utils       YTDLWebUpdater            get_stdout              DEBUG    Command "C:\youtube-dl\youtube-dl.exe --version" exited with returncode 0
2023-03-12 19:38:48 youtube_dl  YTDLWebUpdater            _print_version          INFO     youtube-dl updated to version 2021.12.17
2023-03-12 19:38:48 abstract    YTDLApiClient             close_session           DEBUG    Close client session
2023-03-12 19:39:18 extractor   ZipStreamExtractor        _write_file             DEBUG    Write file C:\youtube-dl\ffplay.exe
2023-03-12 19:39:18 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffmpeg.exe -version" exited with returncode 0
2023-03-12 19:39:18 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffmpeg.exe successfully validated
2023-03-12 19:40:08 extractor   ZipStreamExtractor        _write_file             DEBUG    Write file C:\youtube-dl\ffprobe.exe
2023-03-12 19:40:09 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffplay.exe -version" exited with returncode 0
2023-03-12 19:40:09 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffplay.exe successfully validated
2023-03-12 19:40:58 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffprobe.exe -version" exited with returncode 0
2023-03-12 19:40:58 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffprobe.exe successfully validated
2023-03-12 19:40:58 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    All ffbinaries updated, done zip stream process
2023-03-12 19:38:48 abstract    YTDLApiClient             close_session           DEBUG    Close client session
2023-03-12 19:39:18 extractor   ZipStreamExtractor        _write_file             DEBUG    Write file C:\youtube-dl\ffplay.exe
2023-03-12 19:39:18 extractor   ZipStreamExtractor        _write_file             DEBUG    Write file C:\youtube-dl\ffplay.exe
2023-03-12 19:39:18 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffmpeg.exe -version" exited with returncode 0
2023-03-12 19:39:18 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffmpeg.exe -version" exited with returncode 0
2023-03-12 19:39:18 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffmpeg.exe successfully validated
2023-03-12 19:40:08 extractor   ZipStreamExtractor        _write_file             DEBUG    Write file C:\youtube-dl\ffprobe.exe
2023-03-12 19:40:09 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffplay.exe -version" exited with returncode 0
2023-03-12 19:40:09 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffplay.exe successfully validated
2023-03-12 19:40:08 extractor   ZipStreamExtractor        _write_file             DEBUG    Write file C:\youtube-dl\ffprobe.exe
2023-03-12 19:40:09 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffplay.exe -version" exited with returncode 0
2023-03-12 19:40:09 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffplay.exe successfully validated
2023-03-12 19:40:58 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffprobe.exe -version" exited with returncode 0
2023-03-12 19:40:58 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffprobe.exe successfully validated
2023-03-12 19:40:58 utils       FFmpegBinValidationTask   get_stdout              DEBUG    Command "C:\youtube-dl\ffprobe.exe -version" exited with returncode 0
2023-03-12 19:40:58 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffprobe.exe successfully validated
2023-03-12 19:40:58 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    All ffbinaries updated, done zip stream process
2023-03-12 19:40:58 abstract    CodexFFGithubApiClient    close_session           DEBUG    Close client session
2023-03-12 19:40:58 updater     Updater                   run                     INFO     Force update finished
2023-03-12 19:40:58 main        core.main                 main                    INFO     Exiting main app
2023-03-12 19:40:58 validation  FFmpegBinValidationTask   validate                INFO     C:\youtube-dl\ffprobe.exe successfully validated
2023-03-12 19:40:58 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    All ffbinaries updated, done zip stream process
2023-03-12 19:40:58 abstract    CodexFFGithubApiClient    close_session           DEBUG    Close client session
2023-03-12 19:40:58 updater     Updater                   run                     INFO     Force update finished
2023-03-12 19:40:58 main        core.main                 main                    INFO     Exiting main app
2023-03-12 19:40:58 extractor   ZipStreamExtractor        process_zip_stream      DEBUG    All ffbinaries updated, done zip stream process
2023-03-12 19:40:58 abstract    CodexFFGithubApiClient    close_session           DEBUG    Close client session
2023-03-12 19:40:58 updater     Updater                   run                     INFO     Force update finished
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
│ --codex--source  -csrc      [github|codex]           codex binaries download source [default: github]                               │
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
