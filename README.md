## ffmpeg binaries updater for Windows OS

Updates ffmpeg binaries (`ffmpeg.exe`, `ffplay.exe` and `ffprobe.exe`) from 
Codex FFmpeg builds (https://www.gyan.dev/ffmpeg/builds) with their latest versions.

## Version

Current: 0.4.7

## Requirements

Python 3.12+

## TODO
 - Replace `youtube-dl` with `yt-dlp` since `youtube-dl` is gone.

## Installation

```
git clone https://github.com/tropicoo/youtube-dl-ffmpeg-updater-win.git
pip3 install -r requirements.txt
```

## Usage

```
> python main.py --force --platform win64 --verbose 3

2026-07-23 23:37:57 main            app.cli.main              run_cli                  INFO     


███████╗███████╗███╗   ███╗██████╗ ███████╗ ██████╗     ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██████╗
██╔════╝██╔════╝████╗ ████║██╔══██╗██╔════╝██╔════╝     ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
█████╗  █████╗  ██╔████╔██║██████╔╝█████╗  ██║  ███╗    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██████╔╝
██╔══╝  ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══╝  ██║   ██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ██╔══██╗
██║     ██║     ██║ ╚═╝ ██║██║     ███████╗╚██████╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝     ╚═╝     ╚═╝╚═╝     ╚══════╝ ╚═════╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝



2026-07-23 23:37:57 main            app.cli.main              run_cli                  INFO     Starting main app
2026-07-23 23:37:57 updater         Updater                   __init__                 INFO     Initializing "Updater" version 0.4.7
2026-07-23 23:37:57 managers        TaskManager               __init__                 DEBUG    Initializing "TaskManager"
2026-07-23 23:37:57 updater         Updater                   run                      INFO     Starting force update
2026-07-23 23:37:57 abstract        CodexFFGithubApiClient    __init__                 DEBUG    Initializing "CodexFFGithubApiClient"
2026-07-23 23:37:57 abstract        CodexFfmpegUpdaterTask    __init__                 DEBUG    Initializing "CodexFfmpegUpdaterTask"
2026-07-23 23:37:57 zip_extractor   ZipStreamExtractor        __init__                 DEBUG    Initializing "ZipStreamExtractor"
2026-07-23 23:37:57 abstract        CodexFfmpegUpdaterTask    _update                  INFO     Updating FFmpeg binaries from codex
2026-07-23 23:37:57 client          CodexFFGithubApiClient    _get_latest_tag          DEBUG    GET https://github.com/GyanD/codexffmpeg/releases/latest
2026-07-23 23:37:57 client          CodexFFGithubApiClient    download_latest_version  INFO     Latest version: "8.1.2"
2026-07-23 23:37:57 client          CodexFFGithubApiClient    zipped_chunks_generator  DEBUG    GET https://github.com/GyanD/codexffmpeg/releases/download/8.1.2/ffmpeg-8.1.2-essentials_build.zip
2026-07-23 23:37:57 client          CodexFFGithubApiClient    zipped_chunks_generator  DEBUG    Start download ffmpeg-8.1.2-essentials_build.zip
2026-07-23 23:37:58 zip_extractor   ZipStreamExtractor        process_zip_stream       DEBUG    Skip ffmpeg-8.1.2-essentials_build/
2026-07-23 23:37:58 zip_extractor   ZipStreamExtractor        process_zip_stream       DEBUG    Skip ffmpeg-8.1.2-essentials_build/bin/
2026-07-23 23:37:58 zip_extractor   ZipStreamExtractor        _write_file              DEBUG    Write file C:\youtube-dl\ffmpeg.exe
2026-07-23 23:37:59 zip_extractor   ZipStreamExtractor        _write_file              DEBUG    Write file C:\youtube-dl\ffplay.exe
2026-07-23 23:38:00 utils           FFmpegBinValidationTask   get_stdout               DEBUG    Command "('C:/youtube-dl/ffmpeg.exe', '-version')" exited with returncode 0
2026-07-23 23:38:00 validation      FFmpegBinValidationTask   validate                 INFO     C:\youtube-dl\ffmpeg.exe successfully validated
2026-07-23 23:38:00 zip_extractor   ZipStreamExtractor        _write_file              DEBUG    Write file C:\youtube-dl\ffprobe.exe
2026-07-23 23:38:01 utils           FFmpegBinValidationTask   get_stdout               DEBUG    Command "('C:/youtube-dl/ffplay.exe', '-version')" exited with returncode 0
2026-07-23 23:38:01 validation      FFmpegBinValidationTask   validate                 INFO     C:\youtube-dl\ffplay.exe successfully validated
2026-07-23 23:38:03 utils           FFmpegBinValidationTask   get_stdout               DEBUG    Command "('C:/youtube-dl/ffprobe.exe', '-version')" exited with returncode 0
2026-07-23 23:38:03 validation      FFmpegBinValidationTask   validate                 INFO     C:\youtube-dl\ffprobe.exe successfully validated
2026-07-23 23:38:03 zip_extractor   ZipStreamExtractor        process_zip_stream       INFO     All ffbinaries updated, zip stream process done
2026-07-23 23:38:03 abstract        CodexFFGithubApiClient    close_session            DEBUG    Close client session
2026-07-23 23:38:03 updater         Updater                   run                      INFO     Force update finished
2026-07-23 23:38:03 main            app.cli.main              run_cli                  INFO     Exiting main app
```

## Help

```
> python main.py --help

 Usage: main.py [OPTIONS]

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --component      -c         <ffmpeg>            updater components to update; currently, only "ffmpeg" is supported [default: ffmpeg] │
│ --destination    -d         <path>              ffmpeg destination directory path [default: C:\youtube-dl]                            │
│ --platform       -p         <win32|win64>       ffmpeg binaries os platform [default: win64]                                          │
│ --force          -f                             perform force update                                                                  │
│ --ffmpeg-source  -fsrc      <codex|ffbinaries>  ffmpeg binaries source; currently, only "codex" is supported [default: codex]         │
│ --codex--source  -csrc      <github|codex>      codex binaries download source [default: github]                                      │
│ --verbose        -v         <0|1|2|3>           log level 0-3 [default: 2]                                                            │
│ --help                                          Show this message and exit.                                                           │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Misc

Easily run as batch file `ffmpeg-updater.bat` on Windows.

```
:: Content of the file "`ffmpeg-updater.bat"

@echo off

python3 <absolute_path_to_main.py> --platform win64 --verbose 3

pause
```
