data =  {'asset_type': 'server', 'manufacturer': 'innotek GmbH', 'sn': '00002',
 'model': 'VirtualBox', 'uuid': 'E8DE611C-4279-495C-9B58-502B6FCED076',
 'wake_up_type': 'Power Switch', 'os_distribution': 'Ubuntu',
 'os_release': 'Ubuntu 16.04.3 LTS', 'os_type': 'Linux',
 'cpu_count': '2', 'cpu_core_count': '4', 'cpu_model': 'Intel(R) Core(TM) i5-2300 CPU @ 2.80GHz',
 'ram': [{'slot': 'A1', 'capacity': 8}], 'ram_size': 3.858997344970703,
 'nic': [], 'physical_disk_driver': [{'model': 'VBOX HARDDISK', 'size': '50', 'sn': 'VBeee1ba73-09085302'}]}

print(type(data))
print(data.get('ram'))
print(type(data.get('ram')))