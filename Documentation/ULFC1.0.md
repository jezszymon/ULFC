<p align="center">
  <img src="src\ULFC.png" alt="Opis" width="128"/>
</p>

# **ULFC 1.0 Documentation**

### Official documentation for ULFC 1.0

## Contents

*   [Tools](#tools)
*   [Syntax](#syntax)
    *   [Source Files](#source-files)
    *   [Prefixes](#prefixes)
    *   [Characters](#characters)
*   [Instruction](#instruction)
    *   [ADD](#add)
    *   [SUB](#sub)
    *   [RSH](#rsh)
    *   [LSH](#lsh)
    *   [LDI](#ldi)

## **Tools**

> **ULFC Documentation:**  
> [https://www.none.com](https://www.none.com)

> **ULFC To ISA:**  
> [https://www.none.com](https://www.none.com)

> **ULFC Emulator:**  
> [https://www.none.com](https://www.none.com)

## **Syntax**

### **Source Files**

ULFC uses source files with the `.ulfc` extension.

`ULFC source files are utilized within Visual Studio Code. To enhance editing experience, the "ULFC Syntax" extension is available in the VS Code Marketplace, providing syntax highlighting and basic IntelliSense support for ULFC files.`

### **Prefixes**

**Register -** `R`  
**Memory -** `M`  
**Labels -** `.`  
**Comments -** `\\`

### **Characters**

In this assembler, any character specified inside backticks `''` is interpreted as its corresponding **7-bit ASCII code**.

For example:

*   The notation `` `A` `` represents the ASCII code `65`
*   Similarly, `` `0` `` corresponds to ASCII code `48`.

> Note: Only the standard 7-bit ASCII range (0–127) is supported for this notation.

For a comprehensive reference, you can view the full 7-bit ASCII table here:  [ASCII Table](https://www.ascii-code.com/)

## **Instruction**

### ADD

#### _Description_

The `ADD` instruction adds the contents of the second and third values and stores the result in the first register.

#### _Operands_

ADD requires 3 operands.

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

SUB requires 3 operands.

| **Destination** | **Source1** | **Source2** | **Example** |
| --- | --- | --- | --- |
| Register | Register | Register | SUB R1 R2 R3 |
| Register | Immediate | Register | SUB R1 5 R3 |
| Register | Register | Immediate | SUB R1 R2 7 |
| Register | Immediate | Immediate | SUB R1 5 7 |

### RSH

#### _Description_

The `RSH` instruction does a bitwise right shift of a value, then it stores the result in a register.

#### _Operands_

RSH requires 2 operands.

| **Destination** | **Source1** | **Example** |
| --- | --- | --- |
| Register | Register | RSH R1 R2 |
| Register | Immediate | RSH R1 5 |

### LSH

#### _Description_

The `LSH` instruction does a bitwise left shift of a value, then it stores the result in a register.

#### _Operands_

LSH requires 2 operands.

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
| Register | Register | LDI R1 R2 |
| Register | Immediate | LDI R1 5 |