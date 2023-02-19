from flask_restx.reqparse import RequestParser
from flask_restx.inputs import positive

page_parser: RequestParser = RequestParser(bundle_errors=True)
page_parser.add_argument(name='page', type=positive, location='args', required=False, default=None)
page_parser.add_argument(name='status', type=str, location='args', required=False, default=None)
