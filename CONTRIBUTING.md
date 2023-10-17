# Welcome to CONTRIBUTING.md

Hey there, fellow Developer !!!... I'm happy to see you being hyped about making your *(probably first)* open-source contribution to this repo. We heartily welcome you to an amazing journey of open-source contribution. I hope you have fun learning and teaching at the same time. For the **DSA** repo, you'll be contributing the either the theory part of the DSA or the problems that you have solved using those concepts.

## Setting up Environment

You don't need any special dependencies to use it locally, Just make sure you have *[**git**](https://git-scm.com/ "visit official website") and respective complier/interpreter depending upon your language. It's recommended that GitHub cli *(or)* [**gh**](https://cli.github.com/ "visit official website") is installed for easier access to your repo, but that's totally optional.

## Getting Started with Contribution

So, before you jump right into your code editor and start working on your project, make sure you understand and follow the file structure and guidelines which are mentioned below.

### Instructions and Guidelines

- Most of the time you'll be contributing either the theory writing or the problem you have solved in different platform, rather than the default files present within the repo. So, Make sure you **do not add/remove/modify any content present with the default files**.

  > [!IMPORTANT] 
  > - If any such changes are to be found within your Pull Request *(PR)*, then it will be **rejected** i.e., until and unless it's mentioned on an [Issue](https://github.com/Grow-with-Open-Source/Java-Projects/issues "goto issues tab").
  > - If you wish to work on default file *(either to update or fix a bug)*, create an issue first and get assigned to the issue to let others know that  the issue has been recorded and you've already begun working on it.

- Also, your code will be linted automatically as soon as you make the PR. The PR will be merged if and only if all the checks are completed. If there's any issue with the linting of your work, you can contact the maintainer within the conversation tab of your PR.

- Make sure you document your solved problem and theory part properly:
  - **For Solved-Problems:** Make sure you mentioned the problem name, approach, diffculty and link for the problem you have solved. For refernce,
    ```java
    // Problem Name: <problem-name>
    // Approach:     <data-structure> (or) <algorithm>
    // Diffculty:    <mentioned-diffculty>
    // Link:         <link-to-the-problem>

    /* your solution */
    ```

    <details>
    <summary>For example:</summary>
    <div>

    ```java
    // Problem Name: Longest Consecutive Sequence
    // Approach:     Hash Map
    // Diffculty:    Medium
    // Link:         https://leetcode.com/problems/longest-consecutive-sequence

    /* your solution */
    ```

    </div>
    </details>

  - **For Theory-Problems:** Make sure you explain the concept in detail with a **Table of content**. For refernce,
    ```md
    # <Title>
    <small-intro-description>

    ## Table-of-content
    - [topic-heading-1](#topic-heading-1 "goto topic-heading-1")
    - [topic-heading-2](#topic-heading-2 "goto topic-heading-2")
        - [topic-sub-heading-1](#topic-sub-heading-1 "goto topic-sub-heading-1")
        - [topic-sub-heading-2](#topic-sub-heading-2 "goto topic-sub-heading-2")
        - [topic-sub-heading-3](#topic-sub-heading-3 "goto topic-sub-heading-3")
    - [topic-heading-3](#topic-heading-3 "goto topic-heading-3")
        - [topic-sub-heading-1](#topic-sub-heading-1 "goto topic-sub-heading-1")
        - [topic-sub-heading-2](#topic-sub-heading-2 "goto topic-sub-heading-2")
    - [conclusion](#conclusion "goto conclusion")

    <!-- Your content writting starts from here -->
    ```

    <details>
    <summary>For example:</summary>
    <div>

    ```md
    # Linked List
    <small-intro-description-for-linked-list>

    ## Table-of-content
    - [Linked list concept](#linked-list-concept "goto Linked list concept")
    - [Linked list implementation](#linked-list "goto Linked list implementation")
    - [Basic Operation in Linked List](#Basic-operation-in-linked-list "goto Basic Operation in Linked List")
        - [Insertion](#insertion "goto Insertion")
        - [Deletion](#deletion "goto Deletion")
        - [Display](#display "goto Display")
    - [Type of Linked List](#types-of-linked-list "goto Type of Linked List")
        - [Single Linked List](#single-linked-list "goto Single Linked List")
        - [Doublely Linked List](#doublely-linked-list "goto Doublely Linked List")
        - [Circular Linked List](#circular-linked-list "goto Circular Linked List")
    - [Conclusion](#conclusion "goto Conclusion")

    ## Linked List Concept
    <related-description>

    ## Linked List Implementation
    <related-content>

    ## Basic Operation in Linked List
    <small-description>

    ### Insertion
    <related-content>

    ### Deletion
    <related-content>

    ### Display
    <related-content>

    ## Types of Linked List
    <small-description>

    .
    .
    .

    ## Conclusion
    <ends-the-concept>
    ```

    </div>
    </details>

#### File Structure

- The basic file structure of this repo *(excluding any contributions)* as follows:

  > ```
  > /DSA/
  > |
  > ├── .github
  > |       ├── data
  > |       |   └── contributors-log.json
  > |       ├── scripts
  > |       |   ├── convert_to_html_tables.py
  > |       |   ├── update_contributors_log.py
  > |       |   └── update_index_md.py
  > |       └── workflows
  > |           ├── linter.yml
  > |           ├── deploy-gh-pages.yml
  > |           └── update-contributors-details.yml
  > ├── _includes
  > |       └── head-custom.html
  > ├── assets
  > |       └── img
  > |           ├── page-cover.png
  > |           └── favicon.icon
  > ├── index.md
  > ├── _config.yml
  > ├── .gitignore
  > ├── LICENSE
  > ├── CODE_OF_CONDUCT.md
  > ├── CONTRIBUTING.md
  > └── README.md
  > ```

- All of the main content of this repo lies within the `Theory` and `Solved-Problems` directory. All of your writing content will go down to `Theory` directory and all your solved problem will go to `Solved-Problem` directory.

- 

- Before you begin with your project contribution, make sure you create a new directory *(or)* folder within the repo with your project name.

  > [!NOTE]
  > It's suggested to use any of the following naming conventions for the directory *(or)* folder:
  > 
  > | Format | Example |
  > | :---: | :---: |
  > | Separated with dashes | `/my-project-name/` |
  > | Separated with underscores | `/my_project_name/` |
  >
  > Note that you can also use spaces *(like `/my project name/`)* but it's recommended to use any of the above-mentioned naming conversions.

- You can write simple docs for your project using [markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax "visit official GitHub Markdown Docs"). You can write descriptions, add screenshots or even upload a video. **Just make sure documentation is done within files named `README.md` *(or)* `index.md`**

- Even if you're project is small, try to keep it organized by keeping related files within their directories/folders

  <details>
  <summary>Here's an sample example</summary>
  <div>
  
  ```
  /Java-Projects/
  |
  ├── <Default-files>
  └── <your-project-name>
          ├── .pmd
          |   └── pmd_rules.xml
          ├── .settings
          |   ├── org.eclipse.jdt.core.prefs
          |   └── org.eclipse.core.resources.prefs
          ├── docs
          |   └── <generated-javadocs>
          ├── src
          |   └── <project-package-name>
          |           └── <all-java-source-code>  
          └── README.md
  ```
  
  > [!NOTE]
  > Note that this is an example to give you an idea of organizing files, no need to follow the exact pattern. You can come up with your own hierarchy based on your requirements.
  
  </div>
  </details>

### Contributing

Now that you have a basic understanding of this repo, let's talk a bit about the process of contributing...

- **Step 1:** You start you setting up the environment [*(as discussed above)*](#setting-up-environment).

- **Step 2:** Now start by [forking](https://github.com/Grow-with-Open-Source/Java-Projects/fork "let's fork the repo") the repository.

- **Step 3:** Clone the forked repository to your local machine.
  ```bash
  #cloning the repo
  git clone https://github.com/<your-github-user-name>/Java-Projects.git
  
  #entering the project directory
  cd Java-Projects
  ```

- **Step 4:** Create a new branch to work on your contribution. use the following command:
  ```bash
  # create and check out to new branch
  git checkout -b <your-project-name>
  
  # check your branch currently in
  git branch
  ```

- **Step 5:** Now go ahead and create your own directory/folder with your project name with a proper naming convention and finish your project while maintaining a [file structure](#file-structure) & following other rules [*(as discussed above)*](#instructions-and-guidelines).

- **Step 6:** Make sure you commit each and every change while working on your project parallelly, *(like one commit for creating `index.js`, another for writing a piece of code, and so on...)*. Using the following command:
  ```bash
  # tracking or staging the changes
  git add .
  
  # commiting the changes
  git commit -m "<related-short-message>
  ```

  > [!IMPORTANT]
  > Make sure to commit your each and every change with proper description

- **Step 7:** After committing all the changes and completion of your work. push your commit to your forked repo, using the following commands:
  ```bash
  # check your branch name
  git branch
  
  # push your commit to the origin repo
  git push origin <your-branch-name>
  ```

- **Step 8:** Now, create a pull request to the [original repo](https://github.com/Grow-with-Open-Source/Java-Projects). [Learn about Pull requests](https://docs.github.com/articles/using-pull-requests "official GitHub documentation")

- **Step 9:** After creating the pull request wait till the linting checks are done, if there's any issue with your Java code then the checks won't pass. And if the checks won't pass you have to fix the errors, you can check the linting workflow to know where the error occurred. If you need any help, you can contact the maintainer within the PR.

- **Step 10:** If the linting checks are done and your code passes the liniting checks, then wait for the maintainer to review your code and merge the pull request. If there's any issue with your PR, the maintainer will contact you and with the help of the maintainer you can resolve the issue, so that the maintainer merge your PR.

When the maintainer merges your PR, you have successfully made your *(probably first)* open-source contribution to showcase your learning and provide a reference to a complete newbie. Everybody can see your work and make use of it. Good job, mate !!...

## Rules and Regulations

Here are some ground rules that you need to follow:

- It's important for you to commit to each and every change. Don't just finish all of your work with a single commit. If you're a newbie, it will only be tolerated 3 times.
- Sending several pull requests for a single post is not accepted.
- Your Pull Request will not be merged, if you have modified, changed or deleted any files or content that doesn't belong to you.
- Pull Request containing any illegal, NFSW or any other content which doesn't help others in any way possible will be closed immediately.
- The Pull Request will only be merged if everything seems to be in order. You be notified if you did something wrong, and your pull request will only be merged if the notified changes are made.