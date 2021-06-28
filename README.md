# youtube-dl and ffmpeg binaries updater for Windows OS

Updates youtube-dl.exe and ffmpeg binaries (ffmpeg.exe, ffplay.exe and ffprobe.exe) 
with their latest versions.

### INFO Level
```
> python updater.py -f

Updater                   INFO     Starting force update
CodexFfmpegUpdaterTask    INFO     Updating ffmpeg binaries from codex
YTDLUpdaterTask           INFO     Updating youtube-dl.exe
YTDLUpdaterTask           INFO     youtube-dl updated to version 2021.06.06
ZipExtractTask            INFO     [ffmpeg-release-essentials.zip] Extract ffmpeg-4.4-essentials_build/bin/ffmpeg.exe to C:\youtube-dl\ffmpeg.exe
ZipExtractTask            INFO     [ffmpeg-release-essentials.zip] Extract ffmpeg-4.4-essentials_build/bin/ffplay.exe to C:\youtube-dl\ffplay.exe
ZipExtractTask            INFO     [ffmpeg-release-essentials.zip] Extract ffmpeg-4.4-essentials_build/bin/ffprobe.exe to C:\youtube-dl\ffprobe.exe
Updater                   INFO     Force update finished
```

### DEBUG Level
```
> python updater.py -f -p win64 -v3

2021-06-28 19:40:30,845 updater     Updater                   __init__               DEBUG    Initializing Updater
2021-06-28 19:40:30,845 managers    TaskManager               __init__               DEBUG    Initializing TaskManager
2021-06-28 19:40:30,845 updater     Updater                   run                    INFO     Starting force update
2021-06-28 19:40:30,846 abstract    CodexFFAPIClient          __init__               DEBUG    Initializing CodexFFAPIClient
2021-06-28 19:40:30,846 abstract    CodexFfmpegUpdaterTask    __init__               DEBUG    Initializing CodexFfmpegUpdaterTask
2021-06-28 19:40:30,846 extractor   ZipExtractor              __init__               DEBUG    Initializing ZipExtractor
2021-06-28 19:40:30,846 abstract    YouTubeDLAPIClient        __init__               DEBUG    Initializing YouTubeDLAPIClient
2021-06-28 19:40:30,847 abstract    YTDLUpdaterTask           __init__               DEBUG    Initializing YTDLUpdaterTask
2021-06-28 19:40:30,847 abstract    CodexFfmpegUpdaterTask    _update                INFO     Updating ffmpeg binaries from codex
2021-06-28 19:40:30,849 ytdl        YTDLUpdaterTask           _update                INFO     Updating youtube-dl.exe
2021-06-28 19:40:35,080 utils       YTDLUpdaterTask           get_stdout             DEBUG    Command "C:\youtube-dl\youtube-dl.exe --version" exited with returncode 0
2021-06-28 19:40:35,080 ytdl        YTDLUpdaterTask           _print_version         INFO     youtube-dl updated to version 2021.06.06
2021-06-28 19:40:35,081 abstract    YouTubeDLAPIClient        close_session          DEBUG    Closing session
2021-06-28 19:40:42,278 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/
2021-06-28 19:40:42,278 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/bin/
2021-06-28 19:40:42,278 extract     ZipExtractTask            __init__               DEBUG    Initializing ZipExtractTask
2021-06-28 19:40:42,279 extract     ZipExtractTask            __init__               DEBUG    Initializing ZipExtractTask
2021-06-28 19:40:42,279 extract     ZipExtractTask            __init__               DEBUG    Initializing ZipExtractTask
2021-06-28 19:40:42,279 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/
2021-06-28 19:40:42,280 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/bootstrap.min.css
2021-06-28 19:40:42,280 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/default.css
2021-06-28 19:40:42,280 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/developer.html
2021-06-28 19:40:42,280 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/faq.html
2021-06-28 19:40:42,280 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/fate.html
2021-06-28 19:40:42,281 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffmpeg-all.html
2021-06-28 19:40:42,281 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffmpeg-bitstream-filters.html
2021-06-28 19:40:42,281 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffmpeg-codecs.html
2021-06-28 19:40:42,282 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffmpeg-devices.html
2021-06-28 19:40:42,282 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffmpeg-filters.html
2021-06-28 19:40:42,282 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffmpeg-formats.html
2021-06-28 19:40:42,282 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffmpeg-protocols.html
2021-06-28 19:40:42,283 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffmpeg-resampler.html
2021-06-28 19:40:42,283 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffmpeg-scaler.html
2021-06-28 19:40:42,283 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffmpeg-utils.html
2021-06-28 19:40:42,283 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffmpeg.html
2021-06-28 19:40:42,284 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffplay-all.html
2021-06-28 19:40:42,284 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffplay.html
2021-06-28 19:40:42,284 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffprobe-all.html
2021-06-28 19:40:42,285 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/ffprobe.html
2021-06-28 19:40:42,285 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/general.html
2021-06-28 19:40:42,286 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/git-howto.html
2021-06-28 19:40:42,286 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/libavcodec.html
2021-06-28 19:40:42,287 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/libavdevice.html
2021-06-28 19:40:42,287 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/libavfilter.html
2021-06-28 19:40:42,287 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/libavformat.html
2021-06-28 19:40:42,288 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/libavutil.html
2021-06-28 19:40:42,288 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/libswresample.html
2021-06-28 19:40:42,288 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/libswscale.html
2021-06-28 19:40:42,288 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/mailing-list-faq.html
2021-06-28 19:40:42,289 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/nut.html
2021-06-28 19:40:42,289 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/platform.html
2021-06-28 19:40:42,289 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/doc/style.min.css
2021-06-28 19:40:42,289 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/LICENSE
2021-06-28 19:40:42,290 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/presets/
2021-06-28 19:40:42,290 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/presets/libvpx-1080p.ffpreset
2021-06-28 19:40:42,290 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/presets/libvpx-1080p50_60.ffpreset
2021-06-28 19:40:42,290 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/presets/libvpx-360p.ffpreset
2021-06-28 19:40:42,291 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/presets/libvpx-720p.ffpreset
2021-06-28 19:40:42,291 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/presets/libvpx-720p50_60.ffpreset
2021-06-28 19:40:42,291 extractor   ZipExtractor              _get_extract_coros     DEBUG    [ffmpeg-release-essentials.zip] Skip ffmpeg-4.4-essentials_build/README.txt
2021-06-28 19:40:42,301 extract     ZipExtractTask            extract                INFO     [ffmpeg-release-essentials.zip] Extract ffmpeg-4.4-essentials_build/bin/ffmpeg.exe to C:\youtube-dl\ffmpeg.exe
2021-06-28 19:40:42,308 extract     ZipExtractTask            extract                INFO     [ffmpeg-release-essentials.zip] Extract ffmpeg-4.4-essentials_build/bin/ffplay.exe to C:\youtube-dl\ffplay.exe
2021-06-28 19:40:42,322 extract     ZipExtractTask            extract                INFO     [ffmpeg-release-essentials.zip] Extract ffmpeg-4.4-essentials_build/bin/ffprobe.exe to C:\youtube-dl\ffprobe.exe
2021-06-28 19:40:42,809 abstract    CodexFFAPIClient          close_session          DEBUG    Closing session
2021-06-28 19:40:42,810 updater     Updater                   run                    INFO     Force update finished
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
