# interacting with the environment using a basic CMC approach

# this model has a basic CMC architecture
# the motor module carries out motor commands from the motor_buffer in working memory
# the visual module scans the environment and updates the visual_representation_buffer in working memory

# in this model the delay for motor actions is provided by putting the delay in the motor_buffer
# this is not realistic but without a detailed motor?environment model the delays must be provided


from CMCed.production_cycle import ProductionCycle
import copy

# -------------------------
# Initialize Memories
# -------------------------
working_memory = {
    'focusbuffer': {'state': 'underwear1'},
    'motor_buffer': {'state': 'no_action'},  # Initially, no motor action is scheduled.
    'visual_representation_buffer': {
        'underwear1': {'location': 'equipped'},
        'underwear2': {'location': 'desk'},
        'shirt': {'location': 'desk'},
        'pants': {'location': 'desk'},
        'sock1': {'location': 'desk'},
        'sock2': {'location': 'desk'}},
        
    'visual_command_buffer': {'state': 'scan'}  # Command to continuously scan the environment.
}
environment = {
    'underwear1': {'location': 'equipped'},
    'underwear2': {'location': 'desk'},
    'shirt': {'location': 'desk'},
    'pants': {'location': 'desk'},
    'sock1': {'location': 'desk'},
    'sock2': {'location': 'desk'}
}
memories = {
    'working_memory': working_memory,
    'environment': environment  # Motor productions still update the actual environment.
}

# -------------------------
# Define Procedural Productions (Sandwich Steps)
# These productions match on the visual_representation_buffer directly.
# -------------------------
ProceduralProductions = []

#So I'll try moving underwear1 to hamper first if it don't work I'll try drawers I guess

###visual_representation_buffer': {'underwear1': {'location': 'hamper'},
###                                            'underwear2': {'location': 'equipped'},
###                                            'shirt': {'location': 'desk'},
###                                            'pants': {'location': 'desk'},
###                                            'sock1': {'location': 'desk'},
###                                            'sock2': {'location': 'desk'}}}},
###


def underwear1(memories):
    motorbuffer = memories['working_memory']['motor_buffer']
    motorbuffer.update({
        'state': 'do_action',
        'env_object': 'underwear1',
        'slot': 'location',
        'newslotvalue': 'hamper',
        'delay': 4
    })
    memories['working_memory']['focusbuffer']['state'] = 'underwear2'
    print("underwear1 production executed: focus updated to 'underwear2'; motor action scheduled for underwear1 (I am throwing it in the hamper)")

ProceduralProductions.append({
    'matches': {
        'working_memory': {
             'focusbuffer': {'state': 'underwear1'},
             'visual_representation_buffer': {'underwear1': {'location': 'equipped'}}}},
    'negations': {},
    'utility': 10,
    'action': underwear1,
    'report': "underwear1",
})

def underwear2(memories):
    motorbuffer = memories['working_memory']['motor_buffer']
    motorbuffer.update({
        'state': 'do_action',
        'env_object': 'underwear2',
        'slot': 'location',
        'newslotvalue': 'equipped',
        'delay': 4
    })
    memories['working_memory']['focusbuffer']['state'] = 'shirt'
    print("underwear2 production executed: focus updated to 'shirt'; motor action scheduled for underwear2. (putting it on)")

ProceduralProductions.append({
    'matches': {
        'working_memory':
            {'focusbuffer': {'state': 'underwear2'},
            'visual_representation_buffer': {'underwear1': {'location': 'hamper'},
                                             'underwear2': {'location': 'desk'}}}},
    'negations': {},
    'utility': 10,
    'action': underwear2,
    'report': "underwear2",
})


# -------------------------
def shirt(memories):
    motorbuffer = memories['working_memory']['motor_buffer']
    motorbuffer.update({
        'state': 'do_action',
        'env_object': 'shirt',
        'slot': 'location',
        'newslotvalue': 'equipped',
        'delay': 4
    })
    memories['working_memory']['focusbuffer']['state'] = 'pants'
    print("shirt production executed: focus updated to 'pants'; motor action scheduled for shirt.")

ProceduralProductions.append({
    'matches': {
        'working_memory': {'focusbuffer': {'state': 'shirt'},
            'visual_representation_buffer': {'underwear1': {'location': 'hamper'},
                                             'underwear2': {'location': 'equipped'},
                                             'shirt': {'location': 'desk'}}}},
    'negations': {},
    'utility': 10,
    'action': shirt,
    'report': "shirt",
})

# -------------------------

def pants(memories):
    motorbuffer = memories['working_memory']['motor_buffer']
    motorbuffer.update({
        'state': 'do_action',
        'env_object': 'pants',
        'slot': 'location',
        'newslotvalue': 'equipped',
        'delay': 4
    })
    memories['working_memory']['focusbuffer']['state'] = 'sock1'
    print("pants production executed: focus updated to 'sock1'; motor action scheduled for pants.")

ProceduralProductions.append({
    'matches': {
        'working_memory': {'focusbuffer': {'state': 'pants'},
        'visual_representation_buffer': {'underwear1': {'location': 'hamper'},
                                         'underwear2': {'location': 'equipped'},
                                         'shirt': {'location': 'equipped'},
                                         'pants': {'location': 'desk'}}}},
    'negations': {},
    'utility': 10,
    'action': pants,
    'report': "pants",
})

