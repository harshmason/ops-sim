# Operations Simulation (Layer 1)

## Overview
This project is a **lightweight operations simulation** that models industrial assets (crushers, conveyors, trucks) and their impact on system throughput.  
Each asset can **fail, undergo repair, and recover**, and overall plant throughput is determined by **bottleneck constraints**.

The goal of this project is to explore **systems reliability, failure modeling, and operational throughput** concepts commonly encountered in industrial operations and DevOps-adjacent roles.

## System Model
The simulation models a simplified material flow pipeline:

Crusher → Conveyor → Truck Fleet → Output

- Assets operate in discrete time steps (minutes)
- Failures occur probabilistically based on a per-hour failure rate
- When an asset is down, it produces zero capacity
- System throughput is computed as:

throughput = min(crusher_capacity, conveyor_capacity, total_truck_capacity)

This intentionally models **single points of failure** and bottleneck behavior.

## Architecture

### assets.py
Defines the core simulation logic:
- Asset base class
- Failure modeling
- Repair countdown
- Runtime state management
- Crusher, Conveyor, Truck subclasses

### main.py
Acts as the simulation driver:
- Instantiates assets
- Advances time using a discrete simulation loop
- Computes and prints throughput at each step

## Running the Simulation
```bash
python main.py
