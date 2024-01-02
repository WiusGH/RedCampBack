from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RedCamp.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)
CORS(app)


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    date = db.Column(db.String(255))
    time = db.Column(db.String(255))
    mode = db.Column(db.String(255))
    capacity = db.Column(db.String(255))
    full = db.Column(db.Boolean)
    participants = db.relationship('Participant', backref='match', lazy=True)


class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255))
    team = db.Column(db.String(255))
    rental = db.Column(db.Boolean)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    team = db.Column(db.String(255))
    reputation = db.Column(db.Integer)


with app.app_context():
    db.create_all()


@app.route('/')
def homepage():
    return "Holi"


# API route to get all matches
@app.route('/api/all_matches', methods=['GET'])
def get_all_matches():
    all_matches = Match.query.all()
    return jsonify({'matches': [{'id': match.id, 'name': match.name, 'description': match.description,
                                 'date': match.date, 'time': match.time, 'mode': match.mode,
                                 'capacity': match.capacity, 'full': match.full} for match in all_matches]})


# API route to get all matches for a specific user
@app.route('/api/user_matches/<int:user_id>', methods=['GET'])
def get_user_matches(user_id):
    user = User.query.get_or_404(user_id)
    matches = user.matches
    return jsonify({'matches': [{'id': match.id, 'name': match.name, 'team': match.team,
                                 'rental': match.rental, 'match_id': match.match_id} for match in matches]})


# API rout to get all participants for a specific match
@app.route('/api/participants/<int:match_id>', methods=['GET'])
def get_participants(match_id):
    match = Match.query.get_or_404(match_id)
    participants = match.participants
    return jsonify({'participants': [{'id': participant.id, 'name': participant.name, 'team': participant.team,
                                     'rental': participant.rental, 'match_id': participant.match_id}
                                     for participant in participants]})


# API route to get all users
@app.route('/api/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify({'users': [{'id': user.id, 'name': user.name, 'nickname': user.nickname,
                               'team': user.team, 'reputation': user.reputation} for user in users]})


@app.route('/api/participants/<int:match_id>', methods=['POST'])
def add_participant(match_id):
    try:
        match = Match.query.get_or_404(match_id)

        new_player_data = request.json
        print(f"Received new player data: {new_player_data}")

        participant = Participant(**new_player_data)
        match.participants.append(participant)

        db.session.commit()

        print("Participant added successfully")

        return jsonify({'message': 'Participant added successfully'}), 201
    except Exception as e:
        print(f"Error adding participant: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
