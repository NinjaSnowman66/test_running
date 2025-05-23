from CMCed.production_cycle import ProductionCycle

working_memory = {'focusbuffer': {'state': 'bread1'}}


memories = {
    'working_memory': working_memory
}

ProceduralProductions = []

def bread1(memories):
    memories['working_memory']['focusbuffer']['state'] = 'cheese'
    print(f"bread bottom executed. Updated working_memory: {memories['working_memory']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'bread1'}}},
    'negations': {},
    'utility': 10,
    'action': bread1,
    'report': "bread1",
})

def swiss_cheese(memories):
    memories['working_memory']['focusbuffer']['state'] = 'ham'
    print(f"swiss cheese executed. Updated working_memory: {memories['working_memory']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'cheese'}}},
    'negations': {},
    'utility': 10,
    'action': swiss_cheese,
    'report': "swiss cheese",
})

def oka_cheese(memories):
    memories['working_memory']['focusbuffer']['state'] = 'ham'
    print(f"oka cheese executed. Updated working_memory: {memories['working_memory']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'cheese'}}},
    'negations': {},
    'utility': 10,
    'action': oka_cheese,
    'report': "oka cheese",
})

def feta_cheese(memories):
    memories['working_memory']['focusbuffer']['state'] = 'ham'
    print(f"feta cheese executed. Updated working_memory: {memories['working_memory']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'cheese'}}},
    'negations': {},
    'utility': 10,
    'action': feta_cheese,
    'report': "feta cheese",
})

def ham(memories):
    memories['working_memory']['focusbuffer']['state'] = 'bread2'
    print(f"ham executed. Updated working_memory: {memories['working_memory']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'ham'}}},
    'negations': {},
    'utility': 10,
    'action': ham,
    'report': "ham",
})

def bread2(memories):
    memories['working_memory']['focusbuffer']['state'] = 'done'
    print(f"bread top executed. Updated working_memory: {memories['working_memory']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'bread2'}}},
    'negations': {},
    'utility': 10,
    'action': bread2,
    'report': "bread2",
})

# Production system delays in ticks
ProductionSystem1_Countdown = 1

# Stores the number of cycles for a production system to fire and reset
DelayResetValues = {
    'ProductionSystem1': ProductionSystem1_Countdown}

# Dictionary of all production systems and delays
AllProductionSystems = {
    'ProductionSystem1': [ProceduralProductions, ProductionSystem1_Countdown]}

# Initialize ProductionCycle
ps = ProductionCycle()

# Run the cycle with custom parameters
ps.run_cycles(memories, AllProductionSystems, DelayResetValues, cycles=7, millisecpercycle=10)