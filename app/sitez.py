# sitez.py

from flask import Flask, jsonify, request, Blueprint
from app.security import token_required
from app.db import sitez

bp = Blueprint('sitez', __name__)


@bp.route('/site/<int:param>/',methods=['GET'])
def get_site(param):
	# https://www.geeksforgeeks.org/python-find-dictionary-matching-value-in-list/
	res = next((sub for sub in sitez if sub['id'] == param), None)
	if res: 
		return jsonify({"result": res})
	else:
		return jsonify({"result": "Nothing here"}), 404


@bp.route('/site/search-site',methods=['GET'])
@token_required('user')
def get_search_site():
	site = request.args.get('site')
	# https://www.geeksforgeeks.org/python-find-dictionary-matching-value-in-list/
	res = next((sub for sub in sitez if sub['site'] == site), None)
	if res: 
		return jsonify({"result": res})
	else:
		return jsonify({"result": "Nothing here"}), 404


@bp.route('/sitez',methods=['GET'])
@token_required('user')
def get_netz():
    return jsonify(sitez)

@bp.route('/sitez', methods=['POST'])
def add_sitez():
    """
    curl -X POST -H "Content-Type: application/json" -d '{
    "id": 4,
    "site": 'BLACK',
    "comment": "bla...."
    }' http://localhost:5000/api/netz
    """
    sitez.append(request.get_json())
    return '', 204