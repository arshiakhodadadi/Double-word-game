# Double-word-game
This Python script implements a two-player word chain game.

Game Rules:

Turn-Based Play: Two players take turns entering words.

Word Linking: Each new word must start with the last letter of the previous word.

No Repetition: Words cannot be repeated during the game.

Game Over Condition: If a player enters an invalid word (either not starting with the correct letter or already used), the game ends, and the number of successful rounds is displayed.

Code Breakdown:

Variables:

turn: Indicates the current player's turn (0 or 1).

round: Counts the number of successful rounds.

repeated_words: A list to track words that have already been used.

Game Loop:

The game runs indefinitely until a player makes an invalid move.

On each turn, the player is prompted to input a word.

The program checks if the word starts with the correct letter and hasn't been used before.

If valid, the word is added to repeated_words, and the game continues.

If invalid, the game ends, and the total number of successful rounds is displayed.

Example:

Player 1 enters: apple

Player 2 must enter a word starting with e, such as elephant

Player 1 then needs a word starting with t, like tiger

The game continues until a player makes an invalid move.
