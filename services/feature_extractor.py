import re
from urllib.parse import urlparse

class FeatureExtractor:
    def extract_url_features(self, url):
        features = {}
        parsed = urlparse(url)
        features['url_length'] = len(url)
        features['num_dots'] = url.count('.')
        features['num_hyphens'] = url.count('-')
        return features
