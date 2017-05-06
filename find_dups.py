#!/usr/bin/env python

import hashlib
import os
import pprint

empty_digest = hashlib.sha1("").hexdigest()

def get_hash(filename):
	BUF_SIZE = 65536
 	sha1 = hashlib.sha1()
	with open(filename, 'rb') as f:
		while True:
			data = f.read(BUF_SIZE)
			if not data:
				break
			sha1.update(data)
	if sha1.hexdigest() == empty_digest:
		result = None
	else:
		result = sha1.hexdigest()
	return result


def remove_non_dups(dups):
	for hash_value in dups.keys():
		if len(dups[hash_value]) < 2:
			del dups[hash_value]
	return dups

def get_dups(parent_dir):
	dups = {}
	for dirpath, dirnames, filenames in os.walk(parent_dir):
		for filename in filenames:
			full_path = os.path.join(dirpath,filename)
			hash_value = get_hash(full_path)
			if dups.has_key(hash_value):
				dups[hash_value].append(full_path)
			elif hash_value is None:
				pass
			else:
				dups[hash_value] = [full_path]
	return remove_non_dups(dups)


results = get_dups('/home/jacob/salt')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(results)


#for hash_value, items in dups.iteritems():
	




