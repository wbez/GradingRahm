#!/usr/bin/env python

"""
Functions specific to the Grading Rahm app.
"""

import copytext
import app_config
from render_utils import flatten_app_config, JavascriptIncluder, CSSIncluder
from collections import OrderedDict

def make_rahm_context(asset_depth=0):
    """
    Create a base-context for rendering views.
    Includes app_config and JS/CSS includers.
    `asset_depth` indicates how far into the url hierarchy
    the assets are hosted. If 0, then they are at the root.
    If 1 then at /foo/, etc.
    """
    context = flatten_app_config()
    context['TOPICS'] = OrderedDict()
    copy = copytext.Copy(app_config.COPY_PATH)

    topics = copy['topics']

    for topic in topics:
        slug = topic['value']
        story_sheet = '%s_story' % slug
        grades_sheet = '%s_grades' % slug

        topic_context = {}
        topic_context['story'] = copy[story_sheet]
        topic_context['grades'] = copy[grades_sheet]
        context['TOPICS'][slug] = topic_context

        print topic_context


    context['COPY'] = copytext.Copy(app_config.COPY_PATH)
    context['JS'] = JavascriptIncluder(asset_depth=asset_depth)
    context['CSS'] = CSSIncluder(asset_depth=asset_depth)



    return context