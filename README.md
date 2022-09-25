# Traffic-data-warehouse

***

Data Engineering: Data warehouse tech stack with MySQL, DBT, Airflow

**Table of Contents**
- [Traffic-data-warehouse](#Traffic-data-warehouse)
  - [Overview](#overview)
  - [About](#about)
  - [Project Structure](#project-structure)
    - [.github](#.github)
    - [data](#data)
    - [notebooks](#notebooks)
    - [scripts](#scripts)
    - [tests](#tests)
    - [root folder](#root-folder)
  - [Installation guide](#Installation-guide)

***

## Overview

A city traffic department wants to collect traffic data using swarm UAVs (drones) from a number of locations in the city and use the data collected for improving traffic flow in the city and for a number of other undisclosed projects. Your startup is responsible for creating a scalable data warehouse that will host the vehicle trajectory data extracted by analyzing footage taken by swarm drones and static roadside cameras.


## About

The data warehouse should take into account future needs, organise data such that a number of downstream projects query the data efficiently. You should use the Extract Load Transform (ELT) framework using DBT.  Unlike the Extract, Transform, Load (ETL), the ELT framework helps analytic engineers in the city traffic department setup transformation workflows on a need basis.  



![Alt text](Tech_stack_flow.png?raw=true "Tech stack")


## Project Structure
The repository has a number of files including python scripts, jupyter notebooks, raw and cleaned data, and text files. Here is their structure with a brief explanation.


### .github
- a configuration file for github actions and workflow

### data
- the folder where the raw, and cleaned datasets' csv files are stored

### notebooks
- `EDA.ipynb`: a jupyter notebook that Explanatory Data Analysis

***
# Location change through time
![Alt text](Path_for_track_id_1.png?raw=true "Tech stack")

***

### scripts
- Different python utility scripts that have different purposes.

### tests


### root folder
- `requirements.txt`: a text file lsiting the projet's dependancies
- `.gitignore`: a text file listing files and folders to be ignored
- `README.md`: Markdown text with a brief explanation of the project and the repository structure.

***
# Speed comparison between different track_id
![Alt text](Speed_comparison_through_time.png?raw=true "Tech stack")

***

## Installation guide
Option 1
```
git clone https://github.com/natyrix/traffic-data-warehouse
cd traffic-data-warehouse
docker-compose up 
```


***

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


[contributors-shield]: https://img.shields.io/github/contributors/natyrix/traffic-data-warehouse.svg?style=for-the-badge
[contributors-url]: https://github.com/natyrix/traffic-data-warehouse/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/natyrix/traffic-data-warehouse.svg?style=for-the-badge
[forks-url]: https://github.com/natyrix/traffic-data-warehouse/network/members
[stars-shield]: https://img.shields.io/github/stars/natyrix/traffic-data-warehouse.svg?style=for-the-badge
[stars-url]: https://github.com/natyrix/traffic-data-warehouse/stargazers
[issues-shield]: https://img.shields.io/github/issues/natyrix/traffic-data-warehouse.svg?style=for-the-badge
[issues-url]: https://github.com/natyrix/traffic-data-warehouse/issues
