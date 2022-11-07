import datetime

from flask import request, make_response, jsonify

from sweater import app, db
from sweater.models import Cities, Shops, Streets


@app.route('/city', methods = ['GET'])
def city():
    cities = Cities.query.all()
    return [{"id": city.id, "name": city.name} for city in cities]

@app.route('/city/<int:id>/street', methods = ['GET'])
def street(id):
    city = Cities.query.get(id).name
    streets = Streets.query.filter(Streets.city == city)
    return [{"id": street.id, "name": street.name, "city": street.city} for street in streets]

@app.route('/shop', methods = ['POST','GET'])
def shop():
    if request.method == 'GET':
        city = request.args.get('city')
        street = request.args.get('street')
        open = request.args.get('open')

        currTime = datetime.datetime.now().time()
        shops = Shops.query.all()

        if (street or city or open) != None:
            ans = []
            avg = 0

            if city:
                city = city.capitalize()
                avg += 1
            if street:
                street = street.capitalize()
                avg += 1
            if open != None:
                open = int(open)
                avg += 1

            for shop in shops:
                score = 0
                if shop.city == city: score += 1
                if shop.street == street: score += 1
                if open != None:
                    if open == 1 and (shop.Open <= currTime and shop.Close >= currTime):
                        score += 1
                    elif open == 0 and (shop.Open >= currTime and shop.Close <= currTime):
                        score += 1

                if score >= avg: ans.append(shop)
            
            return [{"id": shop.id, "name": shop.name, "city": shop.city, "street": shop.street, "openIn": f"{shop.Open}", "closeIn": f"{shop.Close}"} for shop in ans]

        return [{"id": shop.id, "name": shop.name, "city": shop.city, "street": shop.street, "openIn": f"{shop.Open}", "closeIn": f"{shop.Close}"} for shop in shops]

    elif request.method == 'POST':
        r = request.get_json()
        try:
            shop = Shops(city=r["city"], street=r["street"], name=r["name"], home=r["home"], Open=r["openIn"], Close=r["closeIn"])
            db.session.add(shop)
            db.session.commit()

            return make_response(jsonify(id=shop.id))
        except Exception as err:
            print(err)
            return make_response(err, status_code=400)


@app.errorhandler(404)
def page_not_found(msg):
    return msg, 400

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=False, host='0.0.0.0')