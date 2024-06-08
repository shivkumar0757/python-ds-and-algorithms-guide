# Bitmasking and Bitwise Operations

Bitmasking involves using bitwise operators to manipulate individual bits within an integer. This technique is useful for various tasks like toggling, setting, clearing bits, and checking their status. Understanding bitwise operations is crucial for efficient low-level data manipulation.


*Bitwise operations involve operations between two bits. Below is a table showing all possible combinations for AND, OR, and XOR operations.

| A | B | A & B | A &#124; B | A ^ B |
|---|---|---------|--------|---------|
| 0 | 0 |   0     |   0    |    0    |
| 0 | 1 |   0     |   1    |    1    |
| 1 | 0 |   0     |   1    |    1    |
| 1 | 1 |   1     |   1    |    0    |

AND (&) , OR (|) , XOR (^)
##

## Bitwise Operators in Python

### AND (&): Sets each bit to 1 if both bits are 1.

**Example:**

```python
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a & b  # Binary: 0001 (Decimal: 1)
```

### OR (|): Sets each bit to 1 if one of the bits is 1.

**Example:**

```python
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a | b  # Binary: 0111 (Decimal: 7)
```

### XOR (^): Sets each bit to 1 if only one of the bits is 1.

**Example:**

```python
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a ^ b  # Binary: 0110 (Decimal: 6)
```

### NOT (~): Inverts all the bits.

**Example:**

```python
a = 5  # Binary: 0101
result = ~a  # Binary: ...11111010 (2's complement, Decimal: -6)
```

### Left Shift (<<): Shifts bits to the left, adding zeros from the right.

**Example:**

```python
a = 5  # Binary: 0101
result = a << 1  # Binary: 1010 (Decimal: 10)
```

### Right Shift (>>): Shifts bits to the right, discarding bits shifted off.

**Example:**

```python
a = 5  # Binary: 0101
result = a >> 1  # Binary: 0010 (Decimal: 2)
```

## Common Bitmasking Operations

### Setting a Bit

**Goal:** Set a specific bit to 1.  
**Operation:** `number | (1 << bit_position)`  
**Example:**

```python
number = 5  # Binary: 0101
bit_position = 1
result = number | (1 << bit_position)  # Binary: 0111, Decimal: 7
```

**Explanation:** `1 << bit_position` creates a mask with a 1 at the desired bit position. The OR operation sets this bit to 1 in the number.

### Clearing a Bit

**Goal:** Set a specific bit to 0.  
**Operation:** `number & ~(1 << bit_position)`  
**Example:**

```python
number = 5  # Binary: 0101
bit_position = 0
result = number & ~(1 << bit_position)  # Binary: 0100, Decimal: 4
```

**Explanation:** `1 << bit_position` creates a mask with a 1 at the desired bit position. The NOT operation inverts this mask. The AND operation clears the bit to 0 in the number.

### Toggling a Bit

**Goal:** Flip a specific bit (0 to 1 or 1 to 0).  
**Operation:** `number ^ (1 << bit_position)`  
**Example:**

```python
number = 5  # Binary: 0101
bit_position = 2
result = number ^ (1 << bit_position)  # Binary: 0001, Decimal: 1
```

**Explanation:** `1 << bit_position` creates a mask with a 1 at the desired bit position. The XOR operation toggles this bit in the number.

### Checking if a Bit is Set

**Goal:** Determine if a specific bit is 1.  
**Operation:** `number & (1 << bit_position) != 0`  
**Example:**

```python
number = 5  # Binary: 0101
bit_position = 2
is_set = number & (1 << bit_position) != 0  # True, as the bit is set
```

**Explanation:** `1 << bit_position` creates a mask with a 1 at the desired bit position. The AND operation checks if this bit is 1 in the number.

### Counting Set Bits (Hamming Weight)

**Goal:** Count the number of bits set to 1.  
**Operation:** `bin(number).count('1')`  
**Example:**

```python
number = 5  # Binary: 0101
count = bin(number).count('1')  # 2
```

**Explanation:** Converts the number to its binary representation and counts the number of 1s.

### Getting the Lowest Set Bit

**Goal:** Find the position of the lowest bit set to 1.  
**Operation:** `number & -number`  
**Example:**

```python
number = 10  # Binary: 1010
lowest_set_bit = number & -number  # Binary: 0010, Decimal: 2
```

**Explanation:** `-number` inverts the bits of `number` and adds 1 (two's complement). The AND operation isolates the lowest set bit.

## Practical Examples

### Example 1: Checking Permissions

Consider a system where different permissions are represented by bits:

- Read: `001` (1)
- Write: `010` (2)
- Execute: `100` (4)

To check if a user has write permission:

```python
permissions = 5  # Binary: 101 (Read and Execute)
write_permission = 2  # Binary: 010
has_write = permissions & write_permission != 0  # False
```

### Example 2: Subset Generation

Using bitmasking to generate all subsets of a set:

```python
def generate_subsets(nums):
    n = len(nums)
    subsets = []
    for i in range(1 << n):  # 2^n combinations
        subset = []
        for j in range(n):
            if i & (1 << j):  # Check if j-th bit is set
                subset.append(nums[j])
        subsets.append(subset)
    return subsets

nums = [1, 2, 3]
print(generate_subsets(nums))
```

In this example, each integer from 0 to `2^n - 1` represents a bitmask where each bit indicates whether an element is included in the subset.

Bitmasking is a powerful tool in competitive programming and system design, enabling efficient bit-level operations and manipulations.
