from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AllMatches(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    date = db.Column(db.String(255))
    time = db.Column(db.String(255))
    mode = db.Column(db.String(255))
    capacity = db.Column(db.String(255))
    full = db.Column(db.Boolean)


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255))
    team = db.Column(db.String(255))
    rental = db.Column(db.Boolean)
    match_id = db.Column(db.Integer, db.ForeignKey('all_matches.id'), nullable=False)
    match = db.relationship('AllMatches', backref=db.backref('matches', lazy=True))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    team = db.Column(db.String(255))
    reputation = db.Column(db.Integer)


