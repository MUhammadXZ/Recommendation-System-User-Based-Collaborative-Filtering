from flask import Flask, request, jsonify
import Recommendation_System_User_Based_Collaborative_Filtering


app = Flask(_name_)



def recommend_items(picked_userid):
  

    return ranked_item_score.head(m).to_dict()


@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id', type=int)

    if user_id is None:
        return jsonify({'error': 'user_id is required'}), 400

    recommended_items = recommend_items(user_id)
    return jsonify(recommended_items)


if _name_ == '_main_':
    app.run(debug=True)