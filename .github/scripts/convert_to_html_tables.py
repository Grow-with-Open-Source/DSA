#!/usr/bin/env python

import os
import sys
import json
from collections import OrderedDict

'''
This script requires following environment variables:

- REPO_NAME:
  > example: 'iamwatchdogs/test'
  > GitHub action variable: ${{ github.repository }}
'''

class UpdateFileContent:
	"""Class that updates `index.md` based on contributors-log."""

	# Setting static variables
	DATA = None
	REPO_NAME = None

	def __init__(self, FILE_PATH, condition=None):

		# Displaying starting Message
		print(f'\n--- Updating {FILE_PATH} ---\n')

		# Setting Constant values
		self.FILE_PATH = FILE_PATH

		# Retriving data as modifiable lines
		self.lines = self.get_lines()

		# Updates lines based on the data
		self.update_table_of_contributors(condition)
		self.update_table_of_content(condition)

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

	def update_table_of_contributors(self, condition):

		# Calculating stating and ending points of the targeted table
		table_of_contributors_start, table_of_contributors_end = self.find_table_points('contributors')

		# Creating HTML table header to replace md table
		table_header = list()
		table_header.append('<table>\n')
		table_header.append('\t<tr align="center">\n')
		table_header.append('\t\t<th>Contribution Title</th>\n')
		if condition is None:
			table_header.append('\t\t<th>Core Contribution</th>\n')
		table_header.append('\t\t<th>Contributor Names</th>\n')
		table_header.append('\t\t<th>Pull Requests</th>\n')
		table_header.append('\t\t<th>Demo</th>\n')
		table_header.append('\t</tr>\n')

		# Initializing empty list for lines
		updated_lines = list()

		# checking for entries
		has_at_least_one_entry = False


		# Iterating over log to update target file
		for title, details in self.DATA.items():

			# Modifying based on condition
			if condition is not None and not condition(details['core']):
				continue

			# Processing contributors-names
			contributors_names = details['contributor-name']
			contributors_names_list = [f'<a href="https://github.com/{name}" title="goto {name} profile">{name}</a>' for name in contributors_names]
			contributors_names_output = ', '.join(contributors_names_list)

			# Processing core contribution
			core_contribution = details['core']
			if condition is None:
				core_contribution_output = f'<a href="{core_contribution}" title="goto {core_contribution}">{core_contribution}</a>'

			# Processing pull-requests
			pull_requests = details['pull-request-number']
			pull_requests_list = [f'<a href="https://github.com/{self.REPO_NAME}/pull/{pr}" title="visit pr \#{pr}">&#x23;{pr}</a>' for pr in pull_requests]
			pull_requests_output = ', '.join(pull_requests_list)

			# Processing demo-path
			demo_path = details['demo-path']
			specificity = details['specificity']
			if ' ' in demo_path:
				demo_path = '%20'.join(demo_path.split())
			demo_path_output = f'<a href="{demo_path}" title="view the result of {specificity}">./{core_contribution}/{specificity}</a>' 
			if title == 'root' or title == '{init}':
				demo_path_output = f'<a href="{demo_path}" title="view the result of {title}">/{self.REPO_NAME}/</a>'

			# Appending all data together
			updated_lines.append('\t<tr align="center">\n')
			updated_lines.append(f'\t\t<td>{title}</td>\n')
			if condition is None:
				updated_lines.append(f'\t\t<td>{core_contribution_output}</td>\n')
			updated_lines.append(f'\t\t<td>{contributors_names_output}</td>\n')
			updated_lines.append(f'\t\t<td>{pull_requests_output}</td>\n')
			updated_lines.append(f'\t\t<td>{demo_path_output}</td>\n')
			updated_lines.append(f'\t</tr>\n')

			has_at_least_one_entry = True

		# Adding null values if table is completely empty
		if not has_at_least_one_entry:
			updated_lines.append('\t<tr align="center">\n')
			updated_lines.append(f'\t\t<td>-</td>\n')
			if condition is None:
				updated_lines.append(f'\t\t<td>-</td>\n')
			updated_lines.append(f'\t\t<td>-</td>\n')
			updated_lines.append(f'\t\t<td>-</td>\n')
			updated_lines.append(f'\t\t<td>-</td>\n')
			updated_lines.append(f'\t</tr>\n')
		
		# Table footer
		table_footer = ['</table>\n']

		# Updating the lines with updated data
		self.lines[table_of_contributors_start+1:table_of_contributors_end] = table_header + updated_lines + table_footer

		# Printing Success Message
		print('Successfully updated the contributor details !!!...')

	def update_table_of_content(self, condition):

		# Calculating stating and ending points of the targeted table
		table_of_content_start, table_of_content_end = self.find_table_points('table-of-content')

		# Initializing required variables
		updated_lines = list()
		table_of_content = { 'Theory': {}, 'Solved-Problems': {}, 'Repo': {} }

		# Extracting data into required format
		for title, data in self.DATA.items():

			# Setting values for ease of use and more readibility
			core = data['core']
			specificity = data['specificity']

			# Sorting out required data
			if specificity not in table_of_content[core]:
				table_of_content[core][specificity] = None if specificity == title else [title]
			elif title != specificity and title not in table_of_content[core][specificity]:
				if table_of_content[core][specificity] is None:
					table_of_content[core][specificity] = [title]
				else:
					table_of_content[core][specificity].append(title)

		# Sorting extracted data
		for key, value in table_of_content.items():
			for sub_value in value.values():
				if type(sub_value) == list:
					sub_value.sort()
			table_of_content[key] = OrderedDict(sorted(value.items()))

		# Updating lines based on the extracted data
		for core, data in table_of_content.items():

			# Modifying based on condition
			if condition is not None and not condition(core) or core == 'Repo':
				continue

			# Setting Main Heading (Only for Root)
			if condition is None:
				updated_lines.append(f'- [__{core}__]({core} "goto {core}")\n')

			# Adding all headings
			for  heading, sub_heading_list in data.items():
				if condition is None:
					updated_lines.append(f'\t- [{heading}]({core}/{heading} "goto {heading}")\n')
				else:
					updated_lines.append(f'- [__{heading}__]({heading} "goto {heading}")\n')
				if sub_heading_list is not None:
					for sub_heading in sub_heading_list:
						if condition is None:
							updated_lines.append(f'\t\t- [{sub_heading}]({core}/{heading}/{sub_heading} "goto {sub_heading}")\n')
						else:
							updated_lines.append(f'\t- [{sub_heading}]({heading}/{sub_heading} "goto {sub_heading}")\n')

		# Updating the lines with updated data
		self.lines[table_of_content_start+1:table_of_content_end] = updated_lines

		# Printing Success Message
		print('Successfully updated the table of content !!!...')



