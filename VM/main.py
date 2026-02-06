from assets import Crusher, Conveyor, Truck

# Tester for now.. Will run sim 


crusher = Crusher(name="Crusher_1", failure_rate=0.08, repair_time=15, base_capacity=1200)
conveyor = Conveyor("Conveyor_1", 0.11, 10, 1000)
trucks = [Truck("Truck_1", 0.99, 5, 500), Truck("Truck_2", 0.99, 4, 500)]


SIM_TIME = 360 #mins
DT = 1 # mins per step

for t in range(0, SIM_TIME, DT):
    crusher.step(DT)
    conveyor.step(DT)
    for truck in trucks:
        truck.step(DT)

    crush_outp = crusher.get_output()
    conveyor_outp = conveyor.get_output()
    truck_outp = sum(t.get_output() for t in trucks)

    throughput = min(crush_outp, conveyor_outp, truck_outp)

    print(f"t={t:03d} | "f"Crusher={crusher.status:<7} | "f"Conveyor={conveyor.status:<7} | "f"Trucks={truck_outp:4.0f} | "f"Throughput={throughput:4.0f}")

