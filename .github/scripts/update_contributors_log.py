#!/usr/bin/env python

import os
import json

'''
This script requires following environment variables:

- REPO_NAME:
  > example: 'iamwatchdogs/test'
  > GitHub action variable: ${{ github.repository }}

- PR_NUMBER:
  > example: '5'
  > GitHub action variable: ${{ github.event.pull_request.number }}
'''


def get_contribution_title(CURRENT_PR):
    """
    This function extracts the contribution title from the provided current pull request.

    Parameters:
    - CURRENT_PR (dict): The current pull request information.

    Returns:
    tuple: A tuple containing the contribution title and the path.
    """

    # Setting default value
    contribution_title = 'root'
    path = contribution_title

    # Iterating through the "files" list
    for files in CURRENT_PR["files"]:
        if '/' in files["path"]:
            contribution_title = files["path"]
            path = contribution_title
            break

    if contribution_title == 'root':
        return (contribution_title, path)

    if '.github/workflows' in path:
        contribution_title = '{workflows}'
    elif '.github/scripts' in path:
        contribution_title = '{scripts}'
    elif '.github' in path:
        contribution_title = '{others}'
    else:
        splitted_title = contribution_title.split('/')
        contribution_title = splitted_title[-2] if '.' in contribution_title else splitted_title[-1]

    return (contribution_title, path)


def get_contributor_name(CURRENT_PR):
    """
    This function extracts the contributor name from the provided current pull request.

    Parameters:
    - CURRENT_PR (dict): The current pull request information.

    Returns:
    str: The contributor name.
    """
    return CURRENT_PR["author"]["login"]


def get_core_type(CONTRIBUTION_TITLE, USED_PATH):
    """
    Determines the core type of the contribution based on the contribution title and used path.

    Parameters:
    - CONTRIBUTION_TITLE (str): The title of the contribution, which can be a specific directory or a special identifier.
    - USED_PATH (str): The file path associated with the contribution.

    Returns:
    str: 'Repo' if the contribution title is one of the special identifiers ('root', '{workflows}', '{scripts}', '{others}'),
    otherwise, the first segment of the used path is returned as the core type.
    """
    if CONTRIBUTION_TITLE in ['root', '{workflows}', '{scripts}', '{others}']:
        return 'Repo'
    return USED_PATH.split('/')[0]


def get_specificity(CONTRIBUTION_TITLE, USED_PATH):
    """
    Determines the specificity of the contribution based on the contribution title and used path.

    Parameters:
    - CONTRIBUTION_TITLE (str): The title of the contribution, can be a specific directory or a special identifier.
    - USED_PATH (str): The file path associated with the contribution.

    Returns:
    str: The specificity of the contribution, extracted from the used path.
    """
    if CONTRIBUTION_TITLE in ['root', '{workflows}', '{scripts}', '{others}']:
        return 'Maintenance'
    return USED_PATH.split('/')[1]


def get_demo_path(CURRENT_PR, CONTRIBUTION_TITLE, CORE_TYPE, SPECIFICITY):
    """
    Generates the demo path of the contribution based on the provided pull request information.

    Parameters:
    - CURRENT_PR (dict): The current pull request information.
    - CONTRIBUTION_TITLE (str): The title of the contribution.
    - CORE_TYPE (str): The core type of the contribution.
    - SPECIFICITY (str): The specificity of the contribution.

    Returns:
    str: The generated demo path of the contribution.
    """

    # Getting required values
    REPO_NAME = os.environ.get('REPO_NAME')

    # Handling a base cases
    if CONTRIBUTION_TITLE == 'root':
        return f'https://github.com/{REPO_NAME}/'
    elif CONTRIBUTION_TITLE == '{workflow}':
        return f'https://github.com/{REPO_NAME}/.github/workflows'
    elif CONTRIBUTION_TITLE == '{scripts}':
        return f'https://github.com/{REPO_NAME}/.github/scripts'
    elif CONTRIBUTION_TITLE == '{others}':
        return f'https://github.com/{REPO_NAME}/.github'

    # Setting default value
    demo_path = f'https://github.com/{REPO_NAME}/tree/main/{CORE_TYPE}/{SPECIFICITY}'
    found_required_path = False

    # Iterating through the "files" list
    for files in CURRENT_PR["files"]:
        path = files["path"]
        if "index.html" in path:
            demo_path = path
            found_required_path = True
            break
        elif path.lower().endswith('index.md') or path.lower().endswith('readme.md'):
            demo_path = path
            found_required_path = True

    # Modifying demo path as a route
    if found_required_path:
        demo_path = '/'.join(demo_path.split('/')[:-1])

    # Checking out for spaces:
    if ' ' in demo_path:
        demo_path = '%20'.join(demo_path.split())

    return demo_path


