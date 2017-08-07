from flask_restful import Resource, reqparse, marshal_with, fields, abort
from database import session
from models import Products

prod_fields = {

        'title' : fields.String(),
        'price' : fields.String(),
        'product_url' : fields.String(),
}
parser = reqparse.RequestParser()
parser.add_argument('price', type=str, required=True)

class AdidasProduct(Resource):

    @marshal_with(prod_fields)
    def get(self,id):
        prod = session.query(Products).filter(Products.id == id).first()
        if not prod:
            abort(404, message="Product #{} does not exist".format(id))
        return prod

    @marshal_with(prod_fields)
    def put(self,id):
        prod = session.query(Products).filter(Products.id == id).first()
        if not prod:
            abort(404, message="Product #{} does not exist".format(id))
        parser_args = parser.parse_args()
        prod.price = parser_args['price']
        session.add(prod)
        session.commit()
        return prod

    @marshal_with(prod_fields)
    def delete(self,id):
        prod = session.query(Products).filter(Products.id == id).first()
        if not prod:
            abort(404, message="Product #{} does not exist".format(id))
        session.delete(prod)
        session.commit()
        return prod