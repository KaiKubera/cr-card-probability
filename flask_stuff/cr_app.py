from flask import Flask, render_template, request

app = Flask(__name__)

cards = sorted(['Knight', 'Archers', 'Goblins', 'Giant', 'P.E.K.K.A', 'Minions', 'Balloon', 'Witch', 'Barbarians', 'Golem', 'Skeletons', 'Valkyrie', 'Skeleton Army', 'Bomber', 'Musketeer', 'Baby Dragon', 'Prince', 'Wizard', 'Mini P.E.K.K.A', 'Spear Goblins', 'Giant Skeleton', 'Hog Rider', 'Minion Horde', 'Ice Wizard', 'Royal Giant', 'Guards', 'Princess', 'Dark Prince', 'Three Musketeers', 'Lava Hound', 'Ice Spirit', 'Fire Spirit', 'Miner', 'Sparky', 'Bowler', 'Lumberjack', 'Battle Ram', 'Inferno Dragon', 'Ice Golem', 'Mega Minion', 'Dart Goblin', 'Goblin Gang', 'Electro Wizard', 'Elite Barbarians', 'Hunter', 'Executioner', 'Bandit', 'Royal Recruits', 'Night Witch', 'Bats', 'Royal Ghost', 'Ram Rider', 'Zappies', 'Rascals', 'Cannon Cart', 'Mega Knight', 'Skeleton Barrel', 'Flying Machine', 'Wall Breakers', 'Royal Hogs', 'Goblin Giant', 'Fisherman', 'Magic Archer', 'Electro Dragon', 'Firecracker', 'Mighty Miner', 'Elixir Golem', 'Battle Healer', 'Skeleton King', 'Archer Queen', 'Golden Knight', 'Monk', 'Skeleton Dragons', 'Mother Witch', 'Electro Spirit', 'Electro Giant', 'Phoenix', 'Little Prince', 'Cannon', 'Goblin Hut', 'Mortar', 'Inferno Tower', 'Bomb Tower', 'Barbarian Hut', 'Tesla', 'Elixir Collector', 'X-Bow', 'Tombstone', 'Furnace', 'Goblin Cage', 'Goblin Drill', 'Fireball', 'Arrows', 'Rage', 'Rocket', 'Goblin Barrel', 'Freeze', 'Mirror', 'Lightning', 'Zap', 'Poison', 'Graveyard', 'The Log', 'Tornado', 'Clone', 'Earthquake', 'Barbarian Barrel', 'Heal Spirit', 'Giant Snowball', 'Royal Delivery'])


@app.route('/')
def hello():
    return render_template('index.html', cards=cards)


@app.route('/card-probs')
def card_probs():
    card = request.args.get('card')
    card_img = f"static/card_icons/{card}.png"
    barchart_img = f"static/barcharts/barchart_{card}.png"

    return render_template('card-probs.html',
                           card_img=card_img,
                           barchart_img=barchart_img,
                           cards=cards)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
