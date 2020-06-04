![banner](images/apollo_banner.png)

[![MIT license](https://img.shields.io/github/license/olegbrz/Apollo-SQL?color=teal)](https://lbesson.mit-license.org/) ![top language](https://img.shields.io/github/languages/top/olegbrz/Apollo-SQL) ![Code size](https://img.shields.io/github/languages/code-size/olegbrz/Apollo-SQL?color=green%20green) ![commit activity](https://img.shields.io/github/commit-activity/m/olegbrz/Apollo-SQL?color=green%20green) ![tag](https://img.shields.io/github/v/release/olegbrz/Apollo-SQL?include_prereleases) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3875722.svg)](https://doi.org/10.5281/zenodo.3875722)

Apollo SQL is a lightweight Oracle database manager developed by a group of students from Málaga's University.

This CLI program written in Python allows you to connect to remote database to query and relate data with predesigned queries (modify [`custom/queries.sql`](custom/queries.sql) and [`custom/db_data_.py`](custom/db_data_.py)), show whole tables, and insert data into them.

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [cx-Oracle module](https://pypi.org/project/cx-Oracle/)
- [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html)

## Installation

```bash
git clone https://github.com/olegbrz/Apollo-SQL.git
```

## Usage

The usage is pretty simple, just launch the [`main.py`](main.py) file:

```bash
python main.py
```

It works with a CLI (command-line interface), so you just need a command line to work with it.

In the first start, you will need to setup in settings the following connection parameters:

- `host`
- `port`
- `sid`
- `username`
- `password`

The settings persist in memory in the `config.ini` file, which will be created automatically on first start.

## Demo

Here are some examples from the interface (main menu, settings, and a query) running on Windows Powershell 5.1:

![demo](images/demo.png)

The program also allows to perform customized queries from the menu:

![demo1](images/demo1.png)

Relate and insert data functionalities:

![demo2](images/demo2.png)

## External packages (included)

The program uses external open-source packages (license included in every package in [`extra/`](extra/)):

- [tabulate 0.8.7](https://pypi.org/project/tabulate/)
