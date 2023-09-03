def single_matching(man: str, free_men: list, current_matching: list) -> None:
    # DO NOT MODIFY START
    # We start by looping through the preferences of the men to find a suitable woman
    for woman in m_pref[man]:
        match = []
        # We then check the return set to see if the current woman has any matches already made
        # If she does they are saved in match
        for pair in current_matching:
            if pair.woman == woman:
                match = pair
                break
    # DO NOT MODIFY END

    # Now let's cover the 2 cases:
    # TODO implement the following pseudocode:
    
        if match == []:
            new_pair = Pair(man, woman)
            current_matching.append(new_pair)
            free_men.remove(man)
            
    # if the woman is not in an engagement
        # create a new pair and append it to the return set
        # remove the man from the free list
        # break the loop
        
    # TODO implement the following pseudocode:
    
        if match == pair:
            if m_pref[woman].index(man) < m_pref[woman].index(match.man):
                free_men.remove(man)
                free_men.append(match.man)
                new_pair = Pair(man, woman)
                current_matching.append(new_pair)
                current_matching.remove(match)
                break
    # if the woman is in an engagement:
        # if the current man, is a lower priority then the proposing one:
            # remove the proposing man from the free list
            # add the current man to the free list
            # make a new pair and append them to the return set
            # remove the old pair from the return set
            # break the loop
