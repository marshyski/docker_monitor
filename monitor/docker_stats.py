__author__ = 'mms'


from docker import Client

c = Client(base_url='unix://var/run/docker.sock', version='1.9', timeout=10)


def system_wide_info():
	system_info = {}
	info = c.info()
	system_info['containers'] = info['Containers']
	system_info['images'] = info['Images']
	system_info['driver'] = info['Driver']
	system_info['mem'] = info['MemTotal']
	system_info['kernel'] = info['KernelVersion']
	system_info['ncpu'] = info['NCPU']

	return system_info


def containers_with_status(status='running'):
	if status == 'ExitCode':

		# TODO

		pass
	else:
		containers = c.containers(filters={'status': status})
		result = []
		for cont in containers:
			container = {'id': cont['Id'], 'cmd': cont['Command'], 'status': cont['Status'], 'name': cont['Name']}
			# print "ID: %s CMD: %s STATUS: %s".format(container['Id'], container['Command'], container['Status'])
			result.append(container)
	return result