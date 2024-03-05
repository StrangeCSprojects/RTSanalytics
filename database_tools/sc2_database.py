# Import any needed modules
from sqlalchemy import create_engine
from sqlalchemy.orm import ClassManager, sessionmaker
from sqlalchemy.util import clsname_as_plain_name
from database_tools.entities.sc2_db_entities import (
    Base,
    Game,
    Play,
    Player,
    Issues,
    PlayerCommand,
)


class SC2_DB:
    """A class for interacting with the SC2 database"""

    engine = None
    Session = None

    @classmethod
    def init(cls, db_name):
        """Initializes database connection"""
        # Establish connection to the database file
        cls.engine = create_engine(f"sqlite:///database_tools/{db_name}.db")
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

        # ID initialization
        cls._game_id_count = 0
        cls._player_id_count = 0
        cls._command_id_count = 0

    @classmethod
    def add_games(cls, game_list):
        with cls.Session() as session:
            for game in game_list:
                id = game[0]
                game_map = game[1]
                game_mode = game[2]
                game_winner_id = game[3]
                existing_game = session.query(Game).filter_by(game_id=id).first()
                if existing_game:
                    # print("This game already resides in database.")
                    continue
                game = Game(
                    game_id=id,
                    map=game_map,
                    mode=game_mode,
                    winner_id=game_winner_id,
                )
                session.add(game)
            session.commit()

    @classmethod
    def add_players(cls, player_list):
        with cls.Session() as session:
            for player_info in player_list:
                id = player_info[0]
                race = player_info[1]
                name = player_info[2]
                existing_player = session.query(Player).filter_by(player_id=id).first()
                if existing_player:
                    # print("This player already resides in database.")
                    continue
                player = Player(player_id=id, name=name, race=race)
                session.add(player)
            session.commit()

    @classmethod
    def add_commands(cls, command_dict: dict):
        with cls.Session() as session:
            for id, c_list in command_dict.items():
                existing_command_list = (
                    session.query(PlayerCommand).filter_by(command_id=id).first()
                )
                if existing_command_list:
                    # print("These commands have already been processed")
                    continue
                # Create an instance of PlayerCommand with keyword arguments
                command = PlayerCommand(command_id=id, commands_list=c_list)
                session.add(command)
            session.commit()

    @classmethod
    def add_plays(cls, play_list):
        with cls.Session() as session:
            for play_info in play_list:
                game_id = play_info[0]
                player_id = play_info[1]
                existing_play = (
                    session.query(Play)
                    .filter_by(game_id=game_id)
                    .filter_by(player_id=player_id)
                    .first()
                )
                if existing_play:
                    # print("This play relationship already resides in database.")
                    continue
                play = Play(game_id=game_id, player_id=player_id)
                session.add(play)
            session.commit()

    @classmethod
    def add_issues(cls, issue_list):
        with cls.Session() as session:
            for issue_info in issue_list:
                game_id = issue_info[0]
                player_id = issue_info[1]
                command_id = issue_info[2]
                existing_issued_commands = (
                    session.query(Issues)
                    .filter_by(game_id=game_id)
                    .filter_by(player_id=player_id)
                    .first()
                )
                if existing_issued_commands:
                    # print("These commands have already been issued")
                    continue
                issue = Issues(
                    command_id=command_id, player_id=player_id, game_id=game_id
                )
                session.add(issue)
            session.commit()

    @classmethod
    def get_player_by_id(cls, id):
        with cls.Session() as session:
            player = session.query(Player).filter_by(player_id=id).first()
            if player:
                return {
                    "player_id": player.player_id,
                    "name": player.name,
                    "race": player.race,
                }
            else:
                return None

    @classmethod
    def get_all_players(cls):
        with cls.Session() as session:
            players = session.query(Player).all()
            for player in players:
                print(
                    f"Player ID: {player.player_id}, Name: {player.name}, Race: {player.race}"
                )

    @classmethod
    def _create_game_id(cls) -> int:
        """Increment and return game id"""
        cls._game_id_count += 1
        return cls._game_id_count

    @classmethod
    def _create_player_id(cls) -> int:
        """Increment and return player id"""
        cls._player_id_count += 1
        return cls._player_id_count

    @classmethod
    def _create_command_id(cls) -> int:
        """Increment and return command id"""
        cls._command_id_count += 1
        return cls._command_id_count

    @classmethod
    def test_func(cls):
        session = cls.Session()

        # 1. Add players
        p1_id = cls._create_player_id()
        p2_id = cls._create_player_id()
        player1 = Player(player_id=p1_id, name="Player 1", race="Terran")
        player2 = Player(player_id=p2_id, name="Player 2", race="Protoss")
        session.add_all([player1, player2])
        session.commit()

        command1 = PlayerCommand(commands_list='[("Attack", 10), ("Defend", 20)]')
        command2 = PlayerCommand(commands_list='[("Scout", 5), ("Harass", 15)]')
        session.add_all([command1, command2])
        session.commit()

        # 3. Add games
        game1 = Game(mode="Ranked", map="Lost Temple", winner=player1)
        game2 = Game(mode="Casual", map="Battlefield of Eternity", winner=player2)
        session.add_all([game1, game2])
        session.commit()

        # 4. Add issues
        issue1 = Issues(
            game_id=game1.game_id,
            player_id=player1.player_id,
            command_id=command1.command_id,
        )
        issue2 = Issues(
            game_id=game2.game_id,
            player_id=player2.player_id,
            command_id=command2.command_id,
        )
        session.add_all([issue1, issue2])
        session.commit()

        # 5. Add plays
        play1 = Play(game_id=game1.game_id, player_id=player1.player_id)
        play2 = Play(game_id=game2.game_id, player_id=player2.player_id)
        session.add_all([play1, play2])
        session.commit()

        session.close()