def sock1(memories):
    motorbuffer = memories['working_memory']['motor_buffer']
    motorbuffer.update({
        'state': 'do_action',
        'env_object': 'sock1',
        'slot': 'location',
        'newslotvalue': 'equipped',
        'delay': 4
    })
    memories['working_memory']['focusbuffer']['state'] = 'sock2'
    print("sock1 production executed: focus updated to 'sock2'; motor action scheduled for sock1.")

ProceduralProductions.append({
    'matches': {
        'working_memory': {'focusbuffer': {'state': 'sock1'},
        'visual_representation_buffer': {'underwear1': {'location': 'hamper'},
                                         'underwear2': {'location': 'equipped'},
                                         'shirt': {'location': 'equipped'},
                                         'pants': {'location': 'equipped'},
                                         'sock1': {'location': 'desk'}}}},
    'negations': {},
    'utility': 10,
    'action': sock1,
    'report': "sock1",
})


def sock2(memories):
    motorbuffer = memories['working_memory']['motor_buffer']
    motorbuffer.update({
        'state': 'do_action',
        'env_object': 'sock2',
        'slot': 'location',
        'newslotvalue': 'equipped',
        'delay': 4
    })
    memories['working_memory']['focusbuffer']['state'] = 'done'
    print("sock2 production executed: focus updated to 'done'; motor action scheduled for sock2.")

ProceduralProductions.append({
    'matches': {
        'working_memory': {'focusbuffer': {'state': 'sock2'},
        'visual_representation_buffer': {'underwear1': {'location': 'hamper'},
                                         'underwear2': {'location': 'equipped'},
                                         'shirt': {'location': 'equipped'},
                                         'pants': {'location': 'equipped'},
                                         'sock1': {'location': 'equipped'},
                                         'sock2': {'location': 'desk'}}}},
    'negations': {},
    'utility': 10,
    'action': sock2,
    'report': "sock2",
})
# -------------------------

def finished_dressing(memories):
    print("Dressed and ready to go (male, I'm sure female dressing is more complicated)")

ProceduralProductions.append({
    'matches': {
        'working_memory': {'focusbuffer': {'state': 'done'}}
    },
    'negations': {},
    'utility': 10,
    'action': finished_dressing,
    'report': "finished_dressing",
})
# -------------------------



# -------------------------
# Define Motor Productions (Generic Motor)
# -------------------------
MotorProductions = []

def move_item(memories):
    motorbuffer = memories['working_memory']['motor_buffer']
    env_object = motorbuffer['env_object']
    slot = motorbuffer['slot']
    newslotvalue = motorbuffer['newslotvalue']
    delay = motorbuffer['delay']

    memories['working_memory']['motor_buffer']['state'] = 'moving'
    print(f"move_item production executed: moving {env_object} to {newslotvalue}.")
    print(f"Motor action scheduled to complete in {delay} cycles.")
    return delay

def motor_delayed_action(memories):
    motorbuffer = memories['working_memory']['motor_buffer']
    env_object = motorbuffer['env_object']
    slot = motorbuffer['slot']
    newslotvalue = motorbuffer['newslotvalue']
    # Update the environment once the delay has passed.
    memories['environment'][env_object][slot] = newslotvalue
    memories['working_memory']['motor_buffer']['state'] = 'no_action'
    print(f"motor_delayed_action executed: {env_object} moved to {newslotvalue}.")

MotorProductions.append({
    'matches': {
        'working_memory': {'motor_buffer': {'state': 'do_action'}}
    },
    'negations': {},
    'utility': 10,
    'action': move_item,
    'report': "move_item",
    'delayed_action': motor_delayed_action,
})
# -------------------------



# -------------------------
# Define Visual Productions (Vision)
# -------------------------
VisualProductions = []

def scan_environment(memories):
    # Copy the entire environment into the visual representation buffer.
    # Now the visual representation is structured the same as the environment.
    memories['working_memory']['visual_representation_buffer'] = copy.deepcopy(memories['environment'])
    print("scan_environment production executed: visual_representation_buffer updated.")
    return 2  # Delay of 1 cycle (adjust as needed).

VisualProductions.append({
    'matches': {
        'working_memory': {'visual_command_buffer': {'state': 'scan'}}
    },
    'negations': {},
    'utility': 10,
    'action': scan_environment,
    'report': "scan_environment",
})
# -------------------------



# -------------------------
# Production Systems Setup
# -------------------------
ProductionSystem1_Countdown = 1  # For procedural productions.
ProductionSystem2_Countdown = 1  # For motor productions.
ProductionSystem3_Countdown = 1  # For visual productions (vision system).

DelayResetValues = {
    'ProductionSystem1': ProductionSystem1_Countdown,
    'ProductionSystem2': ProductionSystem2_Countdown,
    'ProductionSystem3': ProductionSystem3_Countdown
}

AllProductionSystems = {
    'ProductionSystem1': [ProceduralProductions, ProductionSystem1_Countdown],
    'ProductionSystem2': [MotorProductions, ProductionSystem2_Countdown],
    'ProductionSystem3': [VisualProductions, ProductionSystem3_Countdown]
}


# -------------------------
# Initialize and Run the Production Cycle
# -------------------------
ps = ProductionCycle()
ps.run_cycles(memories, AllProductionSystems, DelayResetValues, cycles=40, millisecpercycle=50)
