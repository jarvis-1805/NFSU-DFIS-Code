# Description: To imlpement POC of blockchain algorithm!

import hashlib

# Create Block
class Block:

  def __init__(self, data, previous_hash):
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calculate_hash()

  # How to calulate the hash
  def calculate_hash(self):
    sha = hashlib.sha256()
    sha.update( str(self.data).encode('utf-8') + 
                str(self.previous_hash).encode('utf-8') )
    return sha.hexdigest()
  
# Blockchain
class Blockchain:

  def __init__(self):
    self.chain = [self.create_genesis_block()]

  # Create first block
  def create_genesis_block(self):
    return Block("Genesis Block", "0")
  
  # create 2nd block
  def add_block(self, data):
    prev_block = self.chain[-1]
    new_block = Block(data, prev_block.hash)
    self.chain.append(new_block)

# Make a blockchain
blockchain = Blockchain()
blockchain.add_block("First Block")
blockchain.add_block("Second Block")
blockchain.add_block("Third Block")

print("\nBlockchain")
print("----------------------------------------------------------------\n")
for block in blockchain.chain:
  print("Data: ", block.data)
  print("Previous Hash: ", block.previous_hash)
  print("Hash: ", block.hash)
  print("\n----------------------------------------------------------------\n")