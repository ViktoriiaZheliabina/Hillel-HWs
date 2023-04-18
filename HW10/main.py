# ДЗ 10. OOP principals: Abstaraction, Inheritance and Hiding.
# Потрібно описати будь-який транспортний засіб або
# гаджет(на вибір) , з кількома рівнями абстракції, використовуючи ті принципи ООП, що ми розглядали:
# наслідування абстракцію і приховування даних

from HW10.transport.liner import Liner
from HW10.transport.tanker import Tanker

if __name__ == '__main__':
    KnockNevis = Tanker("Knock Nevis", 564763, 8)
    KnockNevis.clean_tanks()
    KnockNevis.docking(14582.25)
    KnockNevis.docking(-2456.33)
    KnockNevis.docking(8854.6)
    print(f"{KnockNevis.get_type()} \"{KnockNevis.name}\" cargo: {KnockNevis.get_cargo()} tons")

    QueenMary2 = Liner("Queen Mary 2", 3090, 2)
    QueenMary2.book(254)
    QueenMary2.book(1065)
    QueenMary2.start_cruise(["London", "Barcelona", "Stambul", "Odessa"])
    print(f"{QueenMary2.get_type()} \"{QueenMary2.name}\" passengers: {QueenMary2.get_passengers()}")
