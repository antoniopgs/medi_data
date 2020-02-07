# ---------- DEPENDENCIES AND OTHERS ----------
from datetime import datetime
import random
blockchains = []
n = 0

# ---------- BLOCK CLASS ----------
class Block:
    def __init__(self, data, previous_block=None):
        self.data = data
        self.time = datetime.now()

    def __repr__(self):
        return f"""----- NEW RECORD -----
Time: {self.time}
Data: {self.data}"""


# ---------- BLOCKCHAIN CLASS ----------
class Blockchain:
    def __init__(self):
        # Set "Tail Block" default as none. This will help identify if Blockchain is empty or not:
        self.tail_block = None
        # Generate Unique Address:
        while True:
            address = hash(random.randint(1, 100))
            if address not in blockchains:
                self.address = address
                blockchains.append(self)
                break
                        
    def __iter__(self):
        return self

    def __next__(self):
        # If Blockchain is empty:
        if not self.tail_block:
            raise StopIteration
        # If Blockchain is not empty:
        else:
            # 'n' counts iterations of "__next__()", or how many times the "__next__()" function has been run.
            global n
            n += 1
            # If it's the first "__next__()" iteration:
            if n == 1:
                return self.tail_block
            # If it's after the first "__next__()" iteration:
            else:
                current_block = self.tail_block
                for i in range(n-1):
                    current_block = current_block.previous_block
                if not current_block:
                    # Reset "n" to 0, so that next iteration works the same:
                    n = 0
                    raise StopIteration
                else:
                    return current_block
            
    def __repr__(self):
        return f"{self.address}"

    def add_block(self, data):         
    # Check to see if Blockchain is empty:
        if not self.tail_block:
            new_block = Block(data)
        # If it's not empty, the new block's "previous block" will be the existing "tail block"
        else:
            new_block = Block(data, self.tail_block)
        # Update "Tail Block" to the newly created block
        self.tail_block = new_block

    def view(self):
        if not [block for block in self]:
            print("This Blockchain is empty.\n")
        else:
            for block in self:
                print(block)

b1 = Blockchain()
b1.add_block("Patient shows sign of x. Will start treatment.")
b1.view()
