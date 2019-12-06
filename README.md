# TCA Dungeon Crawler (Coding 1)

## Goal

You are an adventurer who has fallen into a long-abandoned dungeon. Whoops! You have to get out somehow, and the only way to do that is by traveling through it and finding an exit.

We will be building this game together, but the final product will be yours, so feel free to change any of the code, text, or colors to your heart's content. That said there are 4 requirements to consider your project complete.

### Requirements

1. You MUST be able to navigate through the dungeon and win the game when you reach the exit.
2. You MUST be able to encounter random monsters throughout the dungeon who will try to defeat you before you make it to the exit. You will need to be able to combat those monsters.
3. You MUST be able to find items (weapons and loot) on the dungeon floor as you travel about.
4. You MUST add a feature (or game mechanic) to the game that is not listed above. We will brainstorm ideas in class and those ideas will be added here.

## Getting Started

To start, download the code using your commandline or Terminal. 

> Anytime you see documentation for your commandline, you should copy and paste everything after the dollar sign ($).

```
$ git clone https://github.com/tca-code/dungeon-crawler.git
```

```
$ cd dungeon-crawler
```

Next you are going to make a special "branch" that belongs to you for you to work on your game. We won't dive much into this, but for now the easiest way to make this happen is to copy the following:

```
$ git checkout -b feature/<your-name> origin/master
```

Boom! You did it. You should now have all the code you need to get started. Now before you run the game for the first time, we're going to be working on this code together. I have code that I will be adding each Thursday evening until the end of the semester. This is to get you used to interacting with doing coding as a team. In order to get this code, you'll run the following:

```
$ git pull origin master
```

Don't worry too much about that last part since we'll be doing that in class together each week.

Now that you have everything, let's run the code:

```
$ python3 main.py
```

## Features 

### Feature 1 (Navigation)

#### Background

The dungeon is a 45x45 square grid with a wall around it. So rows 0 and 44 (the last row) are walls, and columns 0 and 44 (the last column) are walls.
In addition, there are random obstacles placed inside dungeon that each occupy a single square.

The player is placed somewhere in the last playable row (row 43) on a random column. The exit is placed somewhere on the first playable row (row 1) on a random column.

The player's goal is to reach the exit.

#### Rules
1. The player can move `up`, `down`, `left`, and `right` and can do so by typing those commands when prompted.
2. If you encounter a wall or an obstacle, the player cannot move into the square the wall or obstacle occupies. The player should also be notified that that square is a wall or obstacle.
3. If the player enters the square that has the exit, the game should end, the player is victorious.
