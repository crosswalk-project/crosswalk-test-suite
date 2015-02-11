Feature: memory game
 Scenario: memory game launch checking
  When launch "memorygame"
   Then I should see title "Memory Game for Older Kids"
   And I press "pagebg"

   # check help
   And I should see "?" in 1 seconds
   And I press "main_help" 
   And I should see "Can you make it through level four" in 1 seconds 
   And I press "help_close"

   # check game level UI
   Then I should see "CHOOSE A LEVEL"
   And I press "selLevel_levelCard1"
   And I should see "LEVEL 1" in 3 seconds 
   And I press "l1c2"
   And I press "l1c3"

   # check back to home screen
   And I press "homebutton_backtomain"
   Then I should see "THE SPECTACULAR" in 2 seconds
   And I should see "MEMORY" 
   And I should see "EXTRAVAGANZA!" 

 Scenario: memory game play checking
  When launch "memorygame"
   Then I should see title "Memory Game for Older Kids"

   And I press "pagebg"
   And I press "selLevel_levelCard1"
   And I should see "LEVEL 1" in 3 seconds
   And I should see "GAME 1" in 3 seconds
   And I press "l1c1"

   # click the memory game card cyclically, to pass the "GAME 1" 
#   And I press "l1c" for 12 times cyclically
#   Then I should see "LEVEL 1" in 3 seconds

   # "GAME 1" pass and go into "GAME 2"!
#   And I wait 5 seconds
#   Then I should see "GAME 2"
