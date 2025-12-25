from flask import Flask, render_template, jsonify, request
from games.tower_of_hanoi import TowerOfHanoi
from games.tic_tac_toe import TicTacToe
from games.eight_puzzle import EightPuzzle
from games.water_jug import WaterJug

# New games import placeholders:
from games.sudoku import Sudoku
from games.fifteen_puzzle import FifteenPuzzle
from games.minesweeper import Minesweeper
from games.connect_four import ConnectFour

app = Flask(__name__)

# Game globals
hanoi_game = None
ttt_game = None
eight_game = None
water_game = None
sudoku_game = None
fifteen_game = None
minesweeper_game = None
connect4_game = None

@app.route('/')
def home():
    return render_template('index.html')

# ---------- TOWER OF HANOI ----------
@app.route('/hanoi')
def hanoi_page():
    return render_template('hanoi.html')

@app.route('/hanoi/start/<int:num_disks>')
def hanoi_start(num_disks):
    global hanoi_game
    hanoi_game = TowerOfHanoi(num_disks)
    return jsonify({"message": f"Game started with {num_disks} disks.", "state": hanoi_game.get_state()})

@app.route('/hanoi/move', methods=['POST'])
def hanoi_move():
    global hanoi_game
    if hanoi_game is None:
        return jsonify({"error": "No game started"}), 400
    data = request.json
    from_peg = data.get("from")
    to_peg = data.get("to")
    success, message = hanoi_game.move_disk(from_peg, to_peg)
    return jsonify({"success": success, "message": message, "state": hanoi_game.get_state(), "solved": hanoi_game.is_solved()})

# ---------- TIC-TAC-TOE ----------
@app.route('/tic')
def tic_page():
    return render_template('tic.html')

@app.route('/tic/start')
def tic_start():
    global ttt_game
    ttt_game = TicTacToe()
    return jsonify({"message": "New game started.", "state": ttt_game.get_state()})

@app.route('/tic/move', methods=['POST'])
def tic_move():
    global ttt_game
    if ttt_game is None:
        return jsonify({"error": "No game started"}), 400
    data = request.json
    pos = int(data.get("pos"))
    success, message = ttt_game.make_move(pos)
    return jsonify({
        "success": success,
        "message": message,
        "state": ttt_game.get_state()
    })

# ---------- 8-PUZZLE ----------
@app.route('/eight')
def eight_page():
    return render_template('eight.html')

@app.route('/eight/start')
def eight_start():
    global eight_game
    eight_game = EightPuzzle()
    return jsonify({"message": "New puzzle started.", "state": eight_game.get_state()})

@app.route('/eight/move', methods=['POST'])
def eight_move():
    global eight_game
    if eight_game is None:
        return jsonify({"error": "No puzzle started"}), 400
    data = request.json
    r = int(data.get("r"))
    c = int(data.get("c"))
    success, message = eight_game.move(r, c)
    return jsonify({
        "success": success,
        "message": message,
        "state": eight_game.get_state()
    })

# ---------- WATER JUG ----------
@app.route('/water')
def water_page():
    return render_template('water.html')

@app.route('/water/start')
def water_start():
    global water_game
    water_game = WaterJug()
    return jsonify({"message": "New game started.", "state": water_game.get_state()})

@app.route('/water/action', methods=['POST'])
def water_action():
    global water_game
    if water_game is None:
        return jsonify({"error": "No game started"}), 400
    data = request.json
    act = data.get("act")
    idx = data.get("idx")
    success, message = False, "Invalid action."
    if act in ("fill", "empty"):
        success, message = water_game.action(act, int(idx))
    elif act == "pour":
        success, message = water_game.action(act, [int(x) for x in idx])
    return jsonify({
        "success": success,
        "message": message,
        "state": water_game.get_state()
    })

# ---------- SUDOKU ----------
@app.route('/sudoku')
def sudoku_page():
    return render_template('sudoku.html')

@app.route('/sudoku/start')
def sudoku_start():
    global sudoku_game
    sudoku_game = Sudoku()
    return jsonify({"message": "New puzzle generated.", "state": sudoku_game.get_state()})

@app.route('/sudoku/move', methods=['POST'])
def sudoku_move():
    global sudoku_game
    if sudoku_game is None:
        return jsonify({"error": "No puzzle started"}), 400
    data = request.json
    r = int(data.get("r"))
    c = int(data.get("c"))
    num = int(data.get("num"))
    success, message = sudoku_game.move(r, c, num)
    return jsonify({
        "success": success,
        "message": message,
        "state": sudoku_game.get_state()
    })

# ---------- SLIDING 15-PUZZLE ----------
@app.route('/fifteen')
def fifteen_page():
    return render_template('fifteen.html')

@app.route('/fifteen/start')
def fifteen_start():
    global fifteen_game
    fifteen_game = FifteenPuzzle()
    return jsonify({"message": "New puzzle started.", "state": fifteen_game.get_state()})

@app.route('/fifteen/move', methods=['POST'])
def fifteen_move():
    global fifteen_game
    if fifteen_game is None:
        return jsonify({"error": "No puzzle started"}), 400
    data = request.json
    r = int(data.get("r"))
    c = int(data.get("c"))
    success, message = fifteen_game.move(r, c)
    return jsonify({
        "success": success,
        "message": message,
        "state": fifteen_game.get_state()
    })

# ---------- MINESWEEPER ----------
@app.route('/minesweeper')
def minesweeper_page():
    return render_template('minesweeper.html')

@app.route('/minesweeper/start')
def minesweeper_start():
    global minesweeper_game
    minesweeper_game = Minesweeper()
    return jsonify({"message": "New game started.", "state": minesweeper_game.get_state()})

@app.route('/minesweeper/click', methods=['POST'])
def minesweeper_click():
    global minesweeper_game
    if minesweeper_game is None:
        return jsonify({"error": "No game started"}), 400
    data = request.json
    r = int(data.get("r"))
    c = int(data.get("c"))
    button = data.get("button")
    success, message = minesweeper_game.click(r, c, button)
    return jsonify({
        "success": success,
        "message": message,
        "state": minesweeper_game.get_state()
    })

# ---------- CONNECT FOUR ----------
@app.route('/connect4')
def connect4_page():
    return render_template('connect4.html')

@app.route('/connect4/start')
def connect4_start():
    global connect4_game
    connect4_game = ConnectFour()
    return jsonify({"message": "New game started.", "state": connect4_game.get_state()})

@app.route('/connect4/move', methods=['POST'])
def connect4_move():
    global connect4_game
    if connect4_game is None:
        return jsonify({"error": "No game started"}), 400
    data = request.json
    col = int(data.get("col"))
    success, message = connect4_game.move(col)
    return jsonify({
        "success": success,
        "message": message,
        "state": connect4_game.get_state()
    })

if __name__ == '__main__':
    app.run(debug=True)
