### How to use the CSV files:

The data covers the scripts of seasons 1-10. Each season has its own CSV file and there is also a 'complete.csv' file with all season data if that is needed.

Example:

id,speaker,speech,context,raw-dialouge,season,episode,title,airdate,runtime
1051,Villain," Oh, no! The Raging Whirlpool! ",holds a baby's lollipop and he spots the whirlpool the whirlpool catches him and the lollipop falls on the baby's tongue,"[holds a baby's lollipop and he spots the whirlpool] Oh, no! The Raging Whirlpool! [the whirlpool catches him and the lollipop falls on the baby's tongue]",01,12,Mermaid Man and Barnacle Boy,21-Aug-99,10

Headers:

id = Unique ID number for that piece of dialouge. No order is encoded in this, just a unique number.

speaker = Who is saying this line of dialouge.

speech = The actual words spoken by this character, no context clues.

context = There are often braketed context clues embedded in the raw dialouge, this header stores just these context clues.

raw-dialouge = This is how the dialouge appears exactly as it is from the raw data source.

season = The season number.

episode = The episode number.

title = The title of the episode.

airdate = The date that the episode aired, format as dd-Mmm-YY.

runtime = The length of the episode in minutes.