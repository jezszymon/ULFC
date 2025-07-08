<p align="center">
  <img src="src\ULFC.png" alt="Opis" width="150"/>
</p>

# **ULFC 1.0 Documentation**

### Official documentation for ULFC 1.0

## Contents

*   [Tools](#tools)
*   [Syntax](#syntax)
    *   [Source Files](#source-files)
    *   [Prefixes](#prefixes)
    *   [Characters](#characters)
    *   [Flags](#flags)
    *   [PC](#pc)
*   [Instruction](#instruction)
    *   [NOP](#nop)
    *   [ADD](#add)
    *   [SUB](#sub)
    *   [MUL](#mul)
    *   [DIV](#div)
    *   [AND](#and)
    *   [NAND](#nand)
    *   [NOR](#nor)
    *   [XOR](#xor)
    *   [XNOR](#xnor)
    *   [MOV](#mov)
    *   [RSH](#rsh)
    *   [LSH](#lsh)
    *   [LDI](#ldi)
    *   [STR](#str)
    *   [LOD](#lod)
    *   [JMP](#jmp)
    *   [INC](#inc)
    *   [DEC](#dec)
    *   [NEG](#neg)
    *   [NOT](#not)
    *   [PSH](#psh)
    *   [POP](#pop)
    *   [CAL](#cal)
    *   [RET](#ret)
    *   [IN](#in)
    *   [OUT](#out)
    *   [HLT](#hlt)

## **Tools**

> **ULFC Documentation:**  
> [https://github.com/jezszymon/ULFC](https://github.com/jezszymon/ULFC)

> **ULFC To ISA:**  
> [https://www.none.com](https://www.none.com)

> **Python-Like to ULFC:**  
> [https://www.none.com](https://www.none.com)

> **ULFC Emulator:**  
> [https://www.none.com](https://www.none.com)

## **Syntax**

### **Source Files**

ULFC uses source files with the `.ulfc` extension.

`ULFC source files are utilized within Visual Studio Code. To enhance editing experience, the "ULFC Syntax" extension is available in the VS Code Marketplace, providing syntax highlighting and basic IntelliSense support for ULFC files.`

### **Prefixes**

**Register -** `R`\
**Memory -** `M`\
**Labels -** `.`\
**Comments -** `\\`\
**Ports -** `%`\
**Flags -** `@`

### **Characters**

In this assembler, any character specified inside backticks `''` is interpreted as its corresponding **7-bit ASCII code**.

For example:

*   The notation `` `A` `` represents the ASCII code `65`
*   Similarly, `` `0` `` corresponds to ASCII code `48`.

> Note: Only the standard 7-bit ASCII range (0–127) is supported for this notation.

For a comprehensive reference, you can view the full 7-bit ASCII table here:  [ASCII Table](https://www.ascii-code.com/)

### Flags

| **Flag** | **Full name** | **Description** |
| --- | --- | --- |
| `Z` | Zero | The jump occurs if the result of the previous operation was zero. Commonly used after comparisons when two values are equal. |
| `NZ` | Not Zero | The jump occurs if the result was not zero. Used when values are not equal. |
| `C` | Carry | The jump occurs if a carry was generated from the most significant bit in an unsigned operation (e.g. addition). Indicates that the result exceeded the register’s capacity. |
| `NC` | No Carry | The jump occurs if no carry was generated. Indicates the result stayed within the register’s range. |
| `S` | Sign (negative) | The jump occurs if the result was negative (sign bit is set). Typically used for signed comparisons. |
| `NS` | No sign(positive) | The jump occurs if the result was positive or zero (sign bit is clear). Indicates a non-negative outcome. |
| `O` | Overflow | The jump occurs if a signed overflow occurred (e.g. adding two positives gave a negative). Used for detecting arithmetic errors in signed operations. |
| `NO` | No Overflow | The jump occurs if no overflow occurred during the previous operation. Confirms that the result of a signed operation is valid. |

## PC
In ULFC assembly, the Program Counter (PC) is treated as a normal register.\

This means you can load the current value of the PC into any general-purpose register using a simple move instruction, for example:\
`MOV R0, PC  ; Load the current PC value into register R0`\
This instruction copies the value of the program counter directly into R0, just like with any other register.

## **Instruction**

### NOP

#### _Description_

The `NOP` instruction does nothing; it has no effect on registers or memory and is typically used for timing or alignment purposes.

`NOP` requires 0 operands.

| **Example** |
| --- |
| NOP |


### ADD

#### _Description_

The `ADD` instruction adds the contents of the second and third values and stores the result in the first register.

#### _Operands_

`ADD` requires 3 operands.

| **Destination** | **Source1** | **Source2** | **Example** |
| --- | --- | --- | --- |
| Register | Register | Register | ADD R1 R2 R3 |
| Register | Immediate | Register | ADD R1 5 R3 |
| Register | Register | Immediate | ADD R1 R2 7 |
| Register | Immediate | Immediate | ADD R1 5 7 |

### SUB

#### _Description_

The `SUB` instruction subtracts the third value from the second value and stores the result in the first register.

#### _Operands_

`SUB` requires 3 operands.

| **Destination** | **Source1** | **Source2** | **Example** |
| --- | --- | --- | --- |
| Register | Register | Register | SUB R1 R2 R3 |
| Register | Immediate | Register | SUB R1 5 R3 |
| Register | Register | Immediate | SUB R1 R2 7 |
| Register | Immediate | Immediate | SUB R1 5 7 |

### MUL

#### _Description_

The `MUL` instruction multiplies two values (registers or a register and immediate) and stores the result in a register. Used for arithmetic operations.

#### _Operands_

`MUL` requires 3 operands.

| **Destination** | **Source1** | **Source2** | **Example** |
| --- | --- | --- | --- |
| Register | Register | Register | MUL R1 R2 R3 |
| Register | Immediate | Register | MUL R1 5 R3 |
| Register | Register | Immediate | MUL R1 R2 7 |
| Register | Immediate | Immediate | MUL R1 5 7 |

### DIV

#### _Description_

The `DIV` instruction performs division between two values and gives the result as a quotient. Often used in math operations.

#### _Operands_

`DIV` requires 3 operands.

| **Destination** | **Source1** | **Source2** | **Example** |
| --- | --- | --- | --- |
| Register | Register | Register | DIV R1 R2 R3 |
| Register | Immediate | Register | DIV R1 5 R3 |
| Register | Register | Immediate | DIV R1 R2 7 |
| Register | Immediate | Immediate | DIV R1 5 7 |

### AND

#### _Description_

The `AND` instruction performs a bitwise AND operation between two operands (registers or register and immediate), setting each bit in the result to 1 only if both corresponding bits of the operands are 1. It’s commonly used for masking bits, clearing specific bits, or checking bit flags.

#### _Operands_

`AND` requires 3 operands.

| **Destination** | **Source1** | **Source2** | **Example** |
| --- | --- | --- | --- |
| Register | Register | Register | AND R1 R2 R3 |
| Register | Immediate | Register | AND R1 5 R3 |
| Register | Register | Immediate | AND R1 R2 7 |
| Register | Immediate | Immediate | AND R1 5 7 |

### NAND

#### _Description_

The `NAND` instruction performs a bitwise AND between two values and then inverts the result. It sets each bit to 1 unless both input bits are 1. Commonly used in logic operations and bit manipulation.

#### _Operands_

`NAND` requires 3 operands.

| **Destination** | **Source1** | **Source2** | **Example** |
| --- | --- | --- | --- |
| Register | Register | Register | NAND R1 R2 R3 |
| Register | Immediate | Register | NAND R1 5 R3 |
| Register | Register | Immediate | NAND R1 R2 7 |
| Register | Immediate | Immediate | NAND R1 5 7 |

### NOR

#### _Description_

The `NOR` instruction performs a bitwise NOR operation on the second and third values and stores the result in the first register.

#### _Operands_

`NOR` requires 3 operands.

| **Destination** | **Source1** | **Source2** | **Example** |
| --- | --- | --- | --- |
| Register | Register | Register | NOR R1 R2 R3 |
| Register | Immediate | Register | NOR R1 5 R3 |
| Register | Register | Immediate | NOR R1 R2 7 |
| Register | Immediate | Immediate | NOR R1 5 7 |

### XOR

#### _Description_

The `XOR` instruction performs a bitwise exclusive OR between two values. Each bit is set to 1 only if the bits are different. Used for toggling bits, clearing registers, or simple encryption.#### _Operands_

#### _Operands_

`XOR` requires 3 operands.

| **Destination** | **Source1** | **Source2** | **Example** |
| --- | --- | --- | --- |
| Register | Register | Register | XOR R1 R2 R3 |
| Register | Immediate | Register | XOR R1 5 R3 |
| Register | Register | Immediate | XOR R1 R2 7 |
| Register | Immediate | Immediate | XOR R1 5 7 |

### XNOR

#### _Description_

The `XNOR` instruction performs a bitwise exclusive NOR — it sets each bit to 1 only if the input bits are the same. It’s the inverse of XOR. Used in logic operations where equality is needed at the bit level.

#### _Operands_

`XNOR` requires 3 operands.

| **Destination** | **Source1** | **Source2** | **Example** |
| --- | --- | --- | --- |
| Register | Register | Register | XNOR R1 R2 R3 |
| Register | Immediate | Register | XNOR R1 5 R3 |
| Register | Register | Immediate | XNOR R1 R2 7 |
| Register | Immediate | Immediate | XNOR R1 5 7 |

### MOV

#### _Description_

The `MOV` instruction copies the value from the second operand into the first register.

#### _Operands_

`MOV` requires 2 operands.

| **Destination** | **Source1** | **Example** |
| --- | --- | --- |
| Register | Register | MOV R1 R2 |
| Register | Immediate | MOV R1 5 |

### RSH

#### _Description_

The `RSH` instruction does a bitwise right shift of a value, then it stores the result in a register.

#### _Operands_

`RSH` requires 2 operands.

| **Destination** | **Source1** | **Example** |
| --- | --- | --- |
| Register | Register | RSH R1 R2 |
| Register | Immediate | RSH R1 5 |

### LSH

#### _Description_

The `LSH` instruction does a bitwise left shift of a value, then it stores the result in a register.

#### _Operands_

`LSH` requires 2 operands.

| **Destination** | **Source1** | **Example** |
| --- | --- | --- |
| Register | Register | LSH R1 R2 |
| Register | Immediate | LSH R1 8 |

### LDI

#### _Description_

The `LDI` instruction loads an immediate (constant) value directly into a register. It is used to assign specific numeric values without accessing memory.

#### _Operands_

`LDI` requires 2 operands.

| **Destination** | **Source1** | **Example** |
| --- | --- | --- |
| Register | Immediate | LDI R1 5 |

### STR

#### _Description_

The `STR` (Store) instruction writes the value from a register into a specific memory address. Used to save data to memory.

#### _Operands_

`STR` requires 2 operands.

| **Destination (Pointer)** | **Source1** | **Example** |
| --- | --- | --- |
| Ram Address | Register | STR M1 R2 |
| Ram Address | Immediate | STR M1 2 |
| Register | Register | STR R1 R2 |
| Register | Immediate | STR R1 2 |

### LOD

#### _Description_

The `LOD` (Load) instruction reads a value from a specific memory address into a register. Used to load data from memory.

#### _Operands_

`LOD` requires 2 operands.

| **Destination** | **Source1 (Pointer)** | **Example** |
| --- | --- | --- |
| Register | Register | LOD R1 R2 |
| Register | Ram Address | LOD R1 M5 |

### JMP

#### _Description_

The `JMP` instruction performs a conditional jump to the address stored in a register, based on a specified flag. If the condition is met (e.g., zero, carry, overflow), execution continues from the target address. Otherwise, the next instruction is executed as usual. This allows for implementing logic, loops, and branches in the program flow.

#### _Operands_

`JMP` requires 2 operands.

| **Condition** | **Source1** | **Example** |
| --- | --- | --- |
| [Flag](#flags) | Register | JMP @Z R2 |
| [Flag](#flags) | Immediate | JMP @O 5 |

### INC

#### _Description_

The `INC` instruction increases the value in a register by 1. Used for counting or looping. Affects flags like Zero or Overflow.

#### _Operands_

`INC` requires 2 operands.

| **Destination** | **Source1** | **Example** |
| --- | --- | --- |
| Register | Register | INC R1 R2 |
| Register | Immediate | INC R1 5 |

### DEC

#### _Description_

The `DEC` instruction decrements (subtracts 1 from) the value stored in a register. It’s commonly used in loops, countdowns, or stepping backward through data.

#### _Operands_

`DEC` requires 2 operands.

| **Destination** | **Source1** | **Example** |
| --- | --- | --- |
| Register | Register | DEC R1 R2 |
| Register | Immediate | DEC R1 5 |

### NEG

#### _Description_

The `NEG` instruction negates the value in a register — it changes its sign by computing the two’s complement. Essentially, it turns a positive number into its negative counterpart and vice versa.

#### _Operands_

`NEG` requires 2 operands.

| **Destination** | **Source1** | **Example** |
| --- | --- | --- |
| Register | Register | NEG R1 R2 |
| Register | Immediate | NEG R1 5 |

### NOT

#### _Description_

The `NOT` instruction inverts all bits in a register — it performs a bitwise logical NOT. Each 1 becomes 0, and each 0 becomes 1. Used to flip bits or prepare values for operations like NAND or NOR.

#### _Operands_

`NOT` requires 2 operands.

| **Destination** | **Source1** | **Example** |
| --- | --- | --- |
| Register | Register | NOT R1 R2 |
| Register | Immediate | NOT R1 5 |

### PSH

#### _Description_

The `PSH` (Push) instruction stores a register’s value onto the stack. It decreases the stack pointer and places the data at the new top of the stack. Used to save values during function calls or interrupts.

#### _Operands_

`PSH` requires 1 operands.

| **Source1** | **Example** |
| --- | --- |
| Register | PSH R2 |
| Register | PSH 5 |

### POP

#### _Description_

The `POP` instruction retrieves the top value from the stack into a register. It loads the value and then increases the stack pointer. Used to restore saved data.

#### _Operands_

`POP` requires 1 operands.

| **Source1** | **Example** |
| --- | --- |
| Register | POP R2 |

### CAL

#### _Description_

The CAL (Call) instruction jumps to a subroutine (function) and saves the return address on the stack. Execution continues from the subroutine, and later returns with RET. Used for function calls.

#### _Operands_

`CAL` requires 1 operands.

| **Source1** | **Example** |
| --- | --- |
| Immediate | CAL .label |
| Register | CAL R2 |

### RET

#### _Description_

The `RET` (Return) instruction restores the return address from the stack and jumps back to that point in the code. It ends a subroutine and resumes execution after the CAL (call).

#### _Operands_

`RET` requires 0 operands.

| **Example** |
| --- |
| RET |

### OUT

#### _Description_

The IN instruction reads data from an input port or device into a register. Used for receiving data from peripherals.

#### _Operands_

`OUT` requires 2 operands.

| **Destination** | **Source1** | **Example** |
| --- | --- | --- |
| Register | Port | IN R1 %1 |

### IN

#### _Description_

The OUT instruction sends data from a register to an output port or device. Used to transmit data to peripherals.

#### _Operands_

`OUT` requires 2 operands.

| **Destination** | **Source1** | **Example** |
| --- | --- | --- |
| Port | Register | OUT %1 R1 |
| Port | Immediate | OUT %1 1 |

### HLT

#### _Description_

The `HLT` (Halt) instruction stops the processor from executing further instructions until it is reset or interrupted. Used to pause or stop the CPU safely.

#### _Operands_

`HLT` requires 0 operands.

| **Example** |
| --- |
| HLT |