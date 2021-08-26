_list_objs = [
    {'key': 'value'},
    {'key': 'value', 'data': [
        {'_in_data_key': 'value_1'},
        {'_in_data_key_2': 'value_2'},
        {'_in_data_key_3': 'value_3', 'data_2': [
            {'res': 'ok'}
        ]}
    ]}
]

print(_list_objs[-1]["data"][-1]["data_2"][0]["res"])