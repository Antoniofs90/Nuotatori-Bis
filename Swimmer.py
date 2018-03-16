from datetime import datetime

class Year(object):
    def __init__(self,year1,year2):
        self.year1 = year1
        self.year2 = year2

    def __str__(self):
        return "{}-{}".format(self.year1, self.year2)

    def __add__(self, other):
        self.year1 += other
        self.year2 += other
        return self

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        self.year1 -= other
        self.year2 -= other
        return self

    def __rsub__(self, other):
        return self - other

    def __eq__(self, other):
        return self.year1 == other.year1 and self.year2 == other.year2

    def __ne__(self, other):
        return self.year1 != other.year1 or self.year2 != other.year2


    def __hash__(self):
        return self.year1 + self.year2




class Swimmer(object):
    def __init__(self):
        self.name = None #get_name(url)
        self.year = None #get_class(url)
        self.times_date = None #get_times_date(url)
        self.years_of_partecipation = set() # set
        self.ratio = None
        self.locality = None #get_locality(url)

    def __str__(self):
        return "Name: {} Class: {} Ratio: {}".format(self.name, self.year,self.ratio)

    def fill_partecipation(self):
        for d in self.times_date:
            #self.years_of_partecipation.add(datetime.strptime(d[1], "%d/%m/%Y"))
            self.years_of_partecipation.add(self.get_partecipation_year(d))

    @staticmethod
    def get_partecipation_year(d):
        """prende in input una data formattata "%d/%m/%Y" e decide a che anno di partecipazione"""
        date = datetime.strptime(d[1], "%d/%m/%Y")
        if date.month >= 10:
            return Year(date.year, date.year + 1)
        else:
            return Year(date.year - 1, date.year)

    def calc_ratio(self, starting_year=Year(2000, 2001), ending_year=Year(2016, 2017)):
        partecipation_years = set()
        for year in range(starting_year.year1, ending_year.year2):
            y = Year(year, year + 1)
            if y in self.years_of_partecipation:
                #print(y)
                partecipation_years.add(y)
                #print(partecipation_years)


        self.ratio = len(partecipation_years)/(ending_year.year1 - starting_year.year1)


if __name__ == "__main__":
    print(Swimmer.get_partecipation_year((None, "1/10/2016")))


