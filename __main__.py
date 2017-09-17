import sys
import os
import re
import json
import time
from pprint import pprint
from docopt import docopt

from logger import logger

__doc__ = """
    IronPython-Stubs

    Usage:
      chm_parser parse_pages <year> <in-html-dir> [--output=<DIR>] [--json-directory=<DIR>]
                                [--start-index=<INT>] [--end-index=<INT>] [--no-minify]
                                [--no-html] [--no-json] [--html-test-mode] [--single-file=<FILE>]
      chm_parser parse_namespaces <year> <hhc-filepath> [--json-directory=<DIR>] [--no-minify]
      chm_parser parse_members <year> <hhk-filepath> <in-html-dir> <db-index-filepath> [--json-directory=<DIR>] [--no-minify]
                                                                                       [--no-html] [--no-json]
      chm_parser merge <out-2015> [--no-json]
      chm_parser bootstrap <out-html-dir> <db-index.json> <out-merge-dir>
      chm_parser parse_news <year> <whastnew> [--output=<DIR>]
      chm_parser upload <db-index.json>
      chm_parser -h | --help
      chm_parser --version

    Options:
      --output DIR           Html output directory [default: {default_out_dir}].
      --json-directory DIR   Json output directory filepath [default: {json_out_dir}].
      --no-minify            Disable minify output [default: False].
      --start-index INT      Start index [default: ].
      --end-index INT        End index [default: ].
      --single-file FILE     Testing Mode. Injects <html> and other tags.
      --html-test-mode       Testing Mode. Injects <html> and other tags [default: False].
      --no-json              Don't write json file [default: False].
      --no-html              Don't write html files [default: False].
      -h --help              Show this screen.

    """.format(default_out_dir=DEFAULT_OUT_HTML_DIR,
               json_out_dir=DEFAULT_OUT_JSON_DIR)

# TODO: Improve path/args
# TODO: Create batch command for all

__version__ = '1.0.0'
arguments = docopt(__doc__, version=__version__)
# logger.info(arguments)

# Global Option
minify_json = not arguments['--no-minify']
year = arguments['<year>']
out_json_dir = arguments['--json-directory'].format(year=year)

make_html = not arguments['--no-html']
make_json = not arguments['--no-json']

if arguments['--start-index']:
    MIN = int(arguments['--start-index'])
else:
    MIN = None
if arguments['--end-index']:
    MAX = int(arguments['--end-index'])
else:
    MAX = None

############################
# UPLOAD TO CONSTRUCTOR.IO #
############################
if arguments['upload']:
    db_index_path = arguments['<db-index.json>']
    upload(db_index_path)


##############
# PARSE NEWS #
##############
if arguments['parse_news']:
    whatsnew_html_path = arguments['<whastnew>']
    out_whatsnew_html = arguments['--output'].format(year=year)

    soup = parse_news(whatsnew_html_path)
    filename = '{year}.htm'.format(year=year)
    write_html(soup.prettify(), filename, directory=out_whatsnew_html)

    print('Done.')

############################
# Bootstrap #
############################
if arguments['bootstrap']:
    timer = Timer()

    out_html_dir = arguments['<out-html-dir>']
    db_index_path = arguments['<db-index.json>']
    out_merge_dir = arguments['<out-merge-dir>']

    bootstrap(db_index_path, out_html_dir, out_merge_dir)

    print('Done: {} seconds'.format(timer.stop()))

