from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.space_station import SpaceStation


lilac = SpaceStation()
pesho = Biologist("Pesho")
simo = Meteorologist("Simo")
nina = Geodesist("Nina")
uran = Planet("Uranus")

print(lilac.add_astronaut("Biologist", "Pesho"))
print(lilac.add_astronaut("Meteorologist", "Simo"))
print(lilac.add_astronaut("Geodesist", "Bubo"))
print(lilac.add_astronaut("Meteorologist", "Sumo"))
print(lilac.add_astronaut("Biologist", "Petko"))
print(lilac.add_astronaut("Geodesist", "Goshko"))
print(lilac.add_astronaut("Meteorologist", "Sashko"))
print(lilac.add_astronaut("Biologist", "Pesho"))
print(lilac.add_planet("Uranus", "rocks, mud, more rocks, salt, water, bugs, beans, dogs, cats, lizards, water, sand, ash"))
print(lilac.add_planet("Uranus", "rocks, rocks, mud, more rocks, salt, water, bugs"))

lilac.retire_astronaut("Pesho")
lilac.retire_astronaut("Simo")
print(lilac.send_on_mission("Uranus"))
print(lilac.report())
