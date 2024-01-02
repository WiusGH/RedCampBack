from main import db, Match, Participant, User


def populate_data():
    # Sample data for AllMatches
    match_data = [
        {
            'name': 'Partida estándar',
            'description': 'Partida estándar para novatos',
            'date': 'Lunes 25/12',
            'time': '16:00 a 18:00',
            'mode': 'Deathmatch',
            'capacity': '10',
            'full': False
        },
        {
            'name': 'Partida estándar',
            'description': 'Partida estándar para novatos matutina',
            'date': 'Martes 26/12',
            'time': '10:00 a 12:00',
            'mode': 'Deathmatch',
            'capacity': '16',
            'full': False
        },
        {
            'name': 'Partida tracer',
            'description': 'Partida nocturna con tracers',
            'date': 'Miércoles 27/12',
            'time': '20:00 a 22:00',
            'mode': 'Tracer Night',
            'capacity': '12',
            'full': False
        }
    ]

    # Sample data for Matches
    user_data = [
        {
            'name': 'Carlos',
            'nickname': 'Carlitos',
            'team': 'Equipo Alpha',
            'reputation': 100
        },
        {
            'name': 'Juan',
            'nickname': 'Juancho',
            'team': 'Equipo Alpha',
            'reputation': 100
        },
        {
            'name': 'Julio',
            'nickname': 'julian',
            'team': 'Equipo Beta',
            'reputation': 100
        },
        {
            'name': 'César',
            'nickname': 'César',
            'team': 'Equipo Beta',
            'reputation': 100
        },
        {
            'name': 'Francisca',
            'nickname': 'Francisca',
            'team': 'Equipo Charlie',
            'reputation': 100
        },
        {
            'name': 'Gonzalo',
            'nickname': 'Gonza',
            'team': 'Equipo Charlie',
            'reputation': 100
        },
        {
            'name': 'Camila',
            'nickname': 'Cami',
            'team': 'Equipo delta',
            'reputation': 100
        },
        {
            'name': 'Wilsconidel',
            'nickname': 'Wius',
            'team': 'Equipo Delta',
            'reputation': 100
        },
        {
            'name': 'Matias',
            'nickname': 'Mati',
            'team': 'Equipo Echo',
            'reputation': 100
        },
        {
            'name': 'Maria',
            'nickname': 'Mary',
            'team': 'Equipo Echo',
            'reputation': 100
        }
    ]

    participants_data = [
        {
            'name': 'Maria',
            'team': 'Echo',
            'rental': False,
            'match_id': 1
        },
        {
            'name': 'Gonzalo',
            'team': 'Charlie',
            'rental': False,
            'match_id': 1
        },
        {
            'name': 'Carlos',
            'team': 'Alpha',
            'rental': False,
            'match_id': 1
        },
        {
            'name': 'César',
            'team': 'Beta',
            'rental': True,
            'match_id': 1
        },
        {
            'name': 'Wilsconidel',
            'team': 'Delta',
            'rental': False,
            'match_id': 1
        },
        {
            'name': 'Camila',
            'team': 'Delta',
            'rental': True,
            'match_id': 1
        },
        {
            'name': 'Julio',
            'team': 'Beta',
            'rental': False,
            'match_id': 1
        },
        {
            'name': 'Juan',
            'team': 'Alpha',
            'rental': True,
            'match_id': 1
        }
    ]

    # Populate AllMatches
    for data in match_data:
        match = Match(**data)
        db.session.add(match)

    # Commit changes to AllMatches before populating Matches
    db.session.commit()

    # Populate Matches
    for data in user_data:
        user = User(**data)
        db.session.add(user)

    # Commit changes
    db.session.commit()

    for data in participants_data:
        participant = Participant(**data)
        db.session.add(participant)

    db.session.commit()


if __name__ == '__main__':
    # Set up the Flask app and database
    from main import app

    with app.app_context():
        # Call the function to populate the data
        populate_data()

    print('Data population complete.')
