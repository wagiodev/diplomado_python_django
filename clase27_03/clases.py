class Address():
  def __init__(self, street=None, town=None, city=None):
    self.street = street
    self.town = town
    self.city = city
  
  def get_full_address(self):
    return '{} {} {}'.format(self.street, self.town, self.city)

class Persona():
  def __init__(self, first_name=None, last_name=None, age=None, id=None, address=None):  
      self.first_name = first_name  
      self.last_name = last_name  
      self.age = age  
      self.id = id  
      self.address = address

  def set_last_name(self, last_name):
      self.last_name = last_name  

  def saludar(cls):
    return 'Hola mi nombre es: {full_name}, tengo {age} años, y mi numero id es: {id}'.format(
        full_name='{} {}'.format(cls.first_name, cls.last_name),
        id=cls.id,
        age=cls.age,
    )

  def saludar_con_direccion(cls):
    inicio_saludo = cls.saludar()
    return inicio_saludo + ' mi direccion es: {}'.format(cls.address.get_full_address())


address = Address('calle 27', 'La Cumbre', 'Floridablanca')
walter = Persona(
    first_name='Walter',
    age='27',
    last_name='Cuadros', 
    id=1090090, 
    address=address
  )

print(walter.saludar_con_direccion())