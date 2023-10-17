#!/usr/bin/env python

import os
import sys
import json

'''
This script requires following environment variables:

- REPO_NAME:
  > example: 'iamwatchdogs/test'
  > GitHub action variable: ${{ github.repository }}
'''

class UpdateFileContent:
	"""Class that updates root `index.md` based on contributors-log."""

	# Setting static variables\
	DATA = None
	REPO_NAME = None

	def __init__(self, FILE_PATH):

		# Setting Constant values
		self.FILE_PATH = FILE_PATH

		# Retriving data as modifiable lines
		self.lines = self.get_lines()

		# Updates lines based on the data
		self.update_table_of_contributors()
		self.update_table_of_content()

		# Updating target file content
		self.write_lines_into_file()


	def get_lines(self):

		# Reading lines from the file
		with open(self.FILE_PATH, 'r') as file:
			lines = file.readlines()

		return lines
	
	def write_lines_into_file(self):

		# Updating the target file
		with open(self.FILE_PATH, 'w') as file:
			file.writelines(self.lines)

		# Printing Success Message
		print(f"Updated '{self.FILE_PATH}' Successfully")

	def find_table_points(self, search_type):
	
		# Setting default return values
		table_starting_point = None
		table_ending_point = None
		
		# Setting default markers
		table_start_marker = None
		table_end_marker = None
		
		# Selecting respective markers based on `search-type`
		if search_type == 'contributors':
			table_start_marker = '<!-- TABLE OF CONTRIBUTORS BEGINS -->'
			table_end_marker= '<!-- TABLE OF CONTRIBUTORS ENDS -->'
		elif search_type == 'table-of-content':
			table_start_marker = '<!-- TABLE OF CONTENT BEGINS -->'
			table_end_marker= '<!-- TABLE OF CONTENT ENDS -->'
		else:
			print('Invalid Argument', file=sys.stderr)
			exit(1)
			
		# Iterating over lines to find the markers
		for index, line in enumerate(self.lines):
			if table_starting_point is None and table_start_marker in line:
				table_starting_point = index
			elif table_ending_point is None and table_end_marker in line:
				table_ending_point = index
			if table_starting_point is not None and table_ending_point is not None:
				break
			
		# Checking for possible errors
		if table_starting_point is None or table_ending_point is None:
			print('Table not found in the file.', file=sys.stderr)
			exit(2)
		elif table_starting_point >= table_ending_point:
			print('Invaild use of table markers.', file=sys.stderr)
			exit(3)

		return (table_starting_point, table_ending_point)

	def update_table_of_contributors(self, condition=None):
		
		# Calculating stating and ending points of the targeted table
		table_of_contributors_start, table_of_contributors_end = self.find_table_points('contributors')

		# Creating table header if doesn't exist
		if table_of_contributors_end - table_of_contributors_start == 1:
			table_header = list()
			table_header.append('| Contribution Title | Contributor Names | Pull Requests | Demo |\n')
			table_header.append('| --- | --- | --- | --- |\n')
			self.lines[table_of_contributors_start+1:table_of_contributors_end] = table_header
	
		# Initializing empty list for lines
		updated_lines = list()

		# Iterating over log to update target file
		for title, details in self.DATA.items():

			# Modifying based on condition
			if condition is not None and not condition(details):
				continue

			# Processing contributors-names
			contributors_names = details['contributor-name']
			contributors_names_list = [f'[{name}](https://github.com/{name} "goto {name} profile")' for name in contributors_names]
			contributors_names_output = ', '.join(contributors_names_list)

			# Processing pull-requests
			pull_requests = details['pull-request-number']
			pull_requests_list = [f'[#{pr}](https://github.com/{self.REPO_NAME}/pull/{pr} "visit pr \#{pr}")' for pr in pull_requests]
			pull_requests_output = ', '.join(pull_requests_list)

			# Processing demo-path
			demo_path = details['demo-path']
			if ' ' in demo_path:
				demo_path = '%20'.join(demo_path.split())
			demo_path_output = f'[/{self.REPO_NAME}/{title}/]({demo_path} "view the result of {title}")'
			if title == 'root' or title == '{init}':
				demo_path_output = f'[/{self.REPO_NAME}/]({demo_path} "view the result of {title}")'

			# Appending all data together
			updated_lines.append(f'| {title} | {contributors_names_output} | {pull_requests_output} | {demo_path_output} |\n')

		# Updating the lines with updated data
		self.lines[table_of_contributors_start+3:table_of_contributors_end] = updated_lines

		# Printing Success Message
		print('Successfully updated the contributor details !!!...')
		
	def update_table_of_content(self):
		
		# Calculating stating and ending points of the targeted table
		table_of_content_start, table_of_content_end = self.find_table_points('table-of-content')


def main():

	# Retrieving Environmental variables
	REPO_NAME = os.environ.get('REPO_NAME')

	# Setting path for the log JSON file
	ROOT_INDEX_FILE_PATH = 'index.md'
	THEORY_INDEX_FILE_PATH = 'Theory/index.md'
	SOLVED_PROBLEM_INDEX_FILE_PATH = 'Solved-Problems/index.md'
	CONTRIBUTORS_LOG = '.github/data/contributors-log.json'

	# Retrieving data from log file
	with open(CONTRIBUTORS_LOG, 'r') as json_file:
		DATA = json.load(json_file)

	# Assigning values to static members for class `UpdateFileContent`
	UpdateFileContent.DATA = DATA
	UpdateFileContent.REPO_NAME = REPO_NAME

	# Updating root index file
	UpdateFileContent(ROOT_INDEX_FILE_PATH)
	UpdateFileContent(THEORY_INDEX_FILE_PATH)
	UpdateFileContent(SOLVED_PROBLEM_INDEX_FILE_PATH)
	


if __name__ == '__main__':
	main()