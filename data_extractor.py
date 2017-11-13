headers_key = [
    'id',
    'user_id',
    'archive_url',
    'general_comment',
    'language',
    'project_id',
    'project_name',
    'grader_name',
]


def get_description_row_from_json(_json):
    """
    get csv row
    """
    return (
        _json['id'],
        _json['user_id'],
        _json['archive_url'],
        _json['general_comment'],
        _json['language'],
        _json['project_id'],
        _json['project']['name'],
        _json['grader']['name'],
    )
