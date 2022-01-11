#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Dec 5, 2019

@author: Pavel May
"""

import os
import sys
import getpass
import inspect
import socket
import json
import jsons
import shutil
import time
from datetime import datetime as dt
import pickle
from zipfile import ZipFile
import pandas as pd
import numpy as np
from tabulate import tabulate
import importlib
import requests
import re
# import awswrangler as wr
# import boto3

# from utils import utils as Utils
# from version import __version__

os.environ['global_step_count'] = '0'
os.environ['global_step_base'] = '0'
os.environ['global_step_interval'] = '1'
os.environ['global_step_start_time'] = '0'
os.environ['global_line_separator'] = "-" * 125
os.environ['block_schema_step_count'] = '0'
os.environ['block_schema_total_time_elapsed'] = str(time.time())

DASHBOARD_PORT = 5000
LAST_VERSION_NUMBER_FILE_NAME = 'last_version.txt'


def assert_exit(condition=None, error_message="No error message provided.", is_exit=False):
    try:
        assert condition
    except AssertionError:
        message = f"{get_separator_line('-', 72)}\n{error_message}\n{get_separator_line('-', 72)}"
        print(message)
        if is_exit:
            sys.exit(error_message)
        else:
            raise Exception(message)


def whoami():
    s = inspect.stack()
    function_name = s[1][3]
    #function_name = inspect.currentframe().f_back.f_code.co_name
    caller_name = s[2][3]
    print(f"\n{os.environ['global_line_separator']}")
    print(f"Current path: {os.getcwd()}")
    print(f"In function:  {inspect.getfile(inspect.currentframe().f_back)}({caller_name}.{function_name})")
    print(f"{os.environ['global_line_separator']}")
    return function_name


def increment():
    os.environ['global_step_count'] = str(int(os.environ['global_step_count']) + int(os.environ['global_step_interval']))
    return os.environ['global_step_count']


def increment_block_schema_step_count():
    os.environ['block_schema_step_count'] = str(int(os.environ['block_schema_step_count']) + 1)
    return os.environ['block_schema_step_count']


def get_block_schema_step_time_elapsed():
    ts1 = float(os.environ['block_schema_total_time_elapsed'])
    ts2 = time.time()
    os.environ['block_schema_total_time_elapsed'] = str(ts2)
    time_elapsed = round((dt.fromtimestamp(ts2) - dt.fromtimestamp(ts1)).total_seconds())
    if time_elapsed == 0:
        time_elapsed = 1;
    return time_elapsed


def get_separator_line(char, size):
    return char * size


def print_decorator(label="", value=""):
    print('==========================================')
    if len(value) > 0:
        print(f"{label}={value}")
    else:
        print(f"{label}:")
    print('==========================================')


def print_title(title, size=150, is_add_empty_string=True):
    print(f"\n{get_separator_line('-', size)}")
    print(title)
    print(f"{get_separator_line('-', size)}")
    if is_add_empty_string:
        print()


def start_step_decorator(step_title):
    print(f"\n{os.environ['global_line_separator']}")
    print(f"STEP #{increment()}. {step_title}")
    print(os.environ['global_line_separator'])
    os.environ['global_step_start_time'] = str(time.time())


def finish_step_decorator(step_title):
    print(f"\n{os.environ['global_line_separator']}")
    time_elapsed = time.time() - float(os.environ['global_step_start_time'])
    print(f"STEP #{os.environ['global_step_count']}. {step_title}: execution time={time_elapsed:.2f})")
    print(os.environ['global_line_separator'])


def start_action_decorator(step_title):
    print(f"\n{os.environ['global_line_separator']}")
    print(f"{step_title}")
    os.environ['global_step_start_time'] = str(time.time())


def finish_action_decorator(step_title):
    time_elapsed = time.time() - float(os.environ['global_step_start_time'])
    print(f"\n{step_title}: execution time={time_elapsed:.2f})")
    print(os.environ['global_line_separator'])


def read_config_json_to_dictionary_by_entry(json_file, entry):
    input_dictionary = {}
    assert_exit(len(json_file) == 0, f"Config json file '{json_file}' is empty.")
    input_json_string = read_config_json_file(json_file)
    assert_exit(len(input_json_string) == 0, f"Config json file '{json_file}' is empty.")
    json_dict = json.loads(input_json_string)
    if entry in json_dict:
        sql_list = json_dict[entry]
        for sql_dict in sql_list:
            item_list = list(sql_dict.items())
            input_dictionary[item_list[0][0]] = item_list[0][1]
    return input_dictionary


def read_config_json_file(file_name):
    config_json_file = "config//" + file_name
    assert_exit(os.path.isfile(config_json_file), f"Configuration file '{config_json_file}' does not exist.")
    f = open(config_json_file, "r")
    file_text = f.read()
    f.close()
    return file_text


def read_config_json_file_to_dictionary(config_json_file):
    assert_exit(len(config_json_file) > 0, f"Configuration json file name '{config_json_file}' is empty.")
    input_json_string = read_config_json_file(config_json_file)
    assert_exit(len(input_json_string) > 0, f"Configuration json file '{config_json_file}' is empty.")
    dictionary = json.loads(input_json_string)
    assert_exit(len(dictionary) == 0, f"Configuration json file '{config_json_file}' is empty.")
    return dictionary


def read_model_json_file_to_dictionary(json_file):
    assert_exit(len(json_file) > 0, f"Model json file '{json_file}' name is empty.")
    input_json_string = read_model_json_file(json_file)
    assert_exit(len(input_json_string) > 0, f"Model json file '{json_file}' is empty.")
    dictionary = json.loads(input_json_string)
    return dictionary


def read_any_json_file_to_dictionary(json_file='', is_fail_fast=True):
    if is_fail_fast:
        assert_exit(os.path.isfile(json_file), f"Configuration json file '{json_file}' does not exist.")
        assert_exit(len(json_file) > 0, f"json file '{json_file}' name is empty.")
        input_json_string = read_any_json_file(json_file)
        assert_exit(len(input_json_string) > 0, f"json file '{json_file}' is empty.")
    else:
        if not os.path.isfile(json_file):
            return None
        if len(json_file) == 0:
            return None
        input_json_string = read_any_json_file(json_file)
        if len(input_json_string) == 0:
            return None
    dictionary = None
    try:
        dictionary = json.loads(input_json_string)
    except Exception as err:
        assert_exit(False, f"json file '{json_file}' load fails: {err}.")
    return dictionary


def read_any_json_file_to_dictionary_if_exists(json_file):
    json_file = json_file.replace('\\', '/')
    cwd_path = os.getcwd().replace('\\', '/')
    print(f"UTILS: read_any_json_file_to_dictionary_if_exists():\n  CURRENT_PATH={cwd_path}\n  file={json_file}")
    if not os.path.isfile(json_file):
        return None
    if len(json_file) == 0:
        return None
    input_json_string = read_any_json_file(json_file)
    if len(input_json_string) == 0:
        return None
    dictionary = None
    try:
        dictionary = json.loads(input_json_string)
    except Exception as err:
        assert_exit(False, f"json file '{json_file}' load fails: {err}.")
    return dictionary


def read_model_json_file(file_name):
    json_file_name = f"models//{os.environ['model_name']}//json//{file_name}"
    assert_exit(os.path.isfile(json_file_name), f"Configuration json file '{json_file_name}' does not exist.")
    f = open(json_file_name, "r")
    file_text = f.read()
    f.close()
    return file_text


def read_any_json_file(file_path):
    assert_exit(os.path.isfile(file_path), f"Configuration json file '{file_path}' does not exist.")
    f = open(file_path, "r")
    file_text = f.read()
    f.close()
    return file_text


def read_file_if_exists(file_name):
    file_name = file_name.replace('\\', '/')
    is_exist = os.path.isfile(file_name)
    if is_exist:
        f = open(file_name, "r")
        file_text = f.read()
        f.close()
        return file_text
    else:
        return None


def read_file(file_name):
    file_name = file_name.replace('\\', '/')
    cwd_path = os.getcwd().replace('\\', '/')
    print(f"UTILS: read_file():\n  CURRENT_PATH={cwd_path}\n  file={file_name}")
    assert_exit(os.path.isfile(file_name), f"File '{file_name}' does not exist.")
    f = open(file_name, "r")
    file_text = f.read()
    f.close()
    return file_text


def read_model_json_file_to_list(list_entry, json_file):
    assert_exit(len(json_file) > 0, f"Model json file '{json_file}' name is empty.")
    json_file_path = f"models//{os.environ['model_name']}//json//{json_file}"
    assert_exit(os.path.isfile(json_file_path), f"File '{json_file_path}' does not exist.")
    input_json_string = read_model_json_file(json_file)
    assert_exit(len(input_json_string) > 0, f"Model json file '{json_file}' is empty.")
    json_dict = json.loads(input_json_string)
    assert_exit(list_entry in json_dict, f"List entry '{list_entry}' does not exist.")
    list_elements = json_dict[list_entry]
    return list_elements


def read_text_file_to_set(text_file):
    assert_exit(len(text_file) > 0, f"Model json file '{text_file}' name is empty.")
    if not os.path.isfile(text_file):
        return set()
    file = open(text_file)
    lines_list = file.read().splitlines()
    file.close()
    lines_set = set(lines_list)
    assert_exit(len(lines_set) > 0, f"Text file '{text_file}' is empty.")
    return lines_set


def read_pickle_file_to_dictionary_dfs(file_name='', is_run_by_api=False):
    if os.path.isfile(file_name):
        pickle_file = file_name
    elif is_run_by_api:
        pickle_file = f"files//{file_name}"
    else:
        pickle_file = f"models//{os.environ['model_name']}//files//{file_name}"
    assert_exit(os.path.isfile(pickle_file) is True, f"Pickle file '{pickle_file}' does not exist.")
    f = open(pickle_file, 'rb')
    pickle_dict = pickle.load(f)
    f.close()
    return pickle_dict


def read_csv_file_to_df(file_name):
    relative_path = f"models//{os.environ['model_name']}//files//{file_name}"
    assert_exit(os.path.isfile(relative_path) is True, f"CSV file '{file_name}' does not exist.")
    #current_file = os.path.abspath(os.path.dirname(__file__))  # older/folder2/scripts_folder
    #csv_filename = os.path.join(current_file, f"models/{model_folder_name}/{item['input_file']}")
    df = pd.read_csv(relative_path)
    df = df.fillna(0).copy()
    return df


def read_csv_file_to_df_by_path(file_path):
    assert_exit(os.path.isfile(file_path) is True, f"CSV file '{file_path}' does not exist.")
    df = pd.read_csv(file_path)
    df = df.fillna(0).copy()
    return df


def write_df_to_csv_file(df, file_name):
    relative_path = f"models//{os.environ['model_name']}//files//{file_name}.csv"
    if os.path.isfile(relative_path) is True:
        os.remove(relative_path)
    df.to_csv(relative_path, encoding='utf-8', na_rep='NaN', header=True, index=False)


def export_dictionary_dfs_to_csv(dictionary):
    whoami()
    print(f"EXPORT DICTIONARY DATAFRAMES to CSV FILES...")
    for key, df in dictionary.items():
        if not isinstance(df, pd.DataFrame):
            continue
        print("  SHAPE=" + str(df.shape))
        print("  df.columns=" + str(df.columns))

        start = time.time()
        write_df_to_csv_file(df, key)
        print(f"  CREATE CSV FILE '{key}' execution time: {time.time() - start}")


def read_requests_to_dictionary(json_file=""):
    input_dictionary = {}
    item_list = read_model_json_file_to_list("requests", json_file)
    for item_dict in item_list:
        item_list = list(item_dict.items())
        item = (item_list[0][1])
        assert_exit(item is not None, f"Request '{item_list[0][1]}' read failed.")
        assert_exit(len(item) != 0, f"Request '{item_list[0][1]}' brings no results.")
        input_dictionary[item_list[0][0]] = item
    return input_dictionary


def write_dictionary_to_pickle_file(dictionary, file_name, is_run_by_api=False):
    if "\\" in file_name or "/" in file_name:
        pickle_file = file_name
    elif is_run_by_api:
        create_folder('files')
        pickle_file = f"files//{file_name}"
    else:
        pickle_file = f"models//{os.environ['model_name']}//files//{file_name}"
    dirname, fname = os.path.split(pickle_file)
    create_file_path(dirname)
    remove_file_if_exists(pickle_file)
    pickle.dump(dictionary, open(pickle_file, "wb"), pickle.HIGHEST_PROTOCOL)
    return pickle_file


def write_dictionary_to_json_file(dictionary=None, json_file=""):
    # Open the file for writing. For existing file, the data is truncated and over-written.
    # The handle is positioned at the beginning of the file. Creates the file if the file does not exists.
    with open(json_file, 'w') as f:
        json.dump(obj=dictionary, fp=f, indent=4)


def create_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"Folder '{folder}' created.")
    else:
        print(f"Folder '{folder}' already exists.")


def create_file_path(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path, exist_ok=True)
        print(f"File path '{file_path}' created.")
    else:
        print(f"File path '{file_path}' already exists.")


def time_diff_in_seconds(start_time, finish_time):
    timedelta = finish_time - start_time
    return timedelta.days * 24 * 3600 + timedelta.seconds


def get_config_section_dictionary_by_name(dictionary_name):
    #whoami()
    config_json_file = os.environ['config_json_file']
    with open(config_json_file, "r") as read_file:
        data = json.load(read_file)

    dictionary = data[dictionary_name]
    # print("==========================================")
    # print("ALL PROPERTIES")
    # print("==========================================")
    # print(dictionary_name + "=" + str(type(dictionary)) + ": " + str(dictionary))
    # print("")

    return dictionary


def get_db_props():
    #whoami()
    config_json_file = os.environ['config_json_file']
    with open(config_json_file, "r") as read_file:
        data = json.load(read_file)

    connection = data['connection']
    # print("==========================================")
    # print("PROPERTIES: connection")
    # print("==========================================")
    # print("connection=" + str(type(connection)) + ": " + str(connection))
    # print("")

    driver = connection["driver"]
    server = connection["server"]
    database = connection["database"]
    port = connection["port"]
    username = connection["username"]
    password = connection["password"]

    return (driver,
            server,
            database,
            port,
            username,
            password)


def get_storage_props():
    #whoami()
    config_json_file = os.environ['config_json_file']
    with open(config_json_file, "r") as read_file:
        data = json.load(read_file)

    blobstorage = data['blobstorage']
    # print("==========================================")
    # print("PROPERTIES: blobstorage")
    # print("==========================================")
    # print("blobstorage=" + str(type(blobstorage)) + ": " + str(blobstorage))
    # print("")

    container_name = blobstorage["container_name"]
    model_folder_name = blobstorage["model_folder_name"]
    account_name = blobstorage["account_name"]
    account_key = blobstorage["account_key"]
    df_group_by_name = blobstorage["df_group_by_name"]

    return (container_name,
            model_folder_name,
            account_name,
            account_key,
            df_group_by_name)


def unzip(zip_file_path="", destination_folder=""):
    with ZipFile(zip_file_path, 'r') as zipObj:
        zipObj.extractall(destination_folder)

# (driver,
#  server,
#  database,
#  port,
#  username,
#  password) = get_db_props("config.json")
#
#
# (container_name,
#  model_folder_name,
#  account_name,
#  account_key,
#  df_group_by_name) = get_storage_props("config.json")


# dictionary = get_dictionary_by_name('connection')
# print(dictionary['driver'])
# for k, v in dictionary.items():
#     s = '"%s":"%s"' % (k, v)
#     print(str(s))
#
#
# dictionary = get_dictionary_by_name("blobstorage")
# for k, v in dictionary.items():
#     s = '"%s":"%s"' % (k, v)
#

def print_df_head(title='', df=dict(), max_row=6, max_col=4):
    print(f"\n{title}")
    pd.set_option('display.expand_frame_repr', False)
    seq = np.arange(0, len(df.columns), max_col)
    for i in seq:
        print(df.loc[range(0, max_row), df.columns[range(i, min(i + max_col, len(df.columns)))]])
    pd.set_option('display.expand_frame_repr', True)


def print_df_table(title='', df=pd.DataFrame(), max_row=6, max_col=4):
    print(f"df key='{title}':")
    print(tabulate(df.head(max_row), headers='keys', tablefmt='psql'))


def print_dictionary_head(title, dictionary, max_row=2, max_col=8):
    print(title)
    for key, value in dictionary.items():
        if isinstance(value, pd.DataFrame):
            print(f"\ndf key='{key}'")
            print_df_head(value, max_row, max_col)
        else:
            print(f"non-df '{key}'='{value}'")


def print_dictionary_simple_head(title, dictionary, max_row=2):
    #pd.set_option('display.max_columns', None)
    print(f"\n{title}")
    for key, value in dictionary.items():
        print(f"\nkey='{key}'\ntype='{type(value)}'")
        if isinstance(value, pd.DataFrame):
            print(tabulate(value.head(max_row), headers='keys', tablefmt='psql'))
        elif isinstance(value, pd.Series):
            df = value.to_frame()
            print(tabulate(df.head(max_row), headers='keys', tablefmt='psql'))
        else:
            print(f"non=df value='{value}'")


def print_current_path():
    path = os.getcwd()
    print(f"Current path={path}")
    print(f"__file__={str(__file__)}")


def get_folder_files(path):
    #return os.listdir(path)
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


def remove_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(f"Failure: The file '{file_path}' does not exist.")


def remove_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path, ignore_errors=True)
    else:
        print(f"  Info: The folder '{folder_path}' does not exist.")


def write_text_file(file_path, mode, content):
    file = open(file_path, mode)
    file.write(content)
    file.close()


def say_it(text='', is_print=True):
    if is_print:
        print(text)

    try:
        if os.name == 'nt':
            ttsx3 = importlib.import_module('pyttsx3')
            tts = ttsx3.init()
            tts.setProperty('rate', 135)
            tts.setProperty('volume', 0.5)
            voices = tts.getProperty('voices')
            tts.setProperty('voice', voices[1].id)
            text = text.replace('_', ' ')
            tts.say(text)
            tts.runAndWait()
    except Exception as e:
        print(f'tts: {e}')
        pass


def send_request_to_dashboard_backup(pipeline_name):
    step_count = increment_block_schema_step_count()
    # dashboard = 'DASHBOARD_SERVICE_IS_RUNNING'
    # if dashboard not in os.environ:
    #     print(f"Utils: '{dashboard}' not in os.environ")
    #     return
    #
    # if os.environ[dashboard] != 'TRUE':
    #     print(f"Utils: '{dashboard}' not 'TRUE'")
    #     return

    delete_http_proxy_if_nt()
    print(f"BRAIN: Utils: Sending step_count {step_count} to Dashboard...")
    try:
        response = requests.get(f'http://127.0.0.1:{DASHBOARD_PORT}/{step_count}')
        print(f'\nBRAIN: Utils: Step response.content: {response.content}')
        if response.status_code < 200 or response.status_code > 226:
            msg = f'BRAIN: sending step_count failed: {response.status_code}'
            print(msg)
            return {
                'pipeline_name': pipeline_name,
                'user': getpass.getuser().upper(),
                'status': msg
            }
        else:
            print(f'BRAIN: Utils: sending step_count succeded: {response.status_code}')
    # except (ConnectionError, ConnectionRefusedError) as err:
    except Exception as err:
        print_title(title='BRAIN: Utils: INFO: HTTP CONNECTION ERROR:', is_add_empty_string=False)
        [print(x.strip()) for x in str(err.args[0]).split(':')]
    except:
        print_title(title='BRAIN: Utils: INFO: UNKNOWN HTTP CONNECTION ERROR:', is_add_empty_string=False)
        print(f'BRAIN: Utils: sending step_count failed: {response.status_code}')


def send_request_to_dashboard(pipeline_name, is_time_elapsed=False, step_key='', is_send_request_to_dashboard=False, is_set_time_base=False):
    if not is_send_request_to_dashboard:
        return

    if is_set_time_base:
        os.environ['block_schema_total_time_elapsed'] = str(time.time())

    time_elapsed = 0
    if is_time_elapsed:
        time_elapsed = get_block_schema_step_time_elapsed()

    delete_http_proxy_if_nt()
    print(f"BRAIN: Utils: Sending step_key/time_elapsed {step_key}/{time_elapsed} to BMW Dashboard...")
    #time.sleep(1)  # To enable sync with front-end
    try:
        write_text_file(f"pipeline_progress.bar", 'w', f"{step_key},{time_elapsed}")

        response = requests.get(f'http://127.0.0.1:{DASHBOARD_PORT}/key/{step_key}/{time_elapsed}')
        print(f'BRAIN: Utils: Step response.content: {response.content}')
        if response.status_code < 200 or response.status_code > 226:
            msg = f'BRAIN: sending step_key/time_elapsed failed: {response.status_code}'
            print(msg)
            return {
                'pipeline_name': pipeline_name,
                'user': getpass.getuser().upper(),
                'status': msg
            }
        else:
            print(f'BRAIN: Utils: sending step_key/time_elapsed succeded: {response.status_code}')
    # except (ConnectionError, ConnectionRefusedError) as err:
    except Exception as err:
        print_title(title='Brain: Utils: INFO: HTTP CONNECTION ERROR:', is_add_empty_string=False)
        [print(x.strip()) for x in str(err.args[0]).split(':')]
    except:
        print_title(title='BRAIN: Utils: INFO: UNKNOWN HTTP CONNECTION ERROR:', is_add_empty_string=False)
        print(f'BRAIN: Utils: sending step_key/time_elapsed failed: {response.status_code}')


def post_start_to_dashboard(pipeline_name, block_schema, is_send_request_to_dashboard=False):
    if not is_send_request_to_dashboard:
        return

    # Redirect sys.stdout to the file
    file_handle = open('brain.log', 'w')
    sys.stdout = file_handle
    sys.stderr = file_handle

    # Posting global_block_schema to Dasboard service
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    delete_http_proxy_if_nt()
    response = requests.post(f'http://127.0.0.1:{DASHBOARD_PORT}/start', headers=headers, json=block_schema)
    print(f'\nStep response.content: {response.content}')
    if response.status_code < 200 or response.status_code > 226:
        msg = f'BRAIN: UTILS: start: posting block_schema failed: {response.status_code}'
        print(msg)
        return {
            'pipeline_name': pipeline_name,
            'user': getpass.getuser().upper(),
            'status': msg
        }
    else:
        print(f'BRAIN: UTILS: start: posting block_schema succeeded: {response.status_code}')
        send_request_to_dashboard(is_time_elapsed=False, step_key="START", is_send_request_to_dashboard=is_send_request_to_dashboard, is_set_time_base=True)


def post_finish_to_dashboard(runs_dict, is_send_request_to_dashboard=False):
    if not is_send_request_to_dashboard:
        return
    # Posting global_finish_value
    run_count = len(runs_dict)
    finish_key = runs_dict[run_count - 1]
    finish_key['final_key'] = "FINISH"
    finish_key['step_key'] = "FINISH"
    finish_key['time_elapsed'] = 0


    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    delete_http_proxy_if_nt()
    response = requests.post(f'http://127.0.0.1:{DASHBOARD_PORT}/finish', headers=headers, json=finish_key)
    print(f'\nStep response.content: {response.content}')
    if response.status_code < 200 or response.status_code > 226:
        print(f'BRAIN: UTILS: finish: posting finish_key failed: {response.status_code}')
    else:
        print(f'BRAIN: UTILS: finish: posting finish_key succeeded: {response.status_code}')
        send_request_to_dashboard(is_time_elapsed=False, step_key="FINISH", is_send_request_to_dashboard=is_send_request_to_dashboard, is_set_time_base=True)


def is_file_exist(file_name='', is_run_by_api=False):
    if "\\" in file_name or "/" in file_name:
        some_file = file_name
    elif is_run_by_api:
        create_folder('files')
        some_file = f"files//{file_name}"
    else:
        some_file = f"models//{os.environ['model_name']}//files//{file_name}"
    return os.path.isfile(some_file)


def is_file_path_exist(file_path):
    return os.path.exists(file_path)


########################################################
# Function to detect a difference
# between keys of two dictionaries
########################################################
def compare_data_to_json(json_dict, data_dict):
    msg_string = ""
    diff_list = list(set(json_dict) - set(data_dict))
    if len(diff_list) != 0:
        msg_string = f"\nThese config keys do not exist in data dictionary:\n  {', '.join(diff_list)}. "
    diff_list = list(set(data_dict) - set(json_dict))
    if len(diff_list) != 0:
        msg_string += f"\nThese data keys do not exist in configuration dictionary:\n  {', '.join(diff_list)}."
    if msg_string != "":
        assert_exit(False, f"FAILURE: Provided data dictionary does not match configuration dictionary: {msg_string}")


########################################################
# Functions to Encode and Decode class instance
# To be able to pickle class instance
########################################################
# Encoded class instance (object)
def encode_class_instance(class_obj_to_encode):
    # import jsons #pip install jsons
    # class_obj =  deepcopy(conf_obj)
    try:
        # https://jsons.readthedocs.io/en/latest/?badge=latest
        encoded = jsons.dump(class_obj_to_encode)

        # encode & decode to verify correctness
        loaded_sanity = jsons.load(jsons.dump(class_obj_to_encode), type(class_obj_to_encode))
    # loaded_sanity = jsons.load( jsons.dump(class_obj_to_encode) ,Aux_What_IF.Configuration_class)
    except:
        # https://stackoverflow.com/questions/30113723/creating-class-instance-from-dictionary
        encoded = class_obj_to_encode.__dict__
        loaded_sanity = type(class_obj_to_encode)(**encoded)
    # loaded_sanity =  Aux_What_IF.Configuration_class(**encoded)

    # ------------------------------------------------------
    # Sanity to check dump and load correctenss
    # ------------------------------------------------------
    for key in class_obj_to_encode.__dict__.keys():
        assert (np.all(getattr(class_obj_to_encode, key) == \
                       getattr(loaded_sanity, key))), \
            "encode_class_instance () : The error => encoded class instance  != decocded class instance ! "

    return encoded


# Decode class instance (object)
def decode_class_instance(class_obj_to_decode, class_to_decode):
    # class_obj =  deepcopy(conf_obj)
    # class_to_decode = type(class_obj)

    # import jsons #pip install jsons
    try:

        # https://jsons.readthedocs.io/en/latest/?badge=latest
        decoded = jsons.load(class_obj_to_decode, class_to_decode)
    # decoded = jsons.load( class_obj_to_decode ,Aux_What_IF.Configuration_class)
    except:

        # https://stackoverflow.com/questions/30113723/creating-class-instance-from-dictionary
        decoded = class_to_decode(**class_obj_to_decode)
    # decoded =  Aux_What_IF.Configuration_class(**class_obj_to_decode)

    return decoded


def now_to_string():
    date_time = f'{dt.now()}'
    date_time = re.sub('[ :.]', '_', date_time)
    return date_time


def get_size(obj, seen=None):
    # https://goshippo.com/blog/measure-real-size-any-python-object
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


def create_large_dict(keys_size, value_length):
    large_dict = dict()
    x_value = '*' * value_length
    for x in range(keys_size):
        large_dict[x] = x_value
    print(f'\nCreated large dictionary object size={get_size(large_dict)}\n')
    return large_dict


def delete_http_proxy_if_nt():
    if os.name == 'nt':
        if 'http_proxy' in os.environ:
            print('Delete HTTP_PROXY from list of environment variables...')
            del os.environ['http_proxy']
            print('HTTP_PROXY deleted from list of environment variables.')


def save_objects_to_files(pipeline_name, obj_dict):
    whoami()
    if 'AIA_ML_FS_BASE_PATH' not in os.environ:
        assert_exit(False, f"FAILURE: Pipeline '{pipeline_name}: 'AIA_ML_FS_BASE_PATH' env variable does not exist.")
    base_path = os.environ['AIA_ML_FS_BASE_PATH']
    pipeline_versions_path = f"{base_path}/{pipeline_name}"
    last_version_number_file_name = f'{pipeline_versions_path}/{LAST_VERSION_NUMBER_FILE_NAME}'
    if not is_file_path_exist(pipeline_versions_path):
        # Folder does not exists
        create_folder(pipeline_versions_path)
    version_path = f"{pipeline_versions_path}/{now_to_string()}"
    create_folder(version_path)

    for item in obj_dict.items():
        # Serialize a python object hierarchy
        file_path = f'{version_path}/{item[0]}'
        print(f"Saving pickle file='{file_path}")
        with open(file_path, "wb") as f:
            pickle.dump(item[1], f, pickle.HIGHEST_PROTOCOL)


def save_objects_to_files_by_version_count(pipeline_name, obj_dict):
    whoami()
    if 'AIA_ML_FS_BASE_PATH' not in os.environ:
        assert_exit(False,
                          f"FAILURE: Pipeline '{pipeline_name}: 'AIA_ML_FS_BASE_PATH' env variable does not exist.")
    base_path = os.environ['AIA_ML_FS_BASE_PATH']
    pipeline_versions_path = f"{base_path}/{pipeline_name}"
    last_version_number_file_name = f'{pipeline_versions_path}/{LAST_VERSION_NUMBER_FILE_NAME}'
    if not is_file_path_exist(pipeline_versions_path):
        # Folder does not exists
        create_folder(pipeline_versions_path)
        write_text_file(last_version_number_file_name, 'w', '1')
        version_path = f"{pipeline_versions_path}/version_1"
    else:
        # Folder exists
        last_modified = os.listdir(pipeline_versions_path)[-1]
        version_number = read_file_if_exists(last_version_number_file_name)
        if version_number is None:
            assert_exit(False,
                              f"FAILURE: Pipeline '{pipeline_name}: last version number file '{LAST_VERSION_NUMBER_FILE_NAME}' does not exist.")
        version_number_int = int(version_number)
        version_number_int += 1
        write_text_file(last_version_number_file_name, 'w', str(version_number_int))
        version_path = f"{pipeline_versions_path}/version_{str(version_number_int)}"
    create_folder(version_path)

    for item in obj_dict.items():
        # Serialize a python object hierarchy
        file_path = f'{version_path}/{item[0]}'
        print(f"Saving pickle file='{file_path}")
        with open(file_path, "wb") as f:
            pickle.dump(item[1], f, pickle.HIGHEST_PROTOCOL)


def load_objects_from_files_with_version(pipeline_name):
    whoami()
    if 'AIA_ML_FS_BASE_PATH' not in os.environ:
        assert_exit(False,
                          f"FAILURE: Pipeline '{pipeline_name}: 'AIA_ML_FS_BASE_PATH' env variable does not exist.")
    base_path = os.environ['AIA_ML_FS_BASE_PATH']
    pipeline_versions_path = f"{base_path}/{pipeline_name}"
    last_modified_folder = os.listdir(pipeline_versions_path)[-1]
    version_folder = f'{pipeline_versions_path}/{last_modified_folder}'
    file_list = os.listdir(version_folder)
    obj_dict = dict()
    for file_name in file_list:
        file_path = f'{version_folder}/{file_name}'
        print(f"Loading object from pickle file='{file_path}")
        with open(file_path, 'rb') as f:
            obj_dict[file_name] = pickle.load(f)
    return obj_dict


def load_objects_from_files(pipeline_name, path_list):
    whoami()
    if 'AIA_ML_FS_BASE_PATH' not in os.environ:
        assert_exit(False, f"FAILURE: Pipeline '{pipeline_name}: 'AIA_ML_FS_BASE_PATH' env variable does not exist.")
    base_path = os.environ['AIA_ML_FS_BASE_PATH']
    pipeline_path = f"{base_path}/{pipeline_name}"
    full_paths = list()
    for p in path_list:
        file_path = f"{pipeline_path}/{p}"
        is_dir = os.path.isdir(file_path)
        print(f"Loading object from folder='{file_path}")
        is_file = os.path.isfile(file_path)
        print(f"Loading object from file='{file_path}")
        if is_dir:
            file_list = os.listdir(file_path)
            file_list = [f"{file_path}/{f}" for f in file_list]
            full_paths.extend(file_list)
        elif is_file:
            full_paths.append(file_path)
    file_name, file_extension = os.path.splitext(full_paths[0])
    if file_extension == ".parquet":
        obj_dict = loading_object_from_parquet_files(full_paths)
        return obj_dict
    elif file_extension == ".pickle":
        obj_dict = loading_object_from_pickle_files(full_paths)
        return obj_dict


def loading_object_from_parquet_files(path_list):
    obj_dict = dict()
    for path in path_list:
        print(f"Loading object from parquet file='{path}")
        df = pd.read_parquet(path)
        file_name = get_file_name_without_extension(path)
        obj_dict[file_name] = df
    return obj_dict


def loading_object_from_pickle_files(path_list):
    obj_dict = dict()
    for path in path_list:
        print(f"Loading object from pickle file='{path}")
        with open(path, 'rb') as f:
            file_name = get_file_name_without_extension(path)
            obj_dict[file_name] = pickle.load(f)
    return obj_dict


def print_all_env_variables():
    print_title(f"Environment Variables - total: {len(os.environ)}", 150, False)
    for item, value in sorted(dict(os.environ.items()).items()):
        print('{:50}|{:126}'.format(item, value))
    print(get_separator_line("-", 150))


def get_file_name_without_extension(path):
    file_name = os.path.basename(path)
    return os.path.splitext(file_name)[0]


def create_empty_df(columns, dtypes, index=None):
    assert_exit(len(columns)==len(dtypes), f"FAILURE: columns count is not equal typs count: {len(columns)}!={len(dtypes)} ")
    df = pd.DataFrame(index=index)
    for column_name, column_type in zip(columns, dtypes):
        df[column_name] = pd.Series(dtype=column_type)
    return df


def convert_pseudo_type_to_df_type(type_string):
    switcher = {
        'string': 'object',
        'integer': 'int64',
        'long': 'int64',
        'float': 'float64',
        'double': 'float64',
        'decimal': 'float64',
        'boolean': 'bool',
        'timestamp': 'datetime64[ns]'
    }
    return switcher.get(type_string, 'Invalid type')


def print_fancy_grid(python_object, n):
    if type(python_object) is dict:
        for key, value in python_object.items():
            print(f"\nKey: {key}")
            if type(value) is pd.DataFrame:
                print(f"DF shape: {value.shape}")
                print(f"{tabulate(value.head(n), headers='keys', tablefmt='fancy_grid')}\n")
            else:
                print(f"Value:\n{value}\n")
    elif type(python_object) is pd.DataFrame:
        print(f"DF shape: {python_object.shape}")
        print(f"{tabulate(python_object.head(n), headers='keys', tablefmt='fancy_grid')}\n")
    else:
        print(f"Value:\n{python_object}\n")


def get_env_variables(env_variable_name):
    env_variable = ""
    if env_variable_name not in os.environ:
        assert_exit(False, f"{env_variable_name} environment variable does not exist.")
    else:
        env_variable = os.environ[env_variable_name]
        print(f"Environment variable {env_variable_name}='{env_variable}'")
    return env_variable


def get_model_name_from_fqdn(variable_name, fqdn):
    model_name = fqdn
    point_index = model_name.rfind('.')
    if point_index != -1:
        model_name = model_name[point_index + 1:]
    print(f"  variable_name='{model_name}'")
    return model_name


def print_host_env_data(title):
    print(f'\n{title}:')
    current_path = os.getcwd()
    print(f"os.name='{os.name}'")
    # print(f"version={__version__}")
    print(f"hostname='{socket.gethostname()}'")
    print(f"current path='{current_path}'")


# def read_s3_parquet_file_to_df(bucket_name,
#                                file_path,
#                                region_name,
#                                aws_access_key_id,
#                                aws_secret_access_key):
#     buffer = io.BytesIO()
#     s3 = boto3.resource('s3',
#                         region_name,
#                         aws_access_key_id,
#                         aws_secret_access_key)
#     s3_object = s3.Object(bucket_name, file_path)
#     s3_object.download_fileobj(buffer)
#     df = pd.read_parquet(buffer)
#     return df
#
#
# def write_df_to_s3_parquet_file(df,
#                                 bucket_name,
#                                 key_name,
#                                 file_path,
#                                 region_name,
#                                 aws_access_key_id,
#                                 aws_secret_access_key):
#     table = pd.Table.from_pandas(df)
#     pq.write_table(table, file_path)
#
#     # Upload to AWS S3
#     s3 = boto3.client('s3',
#                       region_name,
#                       aws_access_key_id,
#                       aws_secret_access_key )
#     with open(file_path) as f:
#         object_data = f.read()
#         s3.put_object(Body=object_data, Bucket=bucket_name, Key=key_name)
#
# def write_df_to_s3_parquet_file(df, file_name):
#     aws_region_name = os.environ['ATHENA_AWS_REGION_NAME']
#     aws_access_key_id = os.environ['ATHENA_AWS_ACCESS_KEY_ID']
#     aws_secret_access_key = os.environ['ATHENA_AWS_SECRET_ACCESS_KEY']
#     s3_bucket = 'ml-parquet-bucket'  # os.environ['ATHENA_S3_BUCKET']
#     s3_folder = os.environ['ATHENA_S3_OUTPUT_FOLDER']
#     s3_file_path = f's3://{s3_bucket}/{s3_folder}/{file_name}'
#
#     session = boto3.Session(region_name=aws_region_name,
#                             aws_access_key_id=aws_access_key_id,
#                             aws_secret_access_key=aws_secret_access_key)
#     wr.s3.to_parquet(df=df.copy(), path=s3_file_path, boto3_session=session)
#
#
# def read_df_from_s3_parquet_file(df, file_name):
#     aws_region_name = os.environ['ATHENA_AWS_REGION_NAME']
#     aws_access_key_id = os.environ['ATHENA_AWS_ACCESS_KEY_ID']
#     aws_secret_access_key = os.environ['ATHENA_AWS_SECRET_ACCESS_KEY']
#     s3_bucket = 'ml-parquet-bucket'  # os.environ['ATHENA_S3_BUCKET']
#     s3_folder = os.environ['ATHENA_S3_OUTPUT_FOLDER']
#     s3_file_path = f's3://{s3_bucket}/{s3_folder}/{file_name}'
#
#     session = boto3.Session(region_name=aws_region_name,
#                             aws_access_key_id=aws_access_key_id,
#                             aws_secret_access_key=aws_secret_access_key)
#
#     if len(df) < 1_000_000:
#         df = wr.s3.read_parquet(path=s3_file_path, boto3_session=session, chunked=True)
#     else:
#         df = wr.s3.read_parquet(path=s3_file_path, boto3_session=session, chunked=1_000_000)
#     print_fancy_grid(df, 10)
#
#
# def write_dfs_to_parquet_folder(dfs_dict, folder_path):
#     for key, df in dfs_dict.items():
#         df.to_parquet(key, compression='brotli')
#
#
# def read_dfs_from_parquet_folder(folder_path):
#     files = get_folder_files(folder_path)
#     for file in files:
#         df = pd.read_parquet(file)
#         print_fancy_grid(df, 10)