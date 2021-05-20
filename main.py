# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, greeting='Hello, <name>!'):
    greeting = greeting.replace('<name>', name)
    print(greeting)
    return greeting

greet('Laura')

def force(mass, body='earth'):
    gravity={
        'sun':  274.0,
        'jupiter':  24.9,
        'neptune':  11.2,
        'saturn':  10.4,
        'earth':  9.8,
        'uranus':  8.9,
        'venus':  8.9,
        'mars':  3.7,
        'mercury':  3.7,
        'moon':  1.6,
        'pluto': 0.6
    }
    force = mass*gravity[body]
    print(force)
    return force

force(1200.33, 'pluto')

def pull(m1, m2, d):
    G =  6.674*10**-11
    pull = G*((m1*m2)/(d**2))
    print(pull)
    return pull

pull(800, 1500, 3)
