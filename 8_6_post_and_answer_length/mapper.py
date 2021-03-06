#!/usr/bin/env python

import re
import csv 
import sys

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

    if len(line) < 5:
        continue
    id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
    if node_type == "question":
        print "{0}\t{1}\t{2}".format(id, node_type, len(body))
    elif node_type == "answer":
        print "{0}\t{1}\t{2}".format(parent_id, node_type, len(body))
