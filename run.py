"""
Service running module
"""
import json

import sys
import argparse
from aiohttp import web

from orbbec_mjpeg_streamer.app import create_app


def get_config_files():
    """
    Gets configuration profile name

    Returns:
        tuple (service_config)

    """
    parser = argparse.ArgumentParser(description='orbbec-mjpeg-streamer service')
    parser.add_argument(
        '--config',
        help='configuration file name',
        type=str,
        default='/etc/cam1/orbbec-mjpeg-streamer/orbbec-mjpeg-streamer.json') 
    args, _ = parser.parse_known_args()

    if not args.config:
        parser.print_usage()
        sys.exit(1)
    return args.config


if __name__ == '__main__':
    config_file = get_config_files()

    with open(config_file) as f:
        config = json.load(f)
    app = create_app(config=config)
    web.run_app(
        app,
        host=config['host'],
        port=config['port'],
        access_log_format=config.get('access_log_format')
    )
