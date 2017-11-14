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
CONTENT_HEADERS_KEY = [
    'submission_id',
    'id',
    'sha',
    'path',
    'size',
    'blob',
    'created_at',
    'updated_at',
    'comments_count',
]


def get_content_row_from_json(_json):
    return (
        _json['submission_id'],
        _json['id'],
        _json['sha'],
        _json['path'],
        _json['size'],
        _json['blob'],
        _json['created_at'],
        _json['updated_at'],
        _json['comments_count'],
    )


"""
    {
        "category": "awesome",
        "content_id": 27758935,
        "id": 1698559,
        "user_id": 25252,
        "body": "Nice job using `discrete_distibution` to resample the particles proportional to their weights.\n\nAnother option would be to implement the `resampling wheel` discussed by Sebastian Thrun in the [Python Particle Filters lesson](https://classroom.udacity.com/nanodegrees/nd013/parts/40f38239-66b6-46ec-ae68-03afd8a601c8/modules/2c318113-724b-4f9f-860c-cb334e6e4ad7/lessons/48704330/concepts/487480820923).",
        "position": 185,
        "created_at": "2017-05-22T22:42:43.921Z",
        "updated_at": "2017-05-22T22:42:43.921Z"
    },
"""
COMMENT_HEADERS_KEY = [
    'category',
    'content_id',
    'id',
    'user_id',
    'body',
    'position',
    'created_at',
    'updated_at',
]


def get_comment_row_from_json(_json):
    return (
        _json['category'],
        _json['content_id'],
        _json['id'],
        _json['user_id'],
        _json['body'],
        _json['position'],
        _json['created_at'],
        _json['updated_at'],
    )
