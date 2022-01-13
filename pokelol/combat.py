

def getexp(self,deckally,deckennemy):
    """
        function used to calculte the new level of experience of the pokemons of a deck.
        Parameters
        ---------
        deckally: List of dictionaries of the pokemon gaining exp
        deckennemy: List of dictionaries used to calculate the exp gain

        Return
        ---------
        int
            The experience each pokemon of the deck are gaining
    """
    for i in range (len(deckally)):
        niv=0
        for j in range(len(deckennemy)):
            niv=niv+deckennemy[j]["Niveau"]
        exp=10+niv/len(deckennemy)-deckally[i]["Niveau"]
        return exp



def getdefence(self,pokemon,pokeinit,competence):
    """
        function used when a pokemon use a defensive competence: can gain hp or energy.
        Parameters
        -----------
        Pokemon: Dictionary of the pokemon using the competence (from deck)
        Pokeinit: Initial Dictionary of the pokemon using the competence
        Competence: Dictionary of the competence used by the pokemon.

        Return:
        --------------
        int
            Return the hp healed or the energy given back by the competence

    Deux compétences de régénération d'énergie
    """
    import random
    if competence["Soin"]=="":
        resinf, ressup = int(competence["Energie"][0:2]), int(competence["Energie"][3:5])
        val=random.randint(resinf,ressup)*pokeinit["Vie"]
        pokemon["Energie"]+=val
    else:
        resinf,ressup=int(competence["Soin"][0:2]),int(competence["Soin"][3:5])
        val = random.randint(resinf, ressup)*pokeinit["Vie"]
        pokemon["Vie"] += val






def getdamage(self,pokeatt,pokedef,competence):
    """
        function used to calculate the damage inflicted to a pokemon
        Parameters
        ----------
        pokeatt: Dictionary of the pokemon using the attack.
        pokedef: Dictionary of the pokemon undergoing the attack.
        attack: Dictionary of the attack used by the pokemon.

        Returns
        -------
        int
            Returns an integer corresponding of the damage inflicted.
        """
    import random
    self.pokeatt=pokeatt
    self.pokedef=pokedef
    self.attack=competence
    print(self.pokeatt["Nom"],"utilise",self.attack["Nom"])

    if random.randint(0,100)<=self.attack["Precision"]:

        Matrixelem=[[1,1,0.5,1.5],[1.5,1,1,0.5],[0.5,1.5,1,1],[1,0.5,1.5,1]]
        elem={"Air":0,"Eau":1,"Feu":2,"Terre":3}
        elemcomp=elem[self.attack["Element"]]
        elemdef=elem[self.pokedef["Element"]]
        beta=Matrixelem[elemdef][elemcomp]
        na=int(self.pokeatt["Niveau"])
        resdef=int(self.pokedef["Resistance"])
        p=int(self.attack["Puissance"])
        cm=beta*random.uniform(0.85,1)
        dmg=int(cm*((p*(4*na+2))/resdef+2))
        return dmg
    else:
        return "L'attaque a échouée."

def calculcapture(self,pokeorig,pokecapt,deck):
    """
    function used to add a new pokemon to the deck depending of the catch rate.
    Can't be used if the hp of the pokemon are over 20%.


    Parameters

    ------------

    pokeorig: Dictionary original of the pokemon tried to be captured, used to recover the Hp max
    pokecapt: Current dictionary of the pokemon tried to be captured, used to recover the current Hp
    deck: Deck of the player trying to capture the pokemon

    Return
    -----------
    A sentence indicating whether the pokemon is captured or not
    List
        the list of the deck after the capture attempt.
    """
    V=int(pokecapt["Vie"])
    Vmax=int(pokeorig["Vie"])
    self.pokedef=pokedef
    self.deck=deck

    import random
    #Possibilité d'ajouter une fonction pokeball pour augmenter les chances de réussir
    proba=4*(0.2-V/Vmax)
    rand=random.random()
    if random<=proba:
        self.deck.append(self.pokedef)
        return "Pokemon capturé!"
    else:
        return "Echec de la capture"

def combatia(self):
    pass