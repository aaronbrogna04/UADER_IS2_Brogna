class TipoZombie:
    def __init__(self, nombre, modelo, animacion, velocidad, danio):
        self.nombre = nombre
        self.modelo = modelo
        self.animacion = animacion
        self.velocidad = velocidad
        self.danio = danio

    def mostrar(self, x, y, vida):
        print(f"[{self.nombre}] modelo: {self.modelo} | anim: {self.animacion} | "
              f"vel: {self.velocidad} | daño: {self.danio} | pos: ({x},{y}) | vida: {vida}")

class FabricaZombies:
    _tipos = {}

    @classmethod
    def obtener_tipo(cls, nombre, modelo, animacion, velocidad, danio):
        if nombre not in cls._tipos:
            cls._tipos[nombre] = TipoZombie(nombre, modelo, animacion, velocidad, danio)
            print(f"[Fábrica] Creando nuevo tipo de zombie: {nombre}")
        return cls._tipos[nombre]

    @classmethod
    def total_tipos(cls):
        return len(cls._tipos)


class Zombie:
    def __init__(self, x, y, vida, nombre, modelo, animacion, velocidad, danio):
        self.x = x
        self.y = y
        self.vida = vida
        self.tipo = FabricaZombies.obtener_tipo(nombre, modelo, animacion, velocidad, danio)

    def mostrar(self):
        self.tipo.mostrar(self.x, self.y, self.vida)

horda = []

horda.append(Zombie(10, 5,  100, "Zombie Normal",  "zombie_01.obj", "caminar_lento", 2, 10))
horda.append(Zombie(23, 8,   80, "Zombie Normal",  "zombie_01.obj", "caminar_lento", 2, 10))
horda.append(Zombie(5,  15,  90, "Zombie Normal",  "zombie_01.obj", "caminar_lento", 2, 10))
horda.append(Zombie(30, 2,  200, "Zombie Gordo",   "zombie_02.obj", "caminar_pesado", 1, 25))
horda.append(Zombie(12, 20, 180, "Zombie Gordo",   "zombie_02.obj", "caminar_pesado", 1, 25))
horda.append(Zombie(8,  10,  60, "Zombie Corredor","zombie_03.obj", "correr", 5, 15))
horda.append(Zombie(40, 5,   70, "Zombie Corredor","zombie_03.obj", "correr", 5, 15))
horda.append(Zombie(18, 18,  50, "Zombie Corredor","zombie_03.obj", "correr", 5, 15))

print("\n=== HORDA DE ZOMBIES ===")
for zombie in horda:
    zombie.mostrar()

print(f"\nZombies en pantalla: {len(horda)}")
print(f"Tipos distintos creados (flyweights): {FabricaZombies.total_tipos()}")
print("-> Cada tipo se creó una sola vez y se compartió entre todos los zombies del mismo tipo")