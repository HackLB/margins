"""
Haystack settings for margins project.
"""

# --------------------------------------------------
# Haystack settings
# --------------------------------------------------

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': PROJECT_NAME,
    },
}