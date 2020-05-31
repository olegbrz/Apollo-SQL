![banner](images/apollo_banner.png)

[![MIT license](https://img.shields.io/github/license/olegbrz/Apollo-SQL?color=teal)](https://lbesson.mit-license.org/) ![top language](https://img.shields.io/github/languages/top/olegbrz/Apollo-SQL) ![Code size](https://img.shields.io/github/languages/code-size/olegbrz/Apollo-SQL?color=green%20green) ![commit activity](https://img.shields.io/github/commit-activity/m/olegbrz/Apollo-SQL?color=green%20green) ![tag](https://img.shields.io/github/v/release/olegbrz/Apollo-SQL?include_prereleases)

Apollo SQL is a lightweight Oracle database manager developed by a group of students from Málaga's University.

This CLI program written in Python allows you to connect to remote database to query and relate data with predesigned queries (modify [`core/queries.sql`](core/queries.sql) and [`core/queries.py`](core/queries.py)), show whole tables, and insert data into them.

## Installation

```bash
git clone https://github.com/olegbrz/Apollo-SQL.git
```

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [cx-Oracle module](https://pypi.org/project/cx-Oracle/)
- [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html)

## Usage

The usage is pretty simple, just launch the [`main.py`](main.py) file:

```bash
python main.py
```

It works as a CLI (command-line interface), so you just need a command line to work with it.

## Demo

![demo](images/demo.png)

## External packages (included)

The program uses external open-source packages (license included in every package in [`extra/`](extra/)):

- [tabulate 0.8.7](https://pypi.org/project/tabulate/)
