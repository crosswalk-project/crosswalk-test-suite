## Introduction

This tools is for statistics merged commit information, including
commit id, summary, author, commit date, test add/update/delete number,
file changed, code insertion, code deletion.

- Usage:

        git_stat.py -h | --help
        git_stat.py -r <git-repository> [-s <since>] [-u <until>] [-a <author>] [-o <output>]


- Options:

  -r, --repo         Specify git repository

  -s, --since        optional, Specify the start date of merged commit

  -u, --until        optional, Specify the end date of merged commit

  -a, --author       optional, Specify merged commit author

  -o, --output       optional, Specify an output file for statistics


## Difference

Becuase commit log order are different when using pull request strategy
and directly git commit strategy, there are two different scripts:

- **git_stat.py**: only count merged commit from start date to end date ,
  not contain merged pull request commit.
- **git_stat_pr.py**: count the commit which merged by pull request
  from start date to end date.


## How to Use

    Count all commits merged in repository:
    $ git_stat.py -r <git-repository>

    Count commits merged in a period:
    $ git_stat.py -r <git-repository> -s <since> -u <until>

    Count commits submitted by author:
    $ git_stat.py -r <git-repository> -a <name or email>

    Count commits and save result to an output file:
    $ git_stat.py -r <git-repository> -o <output>


    Count all commits merged via pull request in repository:
    $ git_stat_pr.py -r <git-repository>

    Count commits merged via pull request in a period:
    $ git_stat_pr.py -r <git-repository> -s <since> -u <until>

    Count commits merged via pull request by author:
    $ git_stat_pr.py -r <git-repository> -a <name or email>

    Count commits merged via pull request and save result to an output file:
    $ git_stat_pr.py -r <git-repository> -o <output>

