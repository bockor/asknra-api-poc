# netz.py

from flask import Flask, jsonify, request, Blueprint
from app.security import token_required
from app.db import netz

bp = Blueprint('netz', __name__)


@bp.route('/net/<int:param>',methods=['GET'])
@token_required('user')
def get_net(param):
	# https://www.geeksforgeeks.org/python-find-dictionary-matching-value-in-list/
	res = next((sub for sub in netz if sub['id'] == param), None)
	if res: 
		return jsonify({"result": res})
	else:
		return jsonify({"result": "Nothing here"}), 404


@bp.route('/net/search-net',methods=['GET'])
@token_required('user')
def get_search_net():
	network = request.args.get('network')
	# https://www.geeksforgeeks.org/python-find-dictionary-matching-value-in-list/
	res = next((sub for sub in netz if sub['network'] == network), None)
	if res: 
		return jsonify({"result": res})
	else:
		return jsonify({"result": "Nothing here"}), 404


@bp.route('/netz',methods=['GET'])
@token_required('user')
def get_netz():
    return jsonify(netz)

@bp.route('/netz', methods=['POST'])
def add_netz():
    """
    curl -X POST -H "Content-Type: application/json" -d '{
    "id": 4,
    "network": '4.0.0.0/8',
    "comment": "bla...."
    }' http://localhost:5000/api/netz
    """
    netz.append(request.get_json())
    return '', 204