def main():
    """
    The main function of the script is responsible for updating the contributors log file.

    The function takes in environment variables `REPO_NAME` and `PR_NUMBER` and uses it to fetch the required data from the current PR and the Contributors log file.

    The function then updates the Contributors log file either by appending a new entry or updating an existing one.

    The function also prints out a success message at the end.
    """

    # Setting file paths
    PR_DETAILS_FILE_PATH = 'pr.json'
    CONTRIBUTION_LOG_FILE_PATH = '.github/data/contributors-log.json'

    # Reading contents from the current pr
    with open(PR_DETAILS_FILE_PATH, 'r') as json_file:
        CURRENT_PR = json.load(json_file)

    # Getting required value for update
    CONTRIBUTION_TITLE, USED_PATH = get_contribution_title(CURRENT_PR)
    CONTRIBUTOR_NAME = get_contributor_name(CURRENT_PR)
    CORE_TYPE = get_core_type(CONTRIBUTION_TITLE, USED_PATH)
    SPECIFICITY = get_specificity(CONTRIBUTION_TITLE, USED_PATH)
    PR_NUMBER = os.environ.get('PR_NUMBER')
    DEMO_PATH = get_demo_path(
        CURRENT_PR, CONTRIBUTION_TITLE, CORE_TYPE, SPECIFICITY)

    # Creating a new dict objects for JSON conversion
    existing_data = None
    new_data = {
        CONTRIBUTION_TITLE: {
            "contributor-name": [CONTRIBUTOR_NAME],
            "core": CORE_TYPE,
            "specificity": SPECIFICITY,
            "pull-request-number": [PR_NUMBER],
            "demo-path": DEMO_PATH
        }
    }

    # Processing the data dumps
    operation_name = None
    if os.path.exists(CONTRIBUTION_LOG_FILE_PATH):

        # Reading existing Log file
        with open(CONTRIBUTION_LOG_FILE_PATH, 'r') as json_file:
            existing_data = json.load(json_file)

        # performing updation or addition based on `PROJECT_TITLE`
        if CONTRIBUTION_TITLE in existing_data:
            if CONTRIBUTOR_NAME not in existing_data[CONTRIBUTION_TITLE]["contributor-name"]:
                existing_data[CONTRIBUTION_TITLE]["contributor-name"].append(
                    CONTRIBUTOR_NAME)
            if PR_NUMBER not in existing_data[CONTRIBUTION_TITLE]["pull-request-number"]:
                existing_data[CONTRIBUTION_TITLE]["pull-request-number"].append(
                    PR_NUMBER)
            operation_name = 'Updated'
        else:
            existing_data.update(new_data)
            operation_name = 'Appended data to'
    else:
        existing_data = new_data
        operation_name = 'Created'

    # Dumping the data into log file
    with open(CONTRIBUTION_LOG_FILE_PATH, 'w') as json_file:
        json.dump(existing_data, json_file, indent=2)

    # Output message
    print(f'Successfully {operation_name} the log file')


if __name__ == '__main__':
    main()
