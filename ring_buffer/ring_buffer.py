class RingBuffer:
  def __init__(self, capacity):
    self.buffer = [None] * capacity
    self.oldest = None
    self.length = 0
    self.capacity = capacity

  def append(self, item):
    if self.oldest is None:
      self.buffer[0] = item
      self.oldest = 0
      self.length = 1
    elif self.length < len(self.buffer):
      self.buffer[self.length] = item
      self.length += 1
    else:
      self.buffer[self.oldest] = item
      self.oldest = (self.oldest + 1) % self.length

  def get(self):
    if self.length == 0:
      return []
    elif self.length < len(self.buffer):
      return self.buffer[:self.length]
    return self.buffer
