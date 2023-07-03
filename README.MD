# Generate Media Info 
This set of scripts and corresponding docker file will process all media files within a folder structure recursively and do one of the following:

* create a mediainfo.json file for each one found and then create a single file that combines them all into one (to simplify processing)
* process the mediainfo.json file that was created and extract a few key properties to simplify reporting

## Build

``` bash
git clone https://github.com/ravensorb/mediainfo-generator.git

cd mediainfo-generator
docker build -t media-info . 
```

## Usage

Generate media info files and consolidated mediainfo.json file.

```bash
docker run --rm -v /path/to/your/video/files:/data media-info -g
```

**Note:
You can pass an optional argument if you want to change the root folder in the container to scan (defaults to /data)**

Summarize media info

```bash
docker run --rm -v /path/to/your/video/files:/data media-info -s
```

**Note:
You can pass an optional argument if you want to change the root folder in the container to scan (defaults to /data) and another for the name of the summarized file to create**