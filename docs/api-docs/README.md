<!-- markdownlint-disable -->

# API Overview

## Modules

- [`utils.py`](./utils.py.md#module-utilspy): Created on Dec 5, 2019

## Classes

- No classes

## Functions

- [`py.assert_exit`](./utils.py.md#function-assert_exit)
- [`py.compare_data_to_json`](./utils.py.md#function-compare_data_to_json)
- [`py.convert_pseudo_type_to_df_type`](./utils.py.md#function-convert_pseudo_type_to_df_type)
- [`py.create_empty_df`](./utils.py.md#function-create_empty_df)
- [`py.create_file_path`](./utils.py.md#function-create_file_path)
- [`py.create_folder`](./utils.py.md#function-create_folder)
- [`py.create_large_dict`](./utils.py.md#function-create_large_dict)
- [`py.decode_class_instance`](./utils.py.md#function-decode_class_instance)
- [`py.delete_http_proxy_if_nt`](./utils.py.md#function-delete_http_proxy_if_nt)
- [`py.encode_class_instance`](./utils.py.md#function-encode_class_instance)
- [`py.export_dictionary_dfs_to_csv`](./utils.py.md#function-export_dictionary_dfs_to_csv)
- [`py.finish_action_decorator`](./utils.py.md#function-finish_action_decorator)
- [`py.finish_step_decorator`](./utils.py.md#function-finish_step_decorator)
- [`py.get_block_schema_step_time_elapsed`](./utils.py.md#function-get_block_schema_step_time_elapsed)
- [`py.get_config_section_dictionary_by_name`](./utils.py.md#function-get_config_section_dictionary_by_name)
- [`py.get_db_props`](./utils.py.md#function-get_db_props)
- [`py.get_env_variables`](./utils.py.md#function-get_env_variables)
- [`py.get_file_name_without_extension`](./utils.py.md#function-get_file_name_without_extension)
- [`py.get_folder_files`](./utils.py.md#function-get_folder_files)
- [`py.get_model_name_from_fqdn`](./utils.py.md#function-get_model_name_from_fqdn)
- [`py.get_separator_line`](./utils.py.md#function-get_separator_line)
- [`py.get_size`](./utils.py.md#function-get_size): Recursively finds size of objects
- [`py.get_storage_props`](./utils.py.md#function-get_storage_props)
- [`py.increment`](./utils.py.md#function-increment)
- [`py.increment_block_schema_step_count`](./utils.py.md#function-increment_block_schema_step_count)
- [`py.is_file_exist`](./utils.py.md#function-is_file_exist)
- [`py.is_file_path_exist`](./utils.py.md#function-is_file_path_exist)
- [`py.load_objects_from_files`](./utils.py.md#function-load_objects_from_files)
- [`py.load_objects_from_files_with_version`](./utils.py.md#function-load_objects_from_files_with_version)
- [`py.loading_object_from_parquet_files`](./utils.py.md#function-loading_object_from_parquet_files)
- [`py.loading_object_from_pickle_files`](./utils.py.md#function-loading_object_from_pickle_files)
- [`py.now_to_string`](./utils.py.md#function-now_to_string)
- [`py.post_finish_to_dashboard`](./utils.py.md#function-post_finish_to_dashboard)
- [`py.post_start_to_dashboard`](./utils.py.md#function-post_start_to_dashboard)
- [`py.print_all_env_variables`](./utils.py.md#function-print_all_env_variables)
- [`py.print_current_path`](./utils.py.md#function-print_current_path)
- [`py.print_decorator`](./utils.py.md#function-print_decorator)
- [`py.print_df_head`](./utils.py.md#function-print_df_head)
- [`py.print_df_table`](./utils.py.md#function-print_df_table)
- [`py.print_dictionary_head`](./utils.py.md#function-print_dictionary_head)
- [`py.print_dictionary_simple_head`](./utils.py.md#function-print_dictionary_simple_head)
- [`py.print_fancy_grid`](./utils.py.md#function-print_fancy_grid)
- [`py.print_host_env_data`](./utils.py.md#function-print_host_env_data)
- [`py.print_title`](./utils.py.md#function-print_title)
- [`py.read_any_json_file`](./utils.py.md#function-read_any_json_file)
- [`py.read_any_json_file_to_dictionary`](./utils.py.md#function-read_any_json_file_to_dictionary)
- [`py.read_any_json_file_to_dictionary_if_exists`](./utils.py.md#function-read_any_json_file_to_dictionary_if_exists)
- [`py.read_config_json_file`](./utils.py.md#function-read_config_json_file)
- [`py.read_config_json_file_to_dictionary`](./utils.py.md#function-read_config_json_file_to_dictionary)
- [`py.read_config_json_to_dictionary_by_entry`](./utils.py.md#function-read_config_json_to_dictionary_by_entry)
- [`py.read_csv_file_to_df`](./utils.py.md#function-read_csv_file_to_df)
- [`py.read_csv_file_to_df_by_path`](./utils.py.md#function-read_csv_file_to_df_by_path)
- [`py.read_file`](./utils.py.md#function-read_file)
- [`py.read_file_if_exists`](./utils.py.md#function-read_file_if_exists)
- [`py.read_model_json_file`](./utils.py.md#function-read_model_json_file)
- [`py.read_model_json_file_to_dictionary`](./utils.py.md#function-read_model_json_file_to_dictionary)
- [`py.read_model_json_file_to_list`](./utils.py.md#function-read_model_json_file_to_list)
- [`py.read_pickle_file_to_dictionary_dfs`](./utils.py.md#function-read_pickle_file_to_dictionary_dfs)
- [`py.read_requests_to_dictionary`](./utils.py.md#function-read_requests_to_dictionary)
- [`py.read_text_file_to_set`](./utils.py.md#function-read_text_file_to_set)
- [`py.remove_file_if_exists`](./utils.py.md#function-remove_file_if_exists)
- [`py.remove_folder`](./utils.py.md#function-remove_folder)
- [`py.save_objects_to_files`](./utils.py.md#function-save_objects_to_files)
- [`py.save_objects_to_files_by_version_count`](./utils.py.md#function-save_objects_to_files_by_version_count)
- [`py.say_it`](./utils.py.md#function-say_it)
- [`py.send_request_to_dashboard`](./utils.py.md#function-send_request_to_dashboard)
- [`py.send_request_to_dashboard_backup`](./utils.py.md#function-send_request_to_dashboard_backup)
- [`py.start_action_decorator`](./utils.py.md#function-start_action_decorator)
- [`py.start_step_decorator`](./utils.py.md#function-start_step_decorator)
- [`py.time_diff_in_seconds`](./utils.py.md#function-time_diff_in_seconds)
- [`py.unzip`](./utils.py.md#function-unzip)
- [`py.whoami`](./utils.py.md#function-whoami)
- [`py.write_df_to_csv_file`](./utils.py.md#function-write_df_to_csv_file)
- [`py.write_dictionary_to_json_file`](./utils.py.md#function-write_dictionary_to_json_file)
- [`py.write_dictionary_to_pickle_file`](./utils.py.md#function-write_dictionary_to_pickle_file)
- [`py.write_text_file`](./utils.py.md#function-write_text_file)


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
