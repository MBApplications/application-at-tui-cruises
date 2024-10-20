# Analysis of Cruise Ship Data Towards Performance Trends

The goal of this project is to analyze the provided dataset for two Cruise ships and develop a narrative explaining the
performance trends (e.g.: efficiency, propulsion, power generation, etc.).

# Table of Contents

<!-- TOC -->

- [Analysis of Cruise Ship Data Towards Performance Trends](#analysis-of-cruise-ship-data-towards-performance-trends)
- [Table of Contents](#table-of-contents)
- [Project Plan and Execution](#project-plan-and-execution)
- [Used Software](#used-software)
- [Installation / Usage](#installation--usage)
- [Folder-Order](#folder-order)
- [To-Do](#to-do)
- [Contributions](#contributions)
- [Acknowledgments](#acknowledgments)

<!-- /TOC -->

# Project Plan and Execution
Planning is done using the Kanban-board provided by the Github Web-UI. Check out the repository for further details of the incremental steps that were carried out.

# Used Software
Programming is performed using the open source distribution of VS Code from Microsoft.

# Installation / Usage
- start the main.ipynb-script in the src-subfolder

# Folder-Order
```
|   .gitignore                        <-- file-list ignored by github
|   README.md                         <-- readme-overview
|
+---data
|       data.csv                      <-- raw data
|
+---docs
|       schema.pdf                    <-- scheme send by TUI
|       task_description.pdf          <-- task send by TUI
|
+---src
|   |   .env                          <-- constants for processing (paths etc.)
|   |   main.ipynb                    <-- main, notebook for analysis
|   |
|   \---tui_cruises_data_science
|       |   data_reader.py            <-- data-reader class
|       |   data_visualization.py     <-- visualization class
|       |   __init__.py               <-- class embedding as py-module
|       |
|
\---target
        main_export.html              <-- html export of main notebook
```

# To-Do
- alternatively start the docker container
- transfer Data to SQL-DB (respecting 3.5 normal forms)
- extraction of requirements.txt using Python-venv
- data visualization with Web-UI (Django or Dash, example: https://dash.gallery/dash-opioid-epidemic/)
- dockerization of main.py, exposing web-UI to localhost
- improved branch-management and connection to Kanban-board (agiles management)
- improved object-oriented structure (classes, subclasses, modules) and sustainable programming (markdown-description, improved commit-messages etc.)

# Contributions
This project has only contributer, which is the applicant himself.

# Acknowledgments
Data obtained from TUI Cruises GmbH in the context of an application for an internship as a data scientist.