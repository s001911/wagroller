# Wagroller

Wagroller (Wrath & Glory Roller) is a basic command line dice roller for use with the (as of writing) upcoming game [Wrath & Glory](http://www.ulisses-us.com/games/warhammer-40000-roleplay/ "Wrath & Glory").

For a more indepth look at the rules here is the Designer Diary by the publisher that I based this off of: [Wrath & Glory Designer Diary – November 2017](http://www.ulisses-us.com/wrath-glory-designer-diary-november-2017/ "Wrath & Glory Designer Diary – November 2017")

## Usage

    positional arguments:
      n           Amount of Dice to be rolled

    optional arguments:
      -h, --help  show this help message and exit
      -d D        Difficulty Number, defaults to 3
      -r          Show Dice Rolls

### Basic usage
`python wagroller.py 5` where 5 is the nember of dice in your pool. It defaults to a "difficulty number" of 3 which is  what the designers have set as the base test.

## Sample Outcome


### Override Difficulty Number
This can be overridden by using the `-d` command with the new difficulty class, eg `python wagroller.py 5 -d 4`

### Show Actual Dice Rolls
This can be done by appending `-r` to any command. The dice which is used to determine the Wrath or Glory outcome will have an asterix next to it.

## Example Outcome

    $ python wagroller.py 5 -r
    Rolls: 3*, 6, 1, 6, 5
    Wrath or Glory: Neither
    Complications: 1
    Icons: 1
    Exalted Icons: 2
    Total Icons/Passes: 5
    Passed: True

In this example we've used a pool of 5 dice passed the `-r` flag to show the rolls.
We can see that the first roll, `3*` was used to test for Wrath or Glory resulting in `Neither` as the first outcome. There is 1 "Complication" due to 1 being rolled as the 3rd roll. 1 "Icon" from the last roll of 5, 2 "Exalted Icons" from both 6's giving us a total of 5 "Icons" resulting in a pass as 5 is greater than our default difficulty number of 3.

#### Disclaimer
All product and company names are trademarks™ or registered® trademarks of their respective holders. Use of them does not imply any affiliation with or endorsement by them.
