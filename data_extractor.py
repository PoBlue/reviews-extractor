#!/usr/bin/env python
# -*- coding: utf-8 -*-

headers_key = [
    'id',
    'user_id',
    'archive_url',
    'general_comment',
    'language',
    'project_id',
    'project_name',
    'grader_name',
    'review_url',
    'is_training',
    'result_reason',
    'created_at',
    'completed_at',
]


def get_description_row_from_json(_json):
    """
    get csv row
    """
    url = "https://review.udacity.com/#!/reviews/" + str(_json['id'])
    if 'grader' not in _json:
        _json.update({ 'grader': {'name': 'none'} })
    return (
        _json['id'],
        _json['user_id'],
        _json['archive_url'],
        _json['general_comment'],
        _json['language'],
        _json['project_id'],
        _json['project']['name'],
        _json['grader']['name'],
        url,
        _json['is_training'],
        _json['result_reason'],
        _json['created_at'],
        _json['completed_at'],
    )
