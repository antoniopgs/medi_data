# ---------- DEPENDENCIES AND OTHERS ----------
from datetime import datetime
import random
blockchains = []
n = 0

# ---------- BLOCK CLASS ----------
class Block:
    def __init__(self, data, previous_block = None):
        self.data = data
        self.time = datetime.now().strftime("%A, %d %B %Y - %H:%M:%S")
        self.previous_block = previous_block

    def __repr__(self):
        return f"""----- NEW RECORD -----
Time: {self.time}
Data: {self.data}
"""


# ---------- BLOCKCHAIN CLASS ----------
class Blockchain:

    # Protect Blockchain Memory Address from Prints:
    def __repr__(self):
        return None

    # Create New Blockchain:
    def __init__(self):
        # Set "Tail Block" default as none. This will help identify if Blockchain is empty or not:
        self.tail_block = None
        # Generate Unique Address:
        while True:
            address = hash(random.randint(1, 100))
            if address not in blockchains:
                self.address = address
                self.private_key = hash(random.randint(1,100))
                print(f"""----- PERSONAL DATA -----
Your Address: {self.address}
Your Private Key: {self.private_key}
WARNING: This data will never be shown again! Store it safely.
""")
                blockchains.append(self)
                break

    # Add new Block:
    def add_block(self, address, private_key):
        if address != self.address or private_key != self.private_key:
            print("Invalid Credentials.")
        else:
            data = input("Insert Medical Data: ")
            if not self.tail_block:
                new_block = Block(data)
            else:
                new_block = Block(data, self.tail_block)
            self.tail_block = new_block

    def __iter__(self):
        return self

    def __next__(self):
        global n
        n += 1
        # If it's the first iteration:
        if n == 1:
            return self.tail_block
        # If it's after the first iteration:
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


    def view(self, address, private_key):
        if address != self.address or private_key != self.private_key:
            print("Invalid Credentials.")
        else:
            if not self.tail_block:
                print("Chain is empty.\n")
            else:
                for block in self:
                    print(block)