def main():

	# Retrieving Environmental variables
	REPO_NAME = os.environ.get('REPO_NAME')

	# Setting path for the log JSON file
	ROOT_INDEX_FILE_PATH = 'index.md'
	THEORY_INDEX_FILE_PATH = 'Theory/index.md'
	THEORY_README_FILE_PATH = 'Theory/README.md'
	SOLVED_PROBLEM_INDEX_FILE_PATH = 'Solved-Problems/index.md'
	SOLVED_PROBLEM_README_FILE_PATH = 'Solved-Problems/README.md'
	CONTRIBUTORS_LOG = '.github/data/contributors-log.json'

	# Retrieving data from log file
	with open(CONTRIBUTORS_LOG, 'r') as json_file:
		DATA = json.load(json_file)

	# Assigning values to static members for class `UpdateFileContent`
	UpdateFileContent.DATA = DATA
	UpdateFileContent.REPO_NAME = REPO_NAME

	# Updating All required files
	UpdateFileContent(ROOT_INDEX_FILE_PATH)
	UpdateFileContent(THEORY_INDEX_FILE_PATH, lambda core: core == 'Theory')
	UpdateFileContent(THEORY_README_FILE_PATH, lambda core: core == 'Theory')
	UpdateFileContent(SOLVED_PROBLEM_INDEX_FILE_PATH, lambda core: core == 'Solved-Problems')
	UpdateFileContent(SOLVED_PROBLEM_README_FILE_PATH, lambda core: core == 'Solved-Problems')


if __name__ == '__main__':
	main()
