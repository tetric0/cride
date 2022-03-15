#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv

from cride.circles.models import Circle

with open('cride/fixtures/circles.csv') as f:
    reader = csv.DictReader(f)

    for row in reader:
        circle = Circle(
            name=str(row['name']),
            slug_name=str(row['slug_name']),
            is_public=bool(int(row['is_public'])),
            is_verified=bool(int(row['is_verified'])),
            members_limit=int(row['members_limit']),
            is_limited=(int(row['is_limited'])!=0)
        )
        circle.save()