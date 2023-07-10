# Generate Media Info

![PyPI - Downloads](https://img.shields.io/pypi/:period/mediainfo-generator)

This set of scripts and corresponding docker file will process all media files within a folder structure recursively and do one of the following:

* create a mediainfo.json file for each one found and then create a single file that combines them all into one (to simplify processing)
* process the mediainfo.json file that was created and extract a few key properties to simplify reporting and save this to mediainfo.summary.josn

## Ways to run

There are two ways to run the script, one is via installation (pip module) and the3 other is via docker.

### Installation

First step is to install the module via pip

```bash
pip install mediainfo-generator
```

Then you can run it like this

```bash
mediainfo-generator --path.data /mnt/video
```

### Docker

To Generate media info files and consolidated mediainfo.json file run the following command (after building the container)

```bash
docker run --rm -v /path/to/your/video/files:/data media-info --path.data /data
```

**Note:** You can pass an optional argument if you want to change the root folder in the container to scan (defaults to /data)

## Command Line Arguments

```bash

```

## Build

``` bash
git clone https://github.com/ravensorb/mediainfo-generator.git

cd mediainfo-generator/docker
docker build -t media-info . 
```

## Example Output

### Media Info Consolidate File Example

```json
[
  {
    "streams": [
      {
        "index": 0,
        "codec_name": "h264",
        "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
        "profile": "Main",
        "codec_type": "video",
        "codec_tag_string": "[0][0][0][0]",
        "codec_tag": "0x0000",
        "width": 1920,
        "height": 752,
        "coded_width": 1920,
        "coded_height": 752,
        "closed_captions": 0,
        "film_grain": 0,
        "has_b_frames": 2,
        "sample_aspect_ratio": "1:1",
        "display_aspect_ratio": "120:47",
        "pix_fmt": "yuv420p",
        "level": 40,
        "color_range": "tv",
        "color_space": "bt709",
        "color_transfer": "bt709",
        "color_primaries": "bt709",
        "chroma_location": "left",
        "field_order": "progressive",
        "refs": 1,
        "is_avc": "true",
        "nal_length_size": "4",
        "r_frame_rate": "24000/1001",
        "avg_frame_rate": "24000/1001",
        "time_base": "1/1000",
        "start_pts": 7,
        "start_time": "0.007000",
        "bits_per_raw_sample": "8",
        "extradata_size": 43,
        "disposition": {
          "default": 1,
          "dub": 0,
          "original": 0,
          "comment": 0,
          "lyrics": 0,
          "karaoke": 0,
          "forced": 0,
          "hearing_impaired": 0,
          "visual_impaired": 0,
          "clean_effects": 0,
          "attached_pic": 0,
          "timed_thumbnails": 0,
          "captions": 0,
          "descriptions": 0,
          "metadata": 0,
          "dependent": 0,
          "still_image": 0
        },
        "tags": {
          "BPS-eng": "1667533",
          "DURATION-eng": "02:07:01.990000000",
          "NUMBER_OF_FRAMES-eng": "182745",
          "NUMBER_OF_BYTES-eng": "1588740197",
          "_STATISTICS_WRITING_APP-eng": "mkvmerge v52.0.0 ('Secret For The Mad') 64-bit",
          "_STATISTICS_WRITING_DATE_UTC-eng": "2023-04-26 12:14:35",
          "_STATISTICS_TAGS-eng": "BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES"
        }
      },
      {
        "index": 1,
        "codec_name": "opus",
        "codec_long_name": "Opus (Opus Interactive Audio Codec)",
        "codec_type": "audio",
        "codec_tag_string": "[0][0][0][0]",
        "codec_tag": "0x0000",
        "sample_fmt": "fltp",
        "sample_rate": "48000",
        "channels": 6,
        "channel_layout": "5.1",
        "bits_per_sample": 0,
        "initial_padding": 312,
        "r_frame_rate": "0/0",
        "avg_frame_rate": "0/0",
        "time_base": "1/1000",
        "start_pts": -7,
        "start_time": "-0.007000",
        "extradata_size": 27,
        "disposition": {
          "default": 1,
          "dub": 0,
          "original": 0,
          "comment": 0,
          "lyrics": 0,
          "karaoke": 0,
          "forced": 0,
          "hearing_impaired": 0,
          "visual_impaired": 0,
          "clean_effects": 0,
          "attached_pic": 0,
          "timed_thumbnails": 0,
          "captions": 0,
          "descriptions": 0,
          "metadata": 0,
          "dependent": 0,
          "still_image": 0
        },
        "tags": {
          "language": "eng",
          "title": "Opus / 5.1 / 48 kHz / 1152 kbps",
          "BPS-eng": "774388",
          "DURATION-eng": "02:07:09.661000000",
          "NUMBER_OF_FRAMES-eng": "381483",
          "NUMBER_OF_BYTES-eng": "738540139",
          "_STATISTICS_WRITING_APP-eng": "mkvmerge v52.0.0 ('Secret For The Mad') 64-bit",
          "_STATISTICS_WRITING_DATE_UTC-eng": "2023-04-26 12:14:35",
          "_STATISTICS_TAGS-eng": "BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES"
        }
      },
      {
        "index": 2,
        "codec_name": "hdmv_pgs_subtitle",
        "codec_long_name": "HDMV Presentation Graphic Stream subtitles",
        "codec_type": "subtitle",
        "codec_tag_string": "[0][0][0][0]",
        "codec_tag": "0x0000",
        "r_frame_rate": "0/0",
        "avg_frame_rate": "0/0",
        "time_base": "1/1000",
        "start_pts": -7,
        "start_time": "-0.007000",
        "duration_ts": 7629661,
        "duration": "7629.661000",
        "disposition": {
          "default": 1,
          "dub": 0,
          "original": 0,
          "comment": 0,
          "lyrics": 0,
          "karaoke": 0,
          "forced": 0,
          "hearing_impaired": 0,
          "visual_impaired": 0,
          "clean_effects": 0,
          "attached_pic": 0,
          "timed_thumbnails": 0,
          "captions": 0,
          "descriptions": 0,
          "metadata": 0,
          "dependent": 0,
          "still_image": 0
        },
        "tags": {
          "language": "eng",
          "title": "SDH",
          "BPS-eng": "52274",
          "DURATION-eng": "02:04:19.077000000",
          "NUMBER_OF_FRAMES-eng": "2478",
          "NUMBER_OF_BYTES-eng": "48739495",
          "_STATISTICS_WRITING_APP-eng": "mkvmerge v52.0.0 ('Secret For The Mad') 64-bit",
          "_STATISTICS_WRITING_DATE_UTC-eng": "2023-04-26 12:14:35",
          "_STATISTICS_TAGS-eng": "BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES"
        }
      }
    ],
    "format": {
      "filename": "/data/movie.mkv",
      "nb_streams": 3,
      "nb_programs": 0,
      "format_name": "matroska,webm",
      "format_long_name": "Matroska / WebM",
      "start_time": "-0.007000",
      "duration": "7629.661000",
      "size": "2351055609",
      "bit_rate": "2465174",
      "probe_score": 100,
      "tags": {
        "title": "Some Title",
        "creation_time": "2023-04-26T12:14:35.000000Z",
        "ENCODER": "Lavf58.45.100"
      }
    }
  },
  ...
]
```

### Media Info Summary File Examplpe

```json
[
  {
      "filename": "/data/movie.mkv",
      "format": {
        "format_name": "matroska,webm",
        "format_long_name": "Matroska / WebM",
        "bit_rate": "9878670",
        "size": "7725436645",
        "encoder": "libebml v1.4.2 + libmatroska v1.6.4"
      },
      "video": {
        "codec_name": "hevc",
        "codec_long_name": "H.265 / HEVC (High Efficiency Video Coding)",
        "profile": "Main 10",
        "codec_type": "video",
        "coded_width": 3840,
        "coded_height": 1600,
        "avg_frame_rate": "24000/1001"
      },
      "audio": {
        "codec_name": "eac3",
        "codec_long_name": "ATSC A/52B (AC-3, E-AC-3)",
        "profile": null,
        "codec_type": "audio",
        "sample_rate": "48000",
        "channels": 6,
        "channel_layout": "5.1(side)"
      }
    },
    ...
]
```
