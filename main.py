from ducks import Mallard, San_Antonio, Rubber, Decoy
from behaviors import FlyWithWings, NoFly

def run_simulation(duck):
    """Executes all available behaviors for a given duck."""
    duck.display()
    duck.perform_fly()
    duck.perform_quack()
    duck.swim()
    
    # Check for the unique 'walk' method
    if isinstance(duck, San_Antonio):
        duck.walk()
    print("-" * 30)

if __name__ == "__main__":
    mallard = Mallard()
    san_antonio = San_Antonio()
    rubber = Rubber()
    decoy = Decoy()

    # Run the initial simulation
    print("--- Initial Duck Simulation ---")
    run_simulation(mallard)
    run_simulation(san_antonio)
    run_simulation(rubber)
    run_simulation(decoy)