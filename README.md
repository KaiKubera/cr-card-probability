# Clash Royale Card Probabilities

This tool allows you to pick any card from Clash Royale and get some neat statistics in return; namely, it shows what cards often go along with your choice. 
That is - what is the probability of such and such a card to be present in a deck with the card of your choice?



# Notes

This tool doesn't take into account Tower Troops. It also fully relies on me manually updating deck statistics for each new season each month to account for the ever-changing meta. In theory, this process could be automated with a clever algorithm, but I'm not paid enough to do this. In fact, I'm not paid at all to do this. But having said that -- have fun using this!

## Some technical details

The decks used to calculate the probabilities were taken from Battle Logs of Top-10,000 players of the March 2024 Season (Season 96 internally) in Clash Royale. That means 25 battles for each of those players, with two decks taken from each battle. This resulted in the collection of 390,026 unique decks.
