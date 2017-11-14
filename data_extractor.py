#!/usr/bin/env python
# -*- coding: utf-8 -*-

DESC_HEADERS_KEY = [
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

"""
    {
        "submission_id": 511437,
        "id": 27815301,
        "sha": "7bfb8e95ac2ccf7ff048c278cc13ce06057d1d57",
        "path": "fresh_tomatoes.py",
        "size": 5463,
        "blob": "https://udacity-reviews-uploads.s3-us-west-2.amazonaws.com/_git_blobs/7b/fb/8e95ac2ccf7ff048c278cc13ce06057d1d57",
        "created_at": "2017-05-23T04:30:07.242Z",
        "updated_at": "2017-05-23T04:30:07.242Z",
        "comments_count": 1
    },
"""
