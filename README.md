# Apollo SQL

![banner](images/apollo_banner.png)

Apollo SQL is a lightweight (140 KB!) Oracle database manager developed by a group of students from Málaga's University.

This CLI program written in Python allows you to connect to remote database to query and relate data with predesigned queries (modify `./core/queries.py`), show whole tables, and insert data into them.

## Installation

```bash
git clone https://github.com/olegbrz/Apollo-SQL.git
```

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [cx-Oracle module](https://pypi.org/project/cx-Oracle/)
- [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html)

## Usage

The usage is pretty simple, just launch the `main.py` file:

```bash
python main.py
```

It works as a CLI (command-line interface), so you just need a command line to work with it.

## Demo

<img src="images/demo.png" width="400" align="center">

## External packages (included)

The program uses external open-source packages (license included in every package in `./extra/`):

- [tabulate 0.8.7](https://pypi.org/project/tabulate/)
