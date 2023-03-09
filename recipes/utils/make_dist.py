#! /usr/bin/env python3
# coding: utf-8
# This file is derived from make_it_for_release_enunu.py.
# Original Copyright (c) 2020-2021 oatsu
# Copyright (c) 2020-2023 taroushirani

import argparse
import logging
from glob import glob
from jinja2 import Environment, FileSystemLoader
import os
from os.path import basename, dirname, join, expanduser, isabs, isdir
from sh import cp
from shutil import copy2, copytree, make_archive
import sys
from tqdm import tqdm
import yaml
import unittest.mock

DEFAULT_TABLE_PATH='../../_common/dic/kana2phonemes_utf8_for_oto2lab.table'

def get_parser():
    parser = argparse.ArgumentParser(
        description="Make SimpleEnunu model for distribution",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("dist_config", type=str, help="Disbribution config file")
    parser.add_argument("dest_dir", type=str, help="Destination directory")
    parser.add_argument('--table_path', type=str, default=DEFAULT_TABLE_PATH, help='Table file path')
    parser.add_argument('--debug', action='store_true', help='Debug Mode')
    return parser

def copy_packed_models(packed_models_dir, release_dir):
    """
    Copy packed_models
    """
    logging.info('copying packed models')
    
#   copytree(packed_models_dir, join(release_dir, "model"))
    cp("-r", packed_models_dir, join(release_dir, "model"))
 
def copy_table(table_path, release_dir):
    """
    Copy *.table, *.conf
    """
    logging.info('copying table')
    
    copy2(table_path, join(release_dir, "model"))

def copy_resources(resource_dir, release_dir):
    """
    Copy resource files.
    """
    resource_path_list = glob(join(resource_dir, '*'))

    logging.info('Copying resources')
    for resource_path in tqdm(resource_path_list):
        name = basename(resource_path)
        if name != "enuconfig.yaml":
            copy2(resource_path, join(release_dir, name))

        
def make_install_txt(template_dir, release_dir, description, encoding='CP932', newline="\r\n"):
    env = Environment(loader=FileSystemLoader(template_dir, encoding='utf8'))
    tpl = env.get_template('install.tmpl.txt')
    txt = tpl.render({'release_dir': basename(release_dir), 'description': description})
    
    install_txt_path=join(release_dir, "..", "install.txt")

    logging.info('Making install.txt')
    with open(install_txt_path, 'w', encoding=encoding, newline=newline) as f:
        f.write(txt)

def make_character_txt(template_dir, release_dir, release_name, image, author, web, encoding='CP932', newline="\r\n"):
    env = Environment(loader=FileSystemLoader(template_dir, encoding='utf8'))
    tpl = env.get_template('character.tmpl.txt')
    txt = tpl.render({'release_name': release_name, 'image': image, 'author': author, 'web': web})
    
    install_txt_path=join(release_dir, "character.txt")

    logging.info('Making character.txt')    
    with open(install_txt_path, 'w', encoding=encoding, newline=newline) as f:
        f.write(txt)

def copy_extra_files(extra_files_list, release_dir):
    """
    Copy extra files
    """
    logging.info('Copying extra files')
    for extra_files_path in tqdm(extra_files_list):
 #      copytree(expanduser(extra_files_path), join(release_dir, basename(extra_files_path)))
        cp("-r", expanduser(extra_files_path), join(release_dir, basename(extra_files_path)))
        
def main():
    """
    Copy model files for destribution.
    """

    args = get_parser().parse_args(sys.argv[1:])
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug(args)

    dist_config_path=args.dist_config
    dest_dir=args.dest_dir
    table_path = args.table_path
    
    dist_config = None
    with open(dist_config_path, 'r', encoding="UTF-8") as f:
        dist_config = yaml.load(f, Loader=yaml.FullLoader)
    if dist_config is None:
        logging.error(f"Cannot read distribution config file: {dist_config_path}.")
        sys.exit(-1)
    
    model_name = dist_config['model_name']
    version = dist_config['version']
    
    release_name= f"{model_name}_v{version}"
    release_dir = join(dest_dir, release_name)
    os.makedirs(release_dir, exist_ok=True)
             
    resource_dir = 'resources'
    template_dir = join("..", "..", "_common", "template")
    packed_models_dir = glob(join("packed_models", "*"))[0]
    logging.debug(f"packed_models_dir: {packed_models_dir}")

    copy_packed_models(packed_models_dir, release_dir)

    table_file = glob(join("packed_models", "**", "*.table"), recursive=True)
    if len(table_file) != 0:
        copy_table(table_path, release_dir)
    else:
        logging.info(f"table_file: {table_file[0]} is found")
    
    copy_resources(resource_dir, release_dir)

    make_install_txt(template_dir, release_dir, dist_config['description'])

    make_character_txt(template_dir, release_dir, release_name.replace('_', ' '),
                       dist_config['image'],
                       dist_config['author'],
                       dist_config['web'])
    
    copy_extra_files(dist_config['extra_files_list'], release_dir)
    
if __name__ == '__main__':
    main()
