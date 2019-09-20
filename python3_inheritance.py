class ArvSuper:
    def __init__(self, fnavn, enavn):
        self.fnavn = fnavn
        self.enavn = enavn

    def get_etternavn(self):
        return self.enavn

    def get_fornavn(self):
        return self.fnavn

    def to_string(self):
        return self.fnavn + " " + self.enavn


class ArvBarn(ArvSuper):
    # Litt nysgjerrig på kordan sette attributter som er unike for sub-klassen, og ikkje er i superklassen

    def to_string(self):
        return self.enavn + ", " + self.fnavn


class ArvBarn2(ArvSuper):
    def __init__(self, fnavn, enavn, tlf):
        # self.fnavn = fnavn
        # self.enavn = enavn
        super().__init__(fnavn, enavn)
        self.tlf = tlf

    def get_tlf(self):
        return self.tlf

    def to_string(self):
        return super().to_string() + ", tlf: " + str(self.tlf)


class ArvSuper2:
    def __init__(self, alder):
        self.alder = alder

    def get_alder(self):
        return self.alder


class ArvBarnAvTo(ArvSuper, ArvSuper2):
    def __init__(self, fnavn, enavn, alder, tlf):
        super().__init__(fnavn, enavn)
        # Seems like second super class must be define, super() seems to be just the first super class,
        ArvSuper2.__init__(self, alder)
        self.tlf = tlf

    def to_string(self):
        return super().to_string() + ", tlf: " + str(self.tlf) + ", alder: " + str(ArvSuper2.get_alder(self))


# Testing

# Standard subclass
test = ArvBarn("John", "Doe")
print(test.to_string())

# First superclass
testSuper = ArvSuper("Jane", "Doe")
print(testSuper.to_string())

# Second subclass, has uniqe methods
test2 = ArvBarn2("Jack", "Doe", 12345678)
print(test2.to_string())

# Third sub class. Has to super classes.
test_barn_av_to = ArvBarnAvTo("Jen", "Doe", 31, 23456789)
print(test_barn_av_to.to_string())
