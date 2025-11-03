from ducks import MallardDuck, SanAntonioDuck, RubberDuck, DecoyDuck
from behaviors import FlyWithWings, NoFly

def run_simulation(duck):
    """Executes all available behaviors for a given duck."""
    duck.display()
    duck.perform_fly()
    duck.perform_quack()
    duck.swim()
    
    # Check for the unique 'walk' method
    if isinstance(duck, SanAntonioDuck):
        duck.walk()
    print("-" * 30)

if __name__ == "__main__":
    mallard = MallardDuck()
    san_antonio = SanAntonioDuck()
    rubber = RubberDuck()
    decoy = DecoyDuck()

    # Run the initial simulation
    print("--- Initial Duck Simulation ---")
    run_simulation(mallard)
    run_simulation(san_antonio)
    run_simulation(rubber)
    run_simulation(decoy)

    # --- Demonstrate Strategy Pattern Power (Runtime Change) ---
    print("--- DEMO: Dynamic Strategy Change ---")
    print("San Antonio Duck's behavior is changed to NoFly at runtime.")
    
    # We can change the strategy object without touching the Duck's class!
    san_antonio.fly_behavior = NoFly()
    san_antonio.perform_fly() 
    
    print("-" * 30)