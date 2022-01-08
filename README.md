# PyPoll with Python

## Overview of Election Audit

We were tasked with assisting Tom, a Colorado Board of Elections employee, in conducting an election audit in one of Colorado's congressional precincts.  We were provided with a massive CSV file containing the hundreds of thousands of datapoints of ballots containing ballot ID, county, and the name of the candidate the vote is for.  In order to handle this mass of information, we used Python to write code that would automate the counting of votes in addition to providing information on the breakdown of voting by county.  This was able to calculate and display how many total votes were cast, how many votes came from each county (including which county had the largest turnout), the vote total and percentage of each candidate, and who the grand winner turned out to be.

## Election Audit Results

![Election Results](https://github.com/Jeffstr00/Election_Analysis/blob/main/resources/election_summary.png)

* In this election, 369,711 total votes were cast in this precinct.  To tabulate this, we used a simple `total_votes = total_votes + 1` formula inside of a for loop that ran through each row of the data.
* To break this down by county, Jefferson produced 38,855 (10.5%) votes, Denver had 306,055 (82.8%), and Arapahoe yielded 24,801 (6.7%) ballots.  To come up with the number of votes by county, when we ran through each row, we used `counties_dict[county_name] += 1` to add a count in the specified county in a dictionary.  Percentages were calculated using the following formula: `county_percentage = float(county_votes) / float(total_votes) * 100`.
* Denver unsurprisingly had what was easily the highest total voter turnout in the precinct.  Its 306,055 voters were 82.8% of the nearly 370 thousand total.  In order to determine this, we used the following code: `if county_votes >= county_turnout: county_turnout = county_votes county_largest = county_name`.  This checked to see if the number of votes from the current county was greater than that of the previous high.  If so, it established a new high vote count and name of the given county.  If not, it was ignored.
* As for the voting results, Charles Casper Stockham received 85,213 (23.0%) votes, Diana DeGette led the way with 272,892 (73.8%), and Raymon Anthony Doane must have been the Libertarian candidate with only 11,606 (3.1%) votes.  `candidate_votes[candidate_name] += 1` kept track of the vote totals and put them into a dictionary of candidates.  Once we had the totals, the percentages were found using `vote_percentage = float(votes) / float(total_votes) * 100`.
* The clear winner of the election was Diana DeGette.  She received 272,892 votes, which was 73.8% of the total.  In order to determine this, we ran through each candidate and looked at their votes and vote percentage (although looking at just one of those two would produce the same results).  If their votes and voting percentage was higher than that of the previous, we updated things to show the new winner and their respective vote count/percentage.  The code looked like this: `if (votes > winning_count) and (vote_percentage > winning_percentage): winning_count = votes winning_candidate = candidate_name winning_percentage = vote_percentage`.

## Election Audit Summary

