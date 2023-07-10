#!/usr/bin/env python3

import os
import subprocess
import json
import logging 

import json

from mediainfo_generator.utils.settings_utils_v1 import globalSettingsMgr

#######################################################################################################

class MediaInfoScanner:
    def __init__(self):
        self.logger = logging.getLogger("mediainfo_generator")

    #######################################################################################################

    def execute(self):
        self.media_info = []
        self.media_summary_info = []
        self.media_files = []

        self.__scan_folder(globalSettingsMgr.settings.output.individualFiles )
        self.__save_media_info()

        if globalSettingsMgr.settings.output.summaryFile:
            self.__summarize_media_info()
            self.__save_summary_info()
        
        pass 
    
    #######################################################################################################

    def __get_media_info(self, file_path):
        # Run ffprobe command to get media info
        command = ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_format', '-show_streams', file_path]
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Parse the output as JSON
        media_info = json.loads(result.stdout)

        # Remove file_path from filename field
        media_info['format']['filename'] = media_info['format']['filename'].replace(os.path.abspath(globalSettingsMgr.settings.path.data), '')   
        
        return media_info

    def __scan_folder(self, saveIndividualFile: bool = False):
        self.logger.info(f"Scanning folder: {globalSettingsMgr.settings.path.data}")

        # Iterate over files in the folder
        for root, dirs, files in os.walk(globalSettingsMgr.settings.path.data):
            for file in files:
                # Check if the file is a media file
                if file.lower().endswith(('.mp4', '.mkv', '.avi', '.m4v', '.mv4')):
                    file_path = os.path.join(root, file)
                    
                    self.logger.info(f"Processing file: {file_path}")
                    
                    media_info = self.__get_media_info(file_path)

                    if saveIndividualFile:
                        json_file_path = os.path.splitext(file_path)[0] + '.mediainfo.json'

                        if os.path.exists(json_file_path):
                            self.logger.debug(f'Removing existing file: {json_file_path}')
                            os.remove(json_file_path)
                            
                        with open(json_file_path, 'w') as json_file:
                            json.dump(media_info, json_file, indent=4)

                        self.logger.info(f'\tSaved media info for file: "{os.path.basename(file_path)}" to: "{os.path.basename(json_file_path)}"')

                    self.media_files.append(file_path)
                    self.media_info.append(media_info)

        self.logger.info("Scanning completed")

    def __save_media_info(self):
        self.logger.debug(f"Saving media info to: {globalSettingsMgr.settings.path.output}")

        output_file_path = f'{globalSettingsMgr.settings.path.output}/mediainfo.json'

        if os.path.exists(output_file_path):
            self.logger.debug(f'Removing existing file: {output_file_path}')
            os.remove(output_file_path)

        # Save media info to JSON file
        with open(output_file_path, 'w') as output_file:
            json.dump(self.media_info, output_file, indent=4)
                    
        self.logger.info(f'Saved media info to: {output_file_path}')
        
    #######################################################################################################

    def __summarize_media_info(self):
        summary = []
        
        for file_info in self.media_info:
            summary_entry = {
                'filename': file_info['format'].get('filename', ''),
                'format_name': file_info['format'].get('format_name', ''),
                'format_long_name': file_info['format'].get('format_long_name', ''),
                'bit_rate': file_info['format'].get('bit_rate', ''),
                'size': file_info['format'].get('size', ''),
                'encoder': '',
                'video': [],
                'audio': []
            }

            if file_info['format'].get('tags'):
                if file_info['format']['tags'].get('encoder'):
                    summary_entry['encoder'] = file_info['format']['tags']['encoder']
                elif file_info['format']['tags'].get('ENCODER'):
                    summary_entry['encoder'] = file_info['format']['tags']['ENCODER']
            
            for stream in file_info['streams']:

                stream_info = {
                    'codec_name': stream.get('codec_name', ''),
                    'codec_long_name': stream.get('codec_long_name', ''),
                    'profile': stream.get('profile', ''),
                    'codec_type': stream.get('codec_type', ''),
                }
                
                if stream['codec_type'] == 'video':
                    
                    stream_info.update({
                        'coded_width': stream.get('coded_width', ''),
                        'coded_height': stream.get('coded_height', ''),
                        'avg_frame_rate': stream.get('avg_frame_rate', '')
                    })

                    summary_entry['video'].append(stream_info)
                    
                elif stream['codec_type'] == 'audio':
                    stream_info.update({
                        'sample_rate': stream.get('sample_rate', ''),
                        'channels': stream.get('channels', ''),
                        'channel_layout': stream.get('channel_layout', '')
                    })

                    if stream.get('tags'):
                        stream_info.update({
                            'language': stream['tags'].get('language', ''),
                            'title': stream['tags'].get('title', '')
                        })
                
                    summary_entry['audio'].append(stream_info)
            
            summary.append(summary_entry)

        self.media_summary_info = summary

    def __save_summary_info(self):
        self.logger.debug(f"Saving summary info to: {globalSettingsMgr.settings.path.output}")
        
        output_file_path = f'{globalSettingsMgr.settings.path.output}/mediainfo.summary.json'

        if os.path.exists(output_file_path):
            self.logger.debug(f'Removing existing file: {output_file_path}')
            os.remove(output_file_path)

        with open(output_file_path, 'w') as output_file:
            json.dump(self.media_summary_info, output_file, indent=4)

        self.logger.info(f'Saved summary info to: {output_file_path}')

    #######################################################################################################

    # jq '[.[] | [leaf_paths as $path | {"key": $path | join("_"), "value": getpath($path)}] | from_entries]' mediainfo.summary.json | jq -r '(map(keys) | add | unique) as $cols | map(. as $row | $cols | map($row[.])) as $rows | $cols, $rows[] | @csv' > mediainfo.summary.csv